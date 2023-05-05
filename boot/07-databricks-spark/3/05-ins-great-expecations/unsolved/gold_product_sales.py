# Databricks notebook source
# MAGIC %md
# MAGIC ## Run set up

# COMMAND ----------

# MAGIC %run "./setup_product"

# COMMAND ----------

# MAGIC %run "./setup_sales_orders"

# COMMAND ----------

gold_product_sales_table_path = f"dbfs:/mnt/dbacedemy-users/{username}/gold/product_sales"
gold_product_sales_table_name = f"gold_product_sales"

# COMMAND ----------

dbutils.widgets.text("silver_product_table_name", silver_product_table_name)
dbutils.widgets.text("silver_sales_orders_table_name", silver_sales_orders_table_name)
dbutils.widgets.text("gold_product_sales_table_path", gold_product_sales_table_path)
dbutils.widgets.text("gold_product_sales_table_name", gold_product_sales_table_name)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create table 

# COMMAND ----------

# MAGIC %sql 
# MAGIC CREATE OR REPLACE TABLE ${gold_product_sales_table_name}
# MAGIC USING DELTA
# MAGIC LOCATION "${gold_product_sales_table_path}"
# MAGIC AS
# MAGIC SELECT
# MAGIC     sales.*,
# MAGIC     product.product_category,
# MAGIC     product.product_name,
# MAGIC     product.sales_price
# MAGIC FROM
# MAGIC     ${silver_sales_orders_table_name} AS sales LEFT JOIN 
# MAGIC     ${silver_product_table_name} AS product ON sales.product_id = product.product_id
