# Solved Exercise


# Create a KSQL table with the primary key set to city

1. Create the table with PRIMARY KEY set to city
   1. Note: for tables we use `PRIMARY KEY` but in a stream we use `KEY`. Can anyone guess why?
   2. https://docs.ksqldb.io/en/latest/developer-guide/ksqldb-reference/create-table/
2. Print out all the values in that table using KSQL CLI, what do you see? Use `EMIT CHANGES` to make this a push query.
   3. You should only see one row per city.


