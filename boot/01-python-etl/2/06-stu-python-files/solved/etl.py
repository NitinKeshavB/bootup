import requests
# get alpaca api keys using this guide: https://alpaca.markets/docs/market-data/getting-started/#creating-an-alpaca-account-and-finding-your-api-keys
import pandas as pd

import datetime as dt 

def generate_datetime_ranges(
        start_date:str=None, 
        end_date:str=None, 
        )->list:
        """ 
        Generates a range of datetime ranges. 
        - start_date: provide a str with the format "yyyy-mm-dd"
        - end_date: provide a str with the format "yyyy-mm-dd" 
        Usage example: 
        - generate_datetime_ranges(start_date="2020-01-01", end_date="2022-01-02")
            returns: 
                [
                    'start_time': '2020-01-01T00:00:00.00Z', 'end_time': '2020-01-02T00:00:00.00Z'}, 
                    {'start_time': '2020-01-02T00:00:00.00Z', 'end_time': '2020-01-03T00:00:00.00Z'}
                ]
        """

        date_range = []
        if start_date is not None and end_date is not None: 
            dte_start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
            dte_end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
            date_range = [
                {
                    "start_time": (dte_start_date + dt.timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S.00Z"),
                    "end_time": (dte_start_date + dt.timedelta(days=i) + dt.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S.00Z"),
                }
            for i in range((dte_end_date - dte_start_date).days)]
        else: 
            raise Exception("The parameters passed in results in no action being performed.")

        return date_range  

def extract(
            stock_ticker:str, 
            api_key_id:str, 
            api_secret_key:str, 
            start_date:str=None, 
            end_date:str=None
        )->pd.DataFrame:
        """
        Extract trades data from the Alpaca API. 
        - stock_ticker: ticker of a stock e.g. tsla 
        - api_key_id: api key id from Alpaca
        - api_secret_key: api key secret from Alpaca
        - start_date: date to begin extracting data from 
        - end_date: date to stop extracting data to 
        
        Returns: 
        - DataFrame with the requested dates 
        """
        
        base_url = f"https://data.alpaca.markets/v2/stocks/{stock_ticker}/trades"
        response_data = []
        for date in generate_datetime_ranges(start_date=start_date, end_date=end_date):
            start_time = date.get("start_time")
            end_time = date.get("end_time")

            params = {
                "start": start_time,
                "end": end_time
            }

            # auth example: https://alpaca.markets/docs/api-references/trading-api/
            headers = {
                "APCA-API-KEY-ID": api_key_id,
                "APCA-API-SECRET-KEY": api_secret_key
            }
            response = requests.get(base_url, params=params, headers=headers)
            if response.json().get("trades") is not None: 
                response_data.extend(response.json().get("trades"))
        # read json data to a dataframe 
        df = pd.json_normalize(data=response_data, meta=["symbol"])
        return df 

def extract_exchange_codes(fp:str)->pd.DataFrame:
    """
    Reads exchange codes CSV file and returns a dataframe.
    - fp: filepath to the exchange codes CSV file
    """
    df = pd.read_csv(fp)
    return df


def transform(
        df:pd.DataFrame, 
        df_exchange_codes:pd.DataFrame
    )->pd.DataFrame:
    """
    Performs transformation on dataframe produced from extract() function.
    - df: dataframe produced from extract() function 
    - df_exchange_codes: dataframe produced from extract_exchange_codes() function 

    Returns: 
    - a transformed dataframe 
    """
    
    df_quotes_renamed = df.rename(columns={
        "t": "timestamp",
        "x": "exchange",
        "p": "price",
        "s": "size",
    })
    df_quotes_selected = df_quotes_renamed[['timestamp', 'exchange', 'price', 'size']]
    df_exchange = pd.merge(left=df_quotes_selected, right=df_exchange_codes, left_on="exchange", right_on="exchange_code").drop(columns=["exchange_code", "exchange"]).rename(columns={"exchange_name": "exchange"})
    # remove duplicates by doing a group by on the keys: timestamp and exchange
    # get the mean of price, and sum of size
    df_ask_bid_exchange_de_dup = df_exchange.groupby(["timestamp", "exchange"]).agg({
        "price": "mean",
        "size": "sum",
    }).reset_index()
    return df_ask_bid_exchange_de_dup

from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Float # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_creating_table.htm
from sqlalchemy.dialects import postgresql

def load(
        df: pd.DataFrame, 
        load_target:str, 
        load_method:str="upsert",
        target_file_directory:str=None,
        target_file_name:str=None,
        target_database_engine=None,
        target_table_name:str=None
    )->None:
    """
    Load dataframe to either a file or a database. 
    - df: pandas dataframe to load.  
    - load_target: choose either `file` or `database`.
    - load_method: currently only `upsert` is supported. 
    - target_file_directory: directory where the file will be written to in parquet format.
    - target_file_name: name of the target file e.g. stock.parquet. 
    - target_database_engine: SQLAlchemy engine for the target database. 
    - target_table_name: name of the SQL table to create and/or upsert data to. 
    """
    import os 
    if load_target == "file": 
        if load_method == "upsert": 
            # upsert (update and insert) data to a csv file 
            if target_file_name in os.listdir(f"{target_file_directory}/"): 
                df_current = pd.read_parquet(f"{target_file_directory}/{target_file_name}")
                df_concat = pd.concat(objs=[df_current,df[~df.index.isin(df_current.index)]]) # ~: converts true to false, and false to true. 
                df_concat.to_parquet(f"{target_file_directory}/{target_file_name}")
            else:
                # create file 
                df.to_parquet(f"{target_file_directory}/{target_file_name}")
    elif load_target == "database": 
        # create target table if not exists 
        meta = MetaData()
        stock_price_tesla_table = Table(
            target_table_name, meta, 
            Column("timestamp", String, primary_key=True),
            Column("exchange", String, primary_key=True),
            Column("price", Float),
            Column("size", Integer)
        )
        meta.create_all(target_database_engine) # creates table if it does not exist 
        insert_statement = postgresql.insert(stock_price_tesla_table).values(df.to_dict(orient='records'))
        upsert_statement = insert_statement.on_conflict_do_update(
            index_elements=['timestamp', 'exchange'],
            set_={c.key: c for c in insert_statement.excluded if c.key not in ['timestamp','exchange']})
        target_database_engine.execute(upsert_statement)

    
def pipeline()->bool:
    
    import os 
    api_key_id = os.environ.get("api_key_id")
    api_secret_key = os.environ.get("api_secret_key")
    db_user = os.environ.get("db_user")
    db_password = os.environ.get("db_password")
    db_server_name = os.environ.get("db_server_name")
    db_database_name = os.environ.get("db_database_name")

    # extract data 
    df = extract(
        stock_ticker="tsla", 
        api_key_id=api_key_id,
        api_secret_key=api_secret_key, 
        start_date="2020-01-01", 
        end_date="2020-01-05"
    )   
    df_exchange_codes = extract_exchange_codes("data/exchange_codes.csv")

    # transform data
    df_transform = transform(
        df=df,
        df_exchange_codes=df_exchange_codes
    )

    # load file (upsert)
    load(
        df=df_transform,
        load_target="file",
        target_file_directory="data",
        target_file_name="tesla.parquet",
    )   
    from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, Float # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_core_creating_table.htm
    from sqlalchemy.engine import URL
    from sqlalchemy.dialects import postgresql
    from sqlalchemy.schema import CreateTable 

    # create connection to database 
    connection_url = URL.create(
        drivername = "postgresql+pg8000", 
        username = db_user,
        password = db_password,
        host = db_server_name, 
        port = 5432,
        database = db_database_name, 
    )

    engine = create_engine(connection_url)

    # load database (upsert)
    load(
        df=df_transform,
        load_target="database",
        target_database_engine=engine,
        target_table_name="tesla_stock"
    )  
    return True  

if __name__ == "__main__": 
    # run the pipeline
    if pipeline(): 
        print("success")