--STEP 0
-- set up schema, table and 2 rows of data
CREATE SCHEMA datastore;

CREATE TABLE datastore.data_tbl
(
    id bigint,
    val character varying,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS datastore.data_tbl
    OWNER to postgres;


INSERT INTO postgres.datastore.data_tbl
VALUES (1, 'a'), (2, 'b');

select * from  postgres.datastore.data_tbl;

-- STEP 1
-- create read only user
CREATE USER airbyte PASSWORD '@irbyte';
GRANT USAGE ON SCHEMA datastore TO airbyte;

GRANT SELECT ON ALL TABLES IN SCHEMA datastore TO airbyte;
ALTER DEFAULT PRIVILEGES IN SCHEMA datastore GRANT SELECT ON TABLES TO airbyte;
-- role for cdc
GRANT rds_replication TO airbyte;

-- STEP 2
/*
https://docs.airbyte.com/integrations/sources/postgres#configuring-postgres-connector-with-change-data-capture-cdc
To enable logical replication on AWS Postgres RDS or Aurora:
1. Go to the Configuration tab for your DB cluster.
2. Find your cluster parameter group. Either edit the parameters for this group or create a copy of this parameter group to edit. If you create a copy, remember to change your cluster's parameter group before REBOOTING.
3. Within the parameter group page, search for rds.logical_replication. Select this row and click Edit parameters. Set this value to 1.
4. Apply the change immediately
*/

-- STEP 3
-- create replication slot
SELECT pg_create_logical_replication_slot('airbyte_slot', 'pgoutput');

-- STEP 4
-- create replication identities and publications for tables
ALTER TABLE postgres.datastore.data_tbl REPLICA IDENTITY DEFAULT;
CREATE PUBLICATION airbyte_publication FOR TABLE postgres.datastore.data_tbl;

-- STEP 5
/*
create source in airbyte
tick SSL
use Logical Replication CDC
*/
