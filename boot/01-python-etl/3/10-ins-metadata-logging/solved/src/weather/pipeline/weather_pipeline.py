from database.postgres import PostgresDB
from weather.etl.extract import Extract
from weather.etl.transform import Transform
from weather.etl.load import Load
import os 
import logging 
import yaml 
from utility.metadata_logging import MetadataLogging
import datetime as dt
from io import StringIO

def pipeline()->bool:
    log_stream = StringIO()
    logging.basicConfig(stream=log_stream, format="[%(levelname)s][%(asctime)s][%(filename)s]: %(message)s") # format: https://docs.python.org/3/library/logging.html#logging.LogRecord
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)
    
    try: 
        # get yaml config 
        with open("weather/config.yaml") as stream:
            config = yaml.safe_load(stream)
        
        api_key = os.environ.get("api_key")

        metadata_logger = MetadataLogging()
        
        metadata_logger_table = f"metadata_log_{config['load']['database']['target_table_name']}"
        metadata_logger_run_id = metadata_logger.get_latest_run_id(db_table=metadata_logger_table)
        metadata_logger.log(
            run_timestamp=dt.datetime.now(),
            run_status="started",
            run_id=metadata_logger_run_id, 
            run_config=config,
            db_table=metadata_logger_table
        )
        
        logger.info("Commencing extract from weather api and csv")
        # extract 
        df = Extract.extract(
            api_key=api_key, 
            fp_cities=config["extract"]["fp_cities"],
            temperature_units=config["extract"]["temperature_units"]
        )
        logger.info("Extract complete")

        logger.info("Commencing extract from city csv")
        df_population = Extract.extract_population(fp_population=config["extract"]["fp_population"])
        logger.info("Extract complete")

        # transform 
        logger.info("Commencing transform")
        df_transformed = Transform.transform(df=df, df_population=df_population)
        logger.info("Transform complete")

        logger.info("Commencing load to file")
        # load file 
        Load.load(
            df=df_transformed,
            load_target=config["load"]["file"]["load_target"], 
            load_method=config["load"]["file"]["load_method"], 
            target_file_directory=config["load"]["file"]["target_file_directory"], 
            target_file_name=config["load"]["file"]["target_file_name"], 
        )
        logger.info("Load complete")

        # create connection to database 
        engine = PostgresDB.create_pg_engine()
        
        logger.info("Commencing load to database")
        # load database 
        Load.load(
            df=df_transformed,
            load_target=config["load"]["database"]["load_target"], 
            load_method=config["load"]["database"]["load_method"], 
            target_database_engine=engine,
            target_table_name=config["load"]["database"]["target_table_name"]
        )
        logger.info("Load complete")
        
        metadata_logger.log(
            run_timestamp=dt.datetime.now(),
            run_status="completed",
            run_id=metadata_logger_run_id,
            run_config=config, 
            run_log=log_stream.getvalue(),
            db_table=metadata_logger_table
        )
        print(log_stream.getvalue())
        return True  
    except BaseException as e:
        logger.exception(e)
        metadata_logger.log(
            run_timestamp=dt.datetime.now(),
            run_status="error",
            run_id=metadata_logger_run_id,
            run_config=config, 
            run_log=log_stream.getvalue(),
            db_table=metadata_logger_table
        )
        print(log_stream.getvalue())
    
    

if __name__ == "__main__":
    pipeline()
        