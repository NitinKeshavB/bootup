# Databricks notebook source
# global vars 
username = dbutils.notebook.entry_point.getDbutils().notebook().getContext().userName().get()
database_name = username.split("@")[0].replace("-", "_")
# bronze vars 
bronze_sales_orders_table_path = f"dbfs:/mnt/dbacademy-users/{username}/bronze/sales_orders"
bronze_sales_orders_table_name = f"bronze_sales_orders"
# silver vars  
silver_sales_orders_table_path = f"dbfs:/mnt/dbacademy-users/{username}/silver/sales_orders"
silver_sales_orders_table_name = f"silver_sales_orders"

# COMMAND ----------

spark.sql(f"""
CREATE DATABASE IF NOT EXISTS {database_name} 
""")
spark.sql(f"""
USE DATABASE {database_name} 
""")
