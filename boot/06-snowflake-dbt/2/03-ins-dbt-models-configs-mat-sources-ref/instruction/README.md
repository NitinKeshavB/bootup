# Instruction

## Concept
### Model
* A model is a `select` statement in a SQL file
* 1 model = 1 SQL file
* file name = model name
* could be in subdirectories

A good convention is to organise your models into sub-folders. In our case, we impose folder name = schema name. Some others may organise by business unit or dim/fact.

### `dbt run` Command
`dbt run` will compile all your models in the project and run them.

In `target` folder, you will see the `compiled` and `run` folders containing the SQL files generated at each stage of a run.

#### Selection
To select a certain model: `dbt run --select model_name`

#### Graph Operator
To select a certain model and all its parents: `dbt run --select +model_name`

To select a certain model and immediate parents and its children down to the 2nd degree: `dbt run --select 1+model_name+2`

## Task
`dbt run --select avg_salary_for_senoirs_by_tenure`

Does it work?

## Concept
### Config Block
A config block can be used to change the default project/profile level behaviour for a certain model.
These could include:
- Change the materialisation
- Build models into a different database or schema
- Apply hooks
- Add tags etc.

Example:
```
{{
  config(
    materialized='incremental',
    unique_key='id'
  )
}}
```

[Ref: other config options](https://docs.getdbt.com/reference/model-configs)

A note on schema:

The default behaviour here is that dbt will append your custom schema to the default schema and give you `<default_schema>_<custom_schema>`.
This is somewhat useful when you have multiple people collaborating.
However, in our settings, we like what-you-see-is-what-you-get.
Please put `generate_schema_name.sql` under marcos folder.

#### Snowflake Specific Configs
- transient (explained in next section, now just focus on configs)
```
{{ 
    config(
        materialized='table',
        transient=true
    )
}}
```
- cluster by
```
{{
  config(
    materialized='table',
    cluster_by=['session_start']
  )
}}
```
- snowflake_warehouse (virtual warehouse name)
- and [some others](https://docs.getdbt.com/reference/resource-configs/snowflake-configs)

### Materialisation
Materialisation is about how to persist models in a warehouse.

What materialisation is available?
- view
- table
- incremental
- ephemeral
- custom, build your own!

View and table are self-explanatory.

#### Materialisation: incremental
- insert or update records into a table since the last time that dbt was run
- extra configs needed
- good on event-style data

Example 1:

The `is_incremental()` part filters records and remain only the new records.

`{{ this }}` variable refers to the table itself.

```
{{
    config(
        materialized='incremental'
    )
}}
```
```
select
    *,
    my_slow_function(my_column)
from
    raw_app_data.events

{% if is_incremental() %}
  where event_time > (select max(event_time) from {{ this }})
{% endif %}
```
Example 2:

`unique_key` defines what is a unique record, so that insert/update is performed accordingly.

If multiple columns, use a list.
```
{{
    config(
        materialized='incremental',
        unique_key='date_day'
    )
}}
```
```
select
    date_trunc('day', event_at) as date_day,
    count(distinct user_id) as daily_active_users
from
    raw_app_data.events

{% if is_incremental() %}
  where date_day >= (select max(date_day) from {{ this }})
{% endif %}

group by 1
```
FAQ:
- What if I have a fundamental change, and I want to rebuild an incremental model from scratch?
  - Use the `--full-refresh` flag.
  - `dbt run --full-refresh --select changed_incremental_model`
- When to use incremental model? 
  - Only when your `materialised='table'` model runs for too long.
  - This could be a result of either large volume of data or complex transformation.
- How does dbt know if it is an incremental run? 
  - dbt checks that 
    1. the destination table already exists in the database 
    2. dbt is not running in full-refresh mode
    3. the running model is configured with materialized='incremental'
- What actually happens behind the scene when it is an incremental run?
  - In warehouses that supports `merge`, it is a `merge`. Otherwise, either `delete+insert` or `insert_overwrite`.
  - Config `incremental_strategy` to change the strategy
- What if I only want to update a subset of the columns?
  - With `merge` strategy, use config `merge_update_columns = ['email', 'ip_address'],`

This would be an impressive feature to use in your project. :)

#### Materialisation: ephemeral
Essentially, this means it doesn't go into your warehouse. You can't even `select` from it.

Think an ephemeral model as just a building block. Other models can build upon ephemeral models.

### Source

Sources are used to describe tables loaded by means other than dbt. In our example, the tables we loaded manually are all sources.

Sources are defined in yml files.
- name it whatever you want
- put it wherever you want as long as it is in the `models` folder
- organisation-wise, put it where it makes sense, maybe a centralised place for all


Sources can enable
- freshness check
- assumption tests

Sources are defined in yml files:
```
version: 2

sources:
  - name: jaffle_shop # this is the source_name
    database: raw
    schema: jaffle_shop
    tables:
      - name: orders # this is the table_name
      - name: customers

  - name: stripe
    database: raw
    schema: stripe
    tables:
      - name: payments
```
When using a source, use the `source()` function `{{ source('jaffle_shop', 'orders') }}`. 

dbt will translate that into full table names `raw.jaffle_shop.orders`.

## Task
`dbt run --select avg_salary_for_senoirs_by_tenure2`

Does it work?

## Concept
### `ref()` function
`ref()` function is used to reference a model written in dbt.

The syntax is `{{ ref(another_model_name) }}`

- `ref()` helps dbt build determine the order to run models by creating a DAG
- you should never use direct table names, they are replaced by either `source()` or `ref()`
- in a multiple env setting, `ref()` handles the changing database and schema name


## Task
`dbt run --select avg_salary_for_senoirs_by_tenure3`