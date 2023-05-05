# Dynamic ELT 

## Task 

Implement dynamic upsert loads: 

1. Get the table name from the SQL file 
2. Set a new config in the SQL file for the primary key columns 
3. Retrieve the key_columns config from the SQL file 
4. Retrieve the column and data types from the pandas dataframe 
5. Map pandas dataframe data types to the target database's data types 
6. Test your code to validate that it works. Make sure to run it at least 2 times. The second run will validate that the upsert worked and you are not overwriting the target table. 

## Tips
- We have provided you with some helper queries in `helper_queries` which will come in handy. 
    - `drop_schema_cascade.sql`: this is useful for recreating your target tables if you had already created them once using `df.to_sql()`. This step is necessary because the target tables were created initially with pandas's inferred schema. However, since we are mapping our own schema and data types, we should therefore recreate those tables with our mapped schema. 


