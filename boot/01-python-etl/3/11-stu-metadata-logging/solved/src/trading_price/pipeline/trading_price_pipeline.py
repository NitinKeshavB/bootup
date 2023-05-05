from database.postgres import PostgresDB
from trading_price.etl.extract import Extract
from trading_price.etl.transform import Transform
from trading_price.etl.load import Load
from utility.date_time import DateTime
import os 
import logging
import yaml 
from io import StringIO
from utility.metadata_logging import MetadataLogging
import datetime as dt

def pipeline_per_stock(config, logger, run_log)->bool:

    # start the streamIO from a clean slate 
    run_log.seek(0)
    run_log.truncate(0)
    
    api_key_id = os.environ.get("api_key_id")
    api_secret_key = os.environ.get("api_secret_key")
    
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

    logger.info(f"Commencing pipeline for {config['extract']['stock_ticker']}⏳")
    logger.info("Commencing extraction")
    # extract data 
    try:
        # get dates 
        if config["extract"]["date_picker"].lower() == "most_recent_weekday":
            start_date = DateTime.get_most_recent_weekday_from_today()
            end_date = DateTime.get_end_date(start_date=start_date, days_from_start=1)
        elif config["extract"]["date_picker"].lower() == "date_range": 
            start_date = config["extract"]["start_date"]
            end_date = config["extract"]["end_date"]
        elif config["extract"]["date_picker"].lower() == "days_from_start":
            start_date = config["extract"]["start_date"]
            days_from_start = config["extract"]["days_from_start"]
            end_date = DateTime.get_end_date(start_date=start_date, days_from_start=days_from_start)
        elif config["extract"]["date_picker"].lower() == "days_from_end":
            end_date = config["extract"]["end_date"]
            days_from_end = config["extract"]["days_from_end"]
            start_date = DateTime.get_start_date(end_date=end_date, days_from_end=days_from_end)
        else: 
            logger.exception("Did not configure extraction dates correctly.")
        
        df = Extract.extract(
            stock_ticker=config["extract"]["stock_ticker"], 
            api_key_id=api_key_id,
            api_secret_key=api_secret_key, 
            start_date=start_date, 
            end_date=end_date
        )
        df_exchange_codes = Extract.extract_exchange_codes("trading_price/data/exchange_codes.csv")
        logger.info("Extraction complete")

        logger.info("Commencing transformation")
        # transform data
        df_transform = Transform.transform(
            df=df,
            df_exchange_codes=df_exchange_codes
        )
        logger.info("Transformation complete")

        # load file (upsert)
        logger.info("Commencing file load")
        Load.load(
            df=df_transform,
            load_target=config["load"]["file"]["load_target"],
            target_file_directory=config["load"]["file"]["target_file_directory"],
            target_file_name=config["load"]["file"]["target_file_name"],
        )   
        logger.info("File load complete")

        engine = PostgresDB.create_pg_engine()

        # load database (upsert)
        logger.info("Commencing database load")
        Load.load(
            df=df_transform,
            load_target=config["load"]["database"]["load_target"],
            target_database_engine=engine,
            target_table_name=config["load"]["database"]["target_table_name"]
        )  
        logger.info("Database load complete")
        logger.info(f"Pipeline for {config['extract']['stock_ticker']} complete ✅")

        metadata_logger.log(
            run_timestamp=dt.datetime.now(),
            run_status="completed",
            run_id=metadata_logger_run_id, 
            run_config=config,
            run_log=run_log.getvalue(),
            db_table=metadata_logger_table
        )
        
        
        return True
    except BaseException as e: 
        logger.exception(e)
        metadata_logger.log(
            run_timestamp=dt.datetime.now(),
            run_status="error",
            run_id=metadata_logger_run_id, 
            run_config=config,
            run_log=run_log.getvalue(),
            db_table=metadata_logger_table
        )
    print(run_log.getvalue())

def pipeline()->bool:
    run_log = StringIO()
    logging.basicConfig(stream=run_log,format="[%(levelname)s][%(asctime)s][%(filename)s]: %(message)s") # format: https://docs.python.org/3/library/logging.html#logging.LogRecord
    logger = logging.getLogger(__file__)
    logger.setLevel(logging.INFO)
    # get yaml config 
    with open("trading_price/config.yaml") as stream:
        config = yaml.safe_load(stream)

    for stock in config["stocks"]:
        pipeline_per_stock(config=stock['stock'], logger=logger, run_log=run_log)
    
    return True  

if __name__ == "__main__": 
    
    # run the pipeline
    if pipeline(): 
        print("success")