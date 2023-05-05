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

bronze_sales_orders_df = spark.sql("""
SELECT * FROM vw_raw_sales_orders
""")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from vw_raw_sales_orders

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Run expectations 
# MAGIC 
# MAGIC View a list of all expectations here: https://greatexpectations.io/expectations/

# COMMAND ----------

from great_expectations.dataset import SparkDFDataset
ge_bronze_sales_orders_df = SparkDFDataset(bronze_sales_orders_df)

# COMMAND ----------

expectation1 = ge_bronze_sales_orders_df.expect_column_values_to_not_be_null("customer_id")
if not expectation1["success"]: 
    raise Exception(expectation1)

# COMMAND ----------

expectation2 = ge_bronze_sales_orders_df.expect_column_values_to_not_be_null("order_number")
if not expectation2["success"]: 
    raise Exception(expectation2)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Write table

# COMMAND ----------

bronze_sales_orders_df.write.option("path", bronze_sales_orders_table_path).format("delta").mode("overwrite").saveAsTable(bronze_sales_orders_table_name)
