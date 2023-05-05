# Metadata logging 

## Task 

Implement logging for your trading price project. 

Steps: 

1. Set up `logger` and the StringIO() buffer `log_stream` on the on `pipeline()` level
2. Pass `logger` and the `log_stream` into `pipeline_per_stock()`
3. At the start of `pipeline_per_stock()`, reset StreamIO to start from a clean slate by running: `log_stream.seek(0)` and `log_stream.truncate(0)`. 
4. Create an object of the `MetadataLogging()` class e.g. `metadata_logger = MetadataLogging()` 
5. Get the target logging table name by using the `target_table_name` specified in YAML. 
6. Get the latest `run_id` from the logging table. A brand new table without any logs will just return `1` as the latest id. 
7. Obtain the `log_stream` values by running `log_stream.getvalue()`.  
8. Write the starting log by running `metadata_logger.log(run_status="started")`. 
9. Write the completion log by running `metadata_logger.log(run_status="completed")`. 
10. If there is an error, first catch the error by running `logger.exception(e)`, then write the error log by running `metadata_logger.log(run_status="error")`. 
11. Run the pipeline and check postgresql to see if the logs have been written. 