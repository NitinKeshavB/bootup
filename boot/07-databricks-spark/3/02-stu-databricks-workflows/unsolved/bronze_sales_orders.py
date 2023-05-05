# Databricks notebook source
# MAGIC %md
# MAGIC ## Run setup

# COMMAND ----------

# MAGIC %run "./setup_sales_orders"

# COMMAND ----------

dbutils.widgets.text("bronze_sales_orders_table_path", bronze_sales_orders_table_path)
dbutils.widgets.text("bronze_sales_orders_table_name", bronze_sales_orders_table_name)
dbutils.widgets.text("silver_sales_orders_table_path", silver_sales_orders_table_path)
dbutils.widgets.text("silver_sales_orders_table_name", silver_sales_orders_table_name)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Read file from S3 into temporary view

# COMMAND ----------

raw_sales_orders_df = spark.read.format("json").load("dbfs:/databricks-datasets/retail-org/sales_orders/")
raw_sales_orders_df.createOrReplaceTempView("vw_raw_sales_orders")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create table 

# COMMAND ----------

# MAGIC %sql 
# MAGIC CREATE OR REPLACE TABLE ${bronze_sales_orders_table_name} 
# MAGIC USING DELTA LOCATION "${bronze_sales_orders_table_path}"
# MAGIC AS SELECT * FROM vw_raw_sales_orders
