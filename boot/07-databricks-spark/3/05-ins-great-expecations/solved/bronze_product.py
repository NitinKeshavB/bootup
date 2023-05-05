# Databricks notebook source
# MAGIC %md
# MAGIC ## Run setup
# MAGIC 
# MAGIC - Install great_expectations using `%pip install great-expectations`, or 
# MAGIC - [Install on cluster (recommended)](https://docs.databricks.com/libraries/cluster-libraries.html) 

# COMMAND ----------

# %pip install great-expectations

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
# MAGIC ## View data (development only)

# COMMAND ----------

# %sql
# SELECT * FROM vw_raw_product

# COMMAND ----------

# %sql
# SELECT distinct(product_category) FROM vw_raw_product

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create table 

# COMMAND ----------

bronze_product_df = spark.sql("""
SELECT * FROM vw_raw_product
""")

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Run expectations 
# MAGIC 
# MAGIC View a list of all expectations here: https://greatexpectations.io/expectations/

# COMMAND ----------

from great_expectations.dataset import SparkDFDataset

# COMMAND ----------

ge_bronze_product_df = SparkDFDataset(bronze_product_df)

# COMMAND ----------

expectation1 = ge_bronze_product_df.expect_column_values_to_not_be_null("product_id")
if not expectation1["success"]: 
    raise Exception(expectation1)

# COMMAND ----------

expectation2 = ge_bronze_product_df.expect_column_distinct_values_to_be_in_set("product_category", [
    "Ankyo",
    "Apson",
    "Conan",
    "Elpine",
    "Karsair",
    "Mannheiser",
    "Mogitech",
    "Mowepro",
    "Olitscreens",
    "Opple",
    "Ramsung",
    "Reagate",
    "Rony",
    "Sioneer",
    "Zamaha" 
])
if not expectation2["success"]: 
    raise Exception(expectation2)


# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Write table

# COMMAND ----------

bronze_product_df.write.option("path", bronze_product_table_path).format("delta").mode("overwrite").saveAsTable(bronze_product_table_name)
