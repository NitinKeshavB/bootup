# Instruction

## Task 

### Create RDS - Postgres

1. Go to AWS console 
2. Search for RDS
3. Select "Create database" 
4. In the "Create database" screen: 
    1. Database creation method: "Standard create"
    2. Engine option: "PostreSQL" 
    3. Templates: "Free tier" 
    4. Settings > DB instance identifier: "<provide_database_name>"
    5. Settings > Credential settings > master password: "<provide_password>"
    6. Instance configuration: db.t3.micro 
    7. Storage > Storage autoscaling > Enable storage autoscaling: No (untick)
    8. Connectivity > Public access: "Yes" 
    9. Select "Create database"

### Allow inbound traffic 

1. Once the database has been created, go to "Connectivity and security"
2. Select the default VPC security group 
3. Select "Edit inbound rules" 
4. Select "Add rule": 
    1. Select "All TCP" 
    2. Select "Anywhere-IPv4" 
5. Select "Save rules" 

### Restore dvd rental database 

1. Go to PgAdmin4
2. Right click on "Servers" > Register > Server: 
    - General > Name: `<choose_a_name>`
    - Connection > Host name: `<provide_host_name_from_rds>`
    - Connection > Port: `5432`
    - Connection > Password: `<provide_password>`
    - Select "Save" 
3. Create a new database 
4. Tools > Restore: 
    - Format: `Directory`
    - Filename: `<select_filepath>` 
    - Select "Restore" 

### Run a select query 

Run a select query on one of the tables to verify restore was successful.

