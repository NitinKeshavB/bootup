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

# MAGIC %sql 
# MAGIC CREATE OR REPLACE TABLE ${silver_product_table_name}
# MAGIC USING DELTA
# MAGIC LOCATION "${silver_product_table_path}"
# MAGIC AS
# MAGIC SELECT
# MAGIC     product_id, 
# MAGIC     product_category,
# MAGIC     product_name,
# MAGIC     product_unit, 
# MAGIC     CAST(sales_price AS DECIMAL(10,2)) as sales_price
# MAGIC FROM
# MAGIC     ${bronze_product_table_name}
