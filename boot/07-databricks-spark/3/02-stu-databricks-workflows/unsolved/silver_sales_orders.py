# Databricks notebook source
# MAGIC %md
# MAGIC ## Run set up

# COMMAND ----------

# MAGIC %run "./setup_sales_orders"

# COMMAND ----------

dbutils.widgets.text("bronze_sales_orders_table_path", bronze_sales_orders_table_path)
dbutils.widgets.text("bronze_sales_orders_table_name", bronze_sales_orders_table_name)
dbutils.widgets.text("silver_sales_orders_table_path", silver_sales_orders_table_path)
dbutils.widgets.text("silver_sales_orders_table_name", silver_sales_orders_table_name)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create table 

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE TABLE ${silver_sales_orders_table_name}
# MAGIC USING DELTA
# MAGIC LOCATION "${silver_sales_orders_table_path}"
# MAGIC AS
# MAGIC WITH bronze_table as (
# MAGIC     SELECT
# MAGIC       customer_id,
# MAGIC       customer_name, 
# MAGIC       from_unixtime(order_datetime) as order_datetime, 
# MAGIC       order_number, 
# MAGIC       number_of_line_items, 
# MAGIC       posexplode_outer(ordered_products) 
# MAGIC     FROM 
# MAGIC       ${bronze_sales_orders_table_name}
# MAGIC )
# MAGIC 
# MAGIC SELECT
# MAGIC     customer_id,
# MAGIC     customer_name, 
# MAGIC     order_datetime, 
# MAGIC     order_number, 
# MAGIC     pos + 1 AS line_number, 
# MAGIC     col.id as product_id, 
# MAGIC     col.curr AS currency_code, 
# MAGIC     col.price AS price, 
# MAGIC     col.qty AS quantity, 
# MAGIC     col.price * col.qty AS order_amount, 
# MAGIC     col.unit
# MAGIC FROM
# MAGIC     bronze_table
