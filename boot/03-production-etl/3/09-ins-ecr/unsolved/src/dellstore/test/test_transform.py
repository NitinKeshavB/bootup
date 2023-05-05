from dellstore.pipeline.extract_load_pipeline import ExtractLoad
from database.postgres import PostgresDB
import pandas as pd 
import os 
import jinja2 as j2 
from dellstore.etl.transform import Transform

def test_serving_top_customers():
    # -- assemble -- 
    actual_source_staging_orders = "staging_orders"
    mock_source_staging_orders = f"mock_{actual_source_staging_orders}"
    actual_source_staging_customers = "staging_customers"
    mock_source_staging_customers = f"mock_{actual_source_staging_customers}"
    actual_target_table="serving_top_customers"
    mock_target_table=f"mock_{actual_target_table}"
    path_model_transform = "dellstore/models/transform"
    engine = PostgresDB.create_pg_engine(db_target="target")
    
    # create mock staging_orders
    df_mock_data_staging_orders = pd.DataFrame({
        "orderid": [1, 2, 3, 4], 
        "customerid": [1, 2, 3, 3],
        "netamount": [10.0, 20.0, 30.0, 20.0]
    })
    df_mock_data_staging_orders.to_sql(name=mock_source_staging_orders, con=engine, if_exists="replace", index=False)

    # create mock staging_customers
    df_mock_data_staging_customers = pd.DataFrame({
        "customerid": [1, 2, 3],
        "firstname": ["Jack", "Jill", "Bob"],
        "lastname": ["Smith", "Smith", "Smith"]
    })
    df_mock_data_staging_customers.to_sql(name=mock_source_staging_customers, con=engine, if_exists="replace", index=False)

    # create expected result df 
    df_expected_output = pd.DataFrame({
        "firstname": ["Bob", "Jill", "Jack"], 
        "lastname": ["Smith", "Smith", "Smith"],
        "sales": [50.0, 20.0, 10.0]
    })

    # get transform sql file 
    with open(f"{path_model_transform}/{actual_target_table}.sql") as f: 
        raw_sql = f.read()
    
    raw_sql = raw_sql.replace(actual_source_staging_orders, mock_source_staging_orders)
    raw_sql = raw_sql.replace(actual_source_staging_customers, mock_source_staging_customers)
    # write mock transform file 
    with open(f"{path_model_transform}/{mock_target_table}.sql", mode="w") as f:  
        f.write(raw_sql)

    # -- act -- 
    node_serving_top_customers = Transform(mock_target_table, engine=engine, models_path=path_model_transform)
    node_serving_top_customers.run()
    df_output = pd.read_sql(sql=mock_target_table, con=engine)

    # clean up first 
    engine.execute(f"drop table {mock_source_staging_orders}")
    engine.execute(f"drop table {mock_source_staging_customers}")
    engine.execute(f"drop table {mock_target_table}")
    os.remove(f"{path_model_transform}/{mock_target_table}.sql")

    # -- assert -- 
    pd.testing.assert_frame_equal(left=df_output, right=df_expected_output, check_exact=True)