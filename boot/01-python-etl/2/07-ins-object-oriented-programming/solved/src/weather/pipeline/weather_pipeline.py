from database.postgres import PostgresDB
from weather.etl.extract import Extract
from weather.etl.transform import Transform
from weather.etl.load import Load
import os 

def pipeline()->bool:

    api_key = os.environ.get("api_key")
    
    # extract 
    df = Extract.extract(
        api_key=api_key, 
        fp_cities="weather/data/australian_capital_cities.csv",
        temperature_units="metric"
    )
    df_population = Extract.extract_population(fp_population="weather/data/australian_city_population.csv")

    # transform 
    df_transformed = Transform.transform(df=df, df_population=df_population)

    # load file 
    Load.load(
        df=df_transformed,
        load_target="file", 
        load_method="upsert", 
        target_file_directory="weather/data", 
        target_file_name="weather.parquet", 
    )

    # create connection to database 
    engine = PostgresDB.create_pg_engine()

    # load database 
    Load.load(
        df=df_transformed,
        load_target="database", 
        load_method="upsert", 
        target_database_engine=engine,
        target_table_name="weather"
    )
    return True  

if __name__ == "__main__":
    if pipeline():
        print("success")