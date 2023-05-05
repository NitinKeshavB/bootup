# Incremental extracts 

## Task 

1. Implement incremental extracts on tables that have > 1000 rows. 

2. For the rest of the tables, modify the existing config in the SQL files to perform full extracts. 

3. Test your ELT pipeline to check if data is written to the target database. 

4. Try running your ELT for a second time, what do you notice happens in your target database for the tables that are populated from incremental extracts? 

## Tips:
- We have provided you with some helper queries in `helper_queries` which will come in handy. 
    - `get_table_row_counts.sql`: this is a useful query we can run against the source database to get the row counts of all tables so that we know which tables we need to enable incremental extracts on. 
