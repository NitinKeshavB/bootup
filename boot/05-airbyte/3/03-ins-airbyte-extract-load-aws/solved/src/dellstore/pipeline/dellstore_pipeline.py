from airbyte.airbyte import AirbyteConnection
from graphlib import TopologicalSorter
import os 
from database.postgres import PostgresDB
from dellstore.etl.transform import Transform
import yaml 
from io import StringIO
import logging
from utility.metadata_logging import MetadataLogging
import datetime as dt 


def run_pipeline():
    # set up logging 
    run_log = StringIO()
    logging.basicConfig(stream=run_log,level=logging.INFO, format="[%(levelname)s][%(asctime)s]: %(message)s")

    # set up metadata logger 
    metadata_logger = MetadataLogging(db_target="target")

    # configure pipeline 
    with open("dellstore/config.yaml") as stream:
        config = yaml.safe_load(stream)
    path_transform_model = config["transform"]["model_path"]
    airbyte_host = os.environ.get("airbyte_host")
    airbyte_connection_id = os.environ.get("airbyte_connection_id")
    target_engine = PostgresDB.create_pg_engine(db_target="target")
    
    metadata_log_table = config["meta"]["log_table"]
    metadata_log_run_id = metadata_logger.get_latest_run_id(db_table=metadata_log_table)
    metadata_logger.log(
        run_timestamp=dt.datetime.now(),
        run_status="started",
        run_id=metadata_log_run_id, 
        run_config=config,
        db_table=metadata_log_table
    )

    try: 
        logging.info("Creating extract and load nodes")
        # build dag 
        dag = TopologicalSorter()

        # extract load node 
        airbyte_connection = AirbyteConnection(host=airbyte_host, connection_id=airbyte_connection_id)
        dag.add(airbyte_connection)
        
        # transform nodes  
        logging.info("Creating transform nodes")
        node_staging_orders = Transform("staging_orders", engine=target_engine, models_path=path_transform_model)
        node_staging_customers = Transform("staging_customers", engine=target_engine, models_path=path_transform_model)
        node_serving_top_customers = Transform("serving_top_customers", engine=target_engine, models_path=path_transform_model)
        dag.add(node_staging_orders, airbyte_connection)
        dag.add(node_staging_customers, airbyte_connection)
        dag.add(node_serving_top_customers, node_staging_orders, node_staging_customers, airbyte_connection)
        
        # run dag 
        logging.info("Executing DAG")
        dag_rendered = tuple(dag.static_order())
        for node in dag_rendered: 
            node.run()
        
        logging.info("Pipeline run successful")
        metadata_logger.log(
            run_timestamp=dt.datetime.now(),
            run_status="completed",
            run_id=metadata_log_run_id, 
            run_config=config,
            run_log=run_log.getvalue(),
            db_table=metadata_log_table
        )
    except Exception as e: 
        logging.exception(e)
        metadata_logger.log(
            run_timestamp=dt.datetime.now(),
            run_status="error",
            run_id=metadata_log_run_id, 
            run_config=config,
            run_log=run_log.getvalue(),
            db_table=metadata_log_table
        )
    print(run_log.getvalue())

if __name__ == "__main__":
    run_pipeline()
