# Databricks notebook source
# MAGIC %md
# MAGIC ## Run set up

# COMMAND ----------

# MAGIC %run "./setup_product"

# COMMAND ----------

dbutils.widgets.text("bronze_product_table_path", bronze_product_table_path)
dbutils.widgets.text("bronze_product_table_name", bronze_product_table_name)
dbutils.widgets.text("silver_product_table_path", silver_product_table_path)
dbutils.widgets.text("silver_product_table_name", silver_product_table_name)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create table 

# COMMAND ----------

silver_product_df = spark.sql(f"""
SELECT
    product_id, 
    product_category,
    product_name,
    product_unit, 
    CAST(sales_price AS DECIMAL(10,2)) as sales_price
FROM
    {bronze_product_table_name}
""")

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Run expectations 
# MAGIC 
# MAGIC View a list of all expectations here: https://greatexpectations.io/expectations/

# COMMAND ----------

from great_expectations.dataset import SparkDFDataset
ge_silver_product_df = SparkDFDataset(silver_product_df)

# COMMAND ----------

expectation1 = ge_silver_product_df.expect_column_values_to_not_be_null("product_id")
if not expectation1["success"]: 
    raise Exception(expectation1)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## Write table

# COMMAND ----------

silver_product_df.write.option("path", silver_product_table_path).format("delta").mode("overwrite").saveAsTable(silver_product_table_name)
