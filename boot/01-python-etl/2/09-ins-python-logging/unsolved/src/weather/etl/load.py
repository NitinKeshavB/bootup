import os 
import pandas as pd 

class Load():
    
    @staticmethod
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