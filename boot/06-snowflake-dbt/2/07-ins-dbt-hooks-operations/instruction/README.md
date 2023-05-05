# Instruction

## Concept
### Hooks
There's often some SQL commands to run before or after your model:
- Managing permissions
- Vacuuming tables on Redshift
- Creating partitions in Redshift Spectrum external tables
- Resuming/pausing/resizing warehouses in Snowflake
- Create a share on Snowflake
- Cloning a database on Snowflake

This kind of "extra" work is a good use case for hooks.

#### Types
There are 4 types of hooks:
- `pre-hook`: executed before a model, seed or snapshot is built.
- `post-hook`: executed after a model, seed or snapshot is built.
- `on-run-start`: executed at the start of `dbt run`, `dbt seed`, `dbt test`, `dbt snapshot`, `dbt build`, `dbt compile` and `dbt docs generate`
- `on-run-end`: executed at the end of `dbt run`, `dbt seed`, `dbt test`, `dbt snapshot`, `dbt build`, `dbt compile` and `dbt docs generate`

#### Executing Order
Hooks can be defined in both `dbt_project.yml` and in `config` blocks. Unlike other configs and properties, hooks are cumulative.
dbt run hooks using the following ordering:
1. Hooks in dependent packages
2. Hooks in the active package 
3. Hooks defined within the model itself 
4. Hooks defined in dbt_project.yml. 
5. Hooks defined in the same context will be run in the order in which they are defined.

#### Transactions
Where transactions apply (Postgres and Redshift), hooks are executed in the same transaction as your model.

Use `before_begin` and `after_commit` to execute hoos outside of transaction.

## Task
1. Add a `post-hook` to unload data into S3
2. `dbt run`
3. Git bash, `gzip -d file_name`

## Concept
### `run-operation`
Operations are macros that you can run using the `run-operation` command. They are just a convenient way to invoke a macro without needing to run a model.

Unlike hooks, you need to explicitly execute a query within a macro, by using either a statement block or a helper macro like the `run_query` macro. Otherwise, dbt will return the query as a string without executing it

Example:
```
{% macro grant_select(role) %}
{% set sql %}
    grant usage on schema {{ target.schema }} to role {{ role }};
    grant select on all tables in schema {{ target.schema }} to role {{ role }};
    grant select on all views in schema {{ target.schema }} to role {{ role }};
{% endset %}

{% do run_query(sql) %}
{% do log("Privileges granted", info=True) %}
{% endmacro %}

```

`$ dbt run-operation grant_select --args '{role: reporter}'`