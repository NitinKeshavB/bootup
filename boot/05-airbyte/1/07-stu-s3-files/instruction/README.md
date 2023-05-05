# Instruction 

## Concept 

Ingesting files into PostgreSQL. 

## Task 

### Upload files to S3 

1. Create a new S3 bucket e.g. `airbyte-demo-001`
2. Upload `airline.csv` to an S3 bucket in the folder `/happiness`. 

### Create IAM user for Airbyte 

1. Go to IAM 
2. Create a new user e.g. `airbyte` 
3. Select AWS credential type: `Access key` 
4. Set Permissions > attach existing policies directly > `AmazonS3FullAccess`
5. Next: Tags  
6. Next: Review
7. Create user 

### Create Airbyte Source for S3 

- Name: `happiness-demo`
- Output stream name: `happiness`
- Pattern of files to replicate: `happiness/*.csv`
- Bucket: `airbyte-demo-001`
- AWS access key ID: `<key id here>`
- AWS secret access key: `<key here>`
- Select "Set up source"  

### Create Airbyte Connection for S3 

For sync mode, select `Incremental | Append`: 
- Cursor field: `_ab_source_file_last_modified` 

