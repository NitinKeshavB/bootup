# Databricks notebook source
# MAGIC %run ./_common

# COMMAND ----------

@DBAcademyHelper.monkey_patch
def create_table(self, table_name, location):
    import time
    start = int(time.time())
    
    print(f"Creating the table \"{table_name}\"", end="...")
    spark.sql(f"CREATE OR REPLACE TABLE {table_name} SHALLOW CLONE delta.`{DA.paths.datasets}/{location}`")
        
    print(f"({int(time.time())-start} seconds)")

# COMMAND ----------

DA = DBAcademyHelper(**helper_arguments) # Create the DA object
DA.reset_environment()                   # Reset by removing databases and files from other lessons
DA.init(install_datasets=True,           # Initialize, install and validate the datasets
        create_db=True)                  # Continue initialization, create the user-db
print()
DA.create_table("events", "ecommerce/events/events.delta", )
DA.create_table("sales", "ecommerce/sales/sales.delta", )
DA.create_table("users", "ecommerce/users/users.delta")
DA.create_table("products", "products/products.delta", )

DA.conclude_setup()                      # Conclude setup by advertising environmental changes

