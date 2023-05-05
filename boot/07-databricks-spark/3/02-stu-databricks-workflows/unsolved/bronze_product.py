# Databricks notebook source
# MAGIC %md
# MAGIC ## Run setup

# COMMAND ----------

# MAGIC %run "./setup_product"

# COMMAND ----------

dbutils.widgets.text("bronze_product_table_path", bronze_product_table_path)
dbutils.widgets.text("bronze_product_table_name", bronze_product_table_name)
dbutils.widgets.text("silver_product_table_path", silver_product_table_path)
dbutils.widgets.text("silver_product_table_name", silver_product_table_name)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Read file from S3 into temporary view

# COMMAND ----------

raw_products_df = spark.read.format("csv").option("delimiter", ";").option("header", True).load("dbfs:/databricks-datasets/retail-org/products/")
raw_products_df.createOrReplaceTempView("vw_raw_product")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create table 

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ${bronze_product_table_name}
# MAGIC USING DELTA LOCATION "${bronze_product_table_path}"
# MAGIC AS SELECT * FROM vw_raw_product
