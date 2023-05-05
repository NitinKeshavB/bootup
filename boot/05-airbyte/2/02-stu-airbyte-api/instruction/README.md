# Instruction 

## Task 

1. Create a new connection in Airbyte to sync between S3 files to Postgres. Note: Use the CSV files provided in `/dataset`. 
2. Go to https://airbyte-public-api-docs.s3.us-east-2.amazonaws.com/rapidoc-api-docs.html to see airbyte api docs 
3. Create a function that: 
    - Triggers the connection sync 
    - Continuously check the status of the connection sync 
    - Returns `True` when the sync is complete  
4. Sync only `2015`, `2016`, `2017` in the first run by uploading only those 3 files to S3 
5. Subsequently sync `2018`, `2019` by uploading those additional 2 files to S3 
6. Verify that all files have been synced to postgres 
