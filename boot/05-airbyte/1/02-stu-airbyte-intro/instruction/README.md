# Instruction 

## Task 

### Deploy airbyte locally

1. Clone the airbyte repo locally from `https://github.com/airbytehq/airbyte.git` 

    ```
    git clone https://github.com/airbytehq/airbyte.git
    ```

2. Make sure you have Docker Desktop running first

3. Run the docker compose file 

    ```
    cd airbyte 
    docker-compose up
    ```

### Create a new source 

1. Go to sources and select "+ New source" 
2. For "Source type", select "Postgres": 
    - Name: `dvd_rental`
    - Host: `host.docker.internal` 
    - Port: `5432`
    - Database name: `dvd_rental` 
    - Schemas: `public` 
    - Username: `postgres`
    - Password: `postgres` 
3. Select "Set up source" 

### Create a new destination 

1. Go to destination and select "+ New destination" 
2. For "Destination type", select "Postgres": 
    - Name: `dw-001`
    - Host: `host.docker.internal` 
    - Port: `5432`
    - Database name: `dvd_rental` 
    - Schemas: `public` 
    - Username: `postgres`
    - Password: `postgres` 
3. Select "Set up destination" 

### Create a new connection (replication job)

1. Go to Connections and select "+ New connection" 
2. For Select an existing source, select "dvd_rental" and "Use existing source" 
3. For Select an existing destination, select "dw-001" and "Use existing destination" 
4. For the new connection: 
    - Connection name: `leave_as_default` 
    - Replication frequency: `Every 5 minutes` 
    - Destination namespace: `Mirror source structure` 
    - Activate streams you want to sync: `leave_as_default` 
5. Select "Set up connection" 

Note: We are currently performing `Source: Full refresh | Destination: Overwrite` for all tables. 

### Manually trigger the run 

1. Select "Sync now" 
2. Take note of the rows emitted, and rows committed 
3. Take notice of the `_staging` tables with JSON records before it becomes flattened in the final table 
4. Take notice of the data types from source vs target
