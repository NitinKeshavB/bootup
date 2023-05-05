# Instruction

## Hosting adventureworks on AWS RDS 

1. Create or replace your existing `t2.micro` RDS instance. 

2. Restore `adventureworks` database to the RDS instance. 

3. Update `profiles.yml` in the dbt project [../solved/adventureworks/profiles.yml](../solved/adventureworks/profiles.yml) with the host and password. 

4. Run `dbt deps` and `dbt build` to materialize the serving tables. 

