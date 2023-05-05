from database.postgres import PostgresDB
from weather.etl.extract import Extract
from weather.etl.transform import Transform
from weather.etl.load import Load
import os 
import logging 

def pipeline()->bool:
    logging.basicConfig()
    logging.basicConfig(format="[%(levelname)s][%(asctime)s][%(filename)s]: %(message)s") # format: https://docs.python.org/3/library/logging.html#logging.LogRecord
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)

    api_key = os.environ.get("api_key")
    
    logger.info("Commencing extract from weather api and csv")
    # extract 
    df = Extract.extract(
        api_key=api_key, 
        fp_cities="weather/data/australian_capital_cities.csv",
        temperature_units="metric"
    )
    logger.info("Extract complete")

    logger.info("Commencing extract from city csv")
    df_population = Extract.extract_population(fp_population="weather/data/australian_city_population.csv")
    logger.info("Extract complete")

    # transform 
    logger.info("Commencing transform")
    df_transformed = Transform.transform(df=df, df_population=df_population)
    logger.info("Transform complete")

    logger.info("Commencing load to file")
    # load file 
    Load.load(
        df=df_transformed,
        load_target="file", 
        load_method="upsert", 
        target_file_directory="weather/data", 
        target_file_name="weather.parquet", 
    )
    logger.info("Load complete")

    # create connection to database 
    engine = PostgresDB.create_pg_engine()
    
    logger.info("Commencing load to database")
    # load database 
    Load.load(
        df=df_transformed,
        load_target="database", 
        load_method="upsert", 
        target_database_engine=engine,
        target_table_name="weather"
    )
    logger.info("Load complete")

    return True  

if __name__ == "__main__":
    pipeline()
        