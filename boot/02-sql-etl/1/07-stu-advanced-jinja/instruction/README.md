# Advanced jinja 

## Task 

For `serving_trades.sql`, dynamically generate flag columns based on the exchange_name data. 

1. Retrieve `exchange_name` values from `staging_exchange_codes` table and store the result in a list. 
2. Loop over each item in the list and create a new column using jinja. Perform string replace for any characters that is not compatible with [Postgresql column name rules](https://www.postgresql.org/docs/7.0/syntax525.htm). 
3. Run the SQL query and validate the table result. 


