from database.postgres import PostgresDB
from trading_price.etl.extract import Extract
from trading_price.etl.transform import Transform
from trading_price.etl.load import Load
import os 

def pipeline()->bool:
    
    api_key_id = os.environ.get("api_key_id")
    api_secret_key = os.environ.get("api_secret_key")
    
    # extract data 
    df = Extract.extract(
        stock_ticker="tsla", 
        api_key_id=api_key_id,
        api_secret_key=api_secret_key, 
        start_date="2020-01-01", 
        end_date="2020-01-05"
    )   
    df_exchange_codes = Extract.extract_exchange_codes("trading_price/data/exchange_codes.csv")

    # transform data
    df_transform = Transform.transform(
        df=df,
        df_exchange_codes=df_exchange_codes
    )

    # load file (upsert)
    Load.load(
        df=df_transform,
        load_target="file",
        target_file_directory="trading_price/data",
        target_file_name="tesla.parquet",
    )   

    engine = PostgresDB.create_pg_engine()

    # load database (upsert)
    Load.load(
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