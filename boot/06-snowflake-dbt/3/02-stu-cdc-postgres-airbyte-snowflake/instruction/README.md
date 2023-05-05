# Instruction

## Task

Now it's your turn to implement a CDC replication.

You could use the table you created in previous weeks as long as it has a primary key.

1. [Set up](https://docs.airbyte.com/integrations/sources/postgres#configuring-postgres-connector-with-change-data-capture-cdc) Postgres
   1. Create table, insert data
   2. Create read only user, grant role
   3. Update parameter group and restart database
   4. Create replication slot
   5. Create publication
2. Create Postgres Source in Airbyte
3. [Set up](https://docs.airbyte.com/integrations/destinations/snowflake) Snowflake
4. Create Snowflake Destination in Airbyte
5. Insert and update data to observe CDC
