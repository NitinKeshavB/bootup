import requests
import pandas as pd 
# from secrets_config import api_key # https://home.openweathermap.org/ 

def extract_city(
        api_key:str,
        city_name:str=None,
        temperature_units:str="metric"
    )->pd.DataFrame:
    """
    Extracting data from the weather API. 
    - api_key: api key 
    - city name: name of the city e.g. perth
    - temperature_units: choose one of "metric" or "imperial" or "standard"
    """
    params = {
        "q": city_name,
        "units": temperature_units,
        "appid": api_key
    }
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather", params=params)
    if response.status_code == 200: 
        weather_data = response.json()
    else: 
        raise Exception("Extracting weather api data failed. Please check if API limits have been reached.")
    df_weather_cities = pd.json_normalize(weather_data)
    return df_weather_cities

def extract(
        api_key:str,
        fp_cities:str,
        temperature_units:str="metric"
    )->pd.DataFrame:
    """
    Perform extraction using a filepath which contains a list of cities. 
    - api_key: api key 
    - fp_cities: filepath to a CSV file containing a list of cities 
    - temperature_units: choose one of "metric" or "imperial" or "standard"
    """

    # read list of cities
    df_cities = pd.read_csv(fp_cities)
    # request data for each city (json) and push to a list 
    df_concat = pd.DataFrame()
    for city_name in df_cities["city_name"]:
        df_extracted = extract_city(api_key=api_key,city_name=city_name,temperature_units=temperature_units)
        df_concat = pd.concat([df_concat,df_extracted])
    return df_concat.reset_index().drop(labels=["index"], axis=1)

def extract_population(
        fp_population:str
    )->pd.DataFrame:
    """Extracts data from the population file"""
    df_population = pd.read_csv(fp_population)
    return df_population

def transform(
        df:pd.DataFrame, 
        df_population:str=None
    )->pd.DataFrame:
    """
    Transform the raw dataframes. 
    - df: the dataframe produced from extract(). 
    - df_population: the dataframe produced from extract_population(). 
    """
    # set city names to lowercase 
    df["city_name"] = df["name"].str.lower()
    df_merged = pd.merge(left=df, right=df_population, on=["city_name"])
    df_selected = df_merged[["dt", "id", "name", "main.temp", "population"]] 
    df_selected["unique_id"] = df_selected["dt"].astype(str) + df_selected["id"].astype(str)
    # convert unix timestamp column to datetime 
    df_selected["dt"] = pd.to_datetime(df_selected["dt"], unit="s")
    # rename colum names to more meaningful names
    df_selected = df_selected.rename(columns={
        "dt": "datetime",
        "main.temp": "temperature"
    })
    df_selected = df_selected.set_index(["unique_id"])
    return df_selected 

import os 

def load(
    df:pd.DataFrame,
    load_target:str, 
    load_method:str="overwrite",
    target_file_directory:str=None,
    target_file_name:str=None,
    target_database_engine=None,
    target_table_name:str=None
    )->None:
    """
    Load dataframe to either a file or a database. 
    - df: pandas dataframe to load.  
    - load_target: choose either `file` or `database`.
    - load_method: choose either `overwrite` or `upsert`. defaults to `overwrite`. 
    - target_file_directory: directory where the file will be written to in parquet format.
    - target_file_name: name of the target file e.g. stock.parquet. 
    - target_database_engine: SQLAlchemy engine for the target database. 
    - target_table_name: name of the SQL table to create and/or upsert data to. 
    """
    if load_target.lower() == "file": 
        if load_method.lower() == "overwrite": 
            df.to_parquet(f"{target_file_directory}/{target_file_name}")
        elif load_method.lower() == "upsert": 
            if target_file_name in os.listdir(f"{target_file_directory}/"): 
                df_current = pd.read_parquet(f"{target_file_directory}/{target_file_name}")
                df_concat = pd.concat(objs=[df_current,df[~df.index.isin(df_current.index)]]) # ~: converts true to false, and false to true. 
                df_concat.to_parquet(f"{target_file_directory}/{target_file_name}")
            else:
                df.to_parquet(f"{target_file_directory}/{target_file_name}")

    elif load_target.lower() == "database": 
        from sqlalchemy import Table, Column, Integer, String, MetaData, Float
        from sqlalchemy.dialects import postgresql
        if load_method.lower() == "overwrite": 
            df.to_sql(target_table_name, target_database_engine)
        elif load_method.lower() == "upsert":
            meta = MetaData()
            weather_table = Table(
                target_table_name, meta, 
                Column("datetime", String, primary_key=True),
                Column("id", Integer, primary_key=True),
                Column("name", String),
                Column("temperature", Float),
                Column("population", Integer)
            )
            meta.create_all(target_database_engine) # creates table if it does not exist 
            insert_statement = postgresql.insert(weather_table).values(df.to_dict(orient='records'))
            upsert_statement = insert_statement.on_conflict_do_update(
                index_elements=['id', 'datetime'],
                set_={c.key: c for c in insert_statement.excluded if c.key not in ['id', 'datetime']})
            target_database_engine.execute(upsert_statement)

def pipeline()->bool:
    """
    Pipeline performs ETL from the Weather Data API and outputs transformed data to a parquet file and to a postgres database. 
    """
    import os 
    api_key = os.environ.get("api_key")
    db_user = os.environ.get("db_user")
    db_password = os.environ.get("db_password")
    db_server_name = os.environ.get("db_server_name")
    db_database_name = os.environ.get("db_database_name")

    # extract 
    df = extract(
        api_key=api_key, 
        fp_cities="data/australian_capital_cities.csv",
        temperature_units="metric"
    )
    df_population = extract_population(fp_population="data/australian_city_population.csv")

    # transform 
    df_transformed = transform(df=df, df_population=df_population)

    # load file 
    load(
        df=df_transformed,
        load_target="file", 
        load_method="upsert", 
        target_file_directory="data", 
        target_file_name="weather.parquet", 
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

    # load database 
    load(
        df=df_transformed,
        load_target="database", 
        load_method="upsert", 
        target_database_engine=engine,
        target_table_name="weather"
    )

    return True 
    
if __name__ == "__main__":
    # run etl pipeline 
    if pipeline(): 
        print("success")