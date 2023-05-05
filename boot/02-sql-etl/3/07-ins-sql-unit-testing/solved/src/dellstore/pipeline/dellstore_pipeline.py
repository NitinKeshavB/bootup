from dellstore.pipeline.extract_load_pipeline import ExtractLoad
from graphlib import TopologicalSorter
import os 
from database.postgres import PostgresDB
from dellstore.etl.transform import Transform

def run_pipeline():

    # configure pipeline 
    path_extract_model = "dellstore/models/extract"
    path_transform_model = "dellstore/models/transform"
    path_extract_log = "dellstore/log/extract_log"
    source_engine = PostgresDB.create_pg_engine(db_target="source")
    target_engine = PostgresDB.create_pg_engine(db_target="target")
    
    # build dag 
    dag = TopologicalSorter()
    nodes_extract_load = []
    
    # extract_load nodes 
    for file in os.listdir(path_extract_model):
        node_extract_load = ExtractLoad(source_engine=source_engine, target_engine=target_engine,table_name=file.replace(".sql", ""), path=path_extract_model, path_extract_log=path_extract_log)
        dag.add(node_extract_load)
        nodes_extract_load.append(node_extract_load)
    
    # transform nodes  
    node_staging_orders = Transform("staging_orders", engine=target_engine, models_path=path_transform_model)
    node_staging_customers = Transform("staging_customers", engine=target_engine, models_path=path_transform_model)
    node_serving_top_customers = Transform("serving_top_customers", engine=target_engine, models_path=path_transform_model)
    dag.add(node_staging_orders, *nodes_extract_load)
    dag.add(node_staging_customers, *nodes_extract_load)
    dag.add(node_serving_top_customers, node_staging_orders, node_staging_customers, *nodes_extract_load)
    
    # run dag 
    dag_rendered = tuple(dag.static_order())
    for node in dag_rendered: 
        node.run()


if __name__ == "__main__":
    run_pipeline()