# Instruction 

## Task 

Perform an incremental sync between `dvd_rental` and `dw`

### Create a new destination 

1. Go to destination and select "+ New destination" 
2. For "Destination type", select "Postgres": 
    - Name: `dw-002`
    - Host: `host.docker.internal` 
    - Port: `5432`
    - Database name: `dvd_rental` 
    - Schemas: `public` 
    - Username: `postgres`
    - Password: `postgres` 
3. Select "Set up destination" 


### Create a new connection 

1. Same as before
2. Change the sync mode for the following tables to either `Incremental | Deduped + history` or `Incremental | Append`: 
    - actor 
    - adddress 
    - customer 
    - film 
    - inventory 
    - payment 
    - rental 

Q: Why do you think we've selected incremental extracts for these tables? 

### Manually trigger the run 

**First run**

1. Select "Sync now" 
2. Take note of the rows emitted, and rows committed 
3. Pay attention to the logs: 
    - `original cursor value null` 

**Second run**

1. Select "Sync now" 
2. Take note of the rows emitted, and rows committed 
3. Pay attention to the logs: 
    - `original cursor value` 
    - `new cursor value` 

**Third run**

1. Insert a new record to the `customer` table 
2. Select "Sync now" 
3. Take note of the rows emitted, and rows committed 
4. Pay attention to the logs: 
    - `original cursor value` 
    - `new cursor value` 
