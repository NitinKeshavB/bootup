import pandas as pd
import jinja2 as j2 
import logging 
import os 
import datetime as dt 
from utility.incremental_logging import IncrementalLogging

class Extract():

    @staticmethod
    def is_incremental(table:str, path:str)->bool:
        # read sql contents into a variable 
        with open(f"{path}/{table}.sql") as f: 
            raw_sql = f.read()
        try: 
            config = j2.Template(raw_sql).make_module().config 
            return config["extract_type"].lower() == "incremental"
        except:
            return False
    
    @staticmethod
    def extract_from_database(table_name, engine, path="extract_queries", path_extract_log="extract_log")->pd.DataFrame:
        """
        Builds models with a matching file name in the models_path folder. 
        - `table_name`: the name of the table (without .sql)
        - `path`: the path to the extract queries directory containing the sql files. defaults to `extract_queries`
        """
        logging.basicConfig(level=logging.INFO, format="[%(levelname)s][%(asctime)s]: %(message)s")
        
        logging.info(f"Extracting table: {table_name}")
        if f"{table_name}.sql" in os.listdir(path):
            # read sql contents into a variable 
            with open(f"{path}/{table_name}.sql") as f: 
                raw_sql = f.read()
            # get config 
            config = j2.Template(raw_sql).make_module().config 
            if Extract.is_incremental(table=table_name, path=path): 
                incremental_logger = IncrementalLogging(db_target="target")
                current_max_incremental_value = incremental_logger.get_latest_incremental_value(db_table=f"incremental_log_{table_name}")
                if current_max_incremental_value is not None:
                    # perform incremental extract 
                    parsed_sql = j2.Template(raw_sql).render(source_table = table_name, engine=engine, is_incremental=True, incremental_value=current_max_incremental_value)
                    # execute incremental extract
                    df = pd.read_sql(sql=parsed_sql, con=engine)
                    # update max incremental value 
                    if len(df) > 0: 
                        max_incremental_value = df[config["incremental_column"]].max()
                    else: 
                        max_incremental_value = current_max_incremental_value
                    incremental_logger.log(run_timestamp=dt.datetime.now(), incremental_value=max_incremental_value, db_table=f"incremental_log_{table_name}")
                    logging.info(f"Successfully extracted table: {table_name}, rows extracted: {len(df)}")
                    return df 
                else: 
                    # parse sql using jinja 
                    parsed_sql = j2.Template(raw_sql).render(source_table = table_name, engine=engine)
                    # perform full extract 
                    df = pd.read_sql(sql=parsed_sql, con=engine)
                    # store latest incremental value 
                    max_incremental_value = df[config["incremental_column"]].max()
                    incremental_logger.log(run_timestamp=dt.datetime.now(), incremental_value=max_incremental_value, db_table=f"incremental_log_{table_name}")
                    logging.info(f"Successfully extracted table: {table_name}, rows extracted: {len(df)}")
                    return df 
            else: 
                # parse sql using jinja 
                parsed_sql = j2.Template(raw_sql).render(source_table = table_name, engine=engine)
                # perform full extract 
                df = pd.read_sql(sql=parsed_sql, con=engine)
                logging.info(f"Successfully extracted table: {table_name}, rows extracted: {len(df)}")
                return df 
        else: 
            logging.error(f"Could not find table: {table_name}")
            
