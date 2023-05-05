# Databricks notebook source
# MAGIC %run ./_common

# COMMAND ----------

@TestHelper.monkey_patch
def validate_1_1(self, schema):
    suite = DA.tests.new("5.1b-1.1")

    suite.test_equals(actual_value=type(schema), expected_value=StructType, description="Schema is of type StructType", hint="Found [[ACTUAL_VALUE]]")
    
    suite.test_length(schema.fieldNames(), 12, description="Schema contians 12 field", hint="Found [[LEN_ACTUAL_VALUE]]: [[ACTUAL_VALUE]]")
    
    suite.test_struct_field(schema, "device", "StringType", None)
    suite.test_struct_field(schema, "ecommerce", "StructType", None)
    suite.test_struct_field(schema, "event_name", "StringType", None)
    suite.test_struct_field(schema, "event_previous_timestamp", "LongType", None)
    suite.test_struct_field(schema, "event_timestamp", "LongType", None)
    suite.test_struct_field(schema, "geo", "StructType", None)
    suite.test_struct_field(schema, "items", "ArrayType", None)
    suite.test_struct_field(schema, "traffic_source", "StringType", None)
    suite.test_struct_field(schema, "user_first_touch_timestamp", "LongType", None)
    suite.test_struct_field(schema, "user_id", "StringType", None)
    suite.test_struct_field(schema, "hour", "IntegerType", None)
    suite.test_struct_field(schema, "createdAt", "TimestampType", None)
    
    suite.display_results()
    assert suite.passed, "One or more tests failed."


# COMMAND ----------

@TestHelper.monkey_patch
def validate_2_1(self, schema):
    suite = DA.tests.new("5.1b-2.1")

    suite.test_equals(actual_value=type(schema), expected_value=StructType, description="Schema is of type StructType", hint="Found [[ACTUAL_VALUE]]")
    
    suite.test_length(schema.fieldNames(), 3, description="Schema contians three field", hint="Found [[LEN_ACTUAL_VALUE]]: [[ACTUAL_VALUE]]")
    
    suite.test_struct_field(schema, "traffic_source", "StringType", None)
    suite.test_struct_field(schema, "active_users", "LongType", None)
    suite.test_struct_field(schema, "hour", "IntegerType", None)
    
    suite.display_results()
    assert suite.passed, "One or more tests failed."


# COMMAND ----------

@TestHelper.monkey_patch
def validate_4_1(self):
    suite = DA.tests.new("5.1b-4.1")

    suite.test_length(spark.streams.active, 0, description="All queries have stopped streaming")
    
    suite.display_results()
    assert suite.passed, "One or more tests failed."

# COMMAND ----------

DA = DBAcademyHelper(**helper_arguments) # Create the DA object
DA.reset_environment()                   # Reset by removing databases and files from other lessons
DA.init(install_datasets=True,           # Initialize, install and validate the datasets
        create_db=True)                  # Continue initialization, create the user-db

DA.paths.sales = f"{DA.paths.datasets}/ecommerce/sales/sales.delta"
DA.paths.users = f"{DA.paths.datasets}/ecommerce/users/users.delta"
DA.paths.events = f"{DA.paths.datasets}/ecommerce/events/events.delta"
DA.paths.products = f"{DA.paths.datasets}/products/products.delta"

DA.conclude_setup()                      # Conclude setup by advertising environmental changes

