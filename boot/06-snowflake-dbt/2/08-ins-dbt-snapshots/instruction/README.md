# Instruction
Jane the HR asks if you could capture last name changes.

## Concepts
dbt snapshots implements SCD2, slowly changing dimension type 2.

Say a source table changes from

| id  | status  | updated_at |
|-----|---------|------------|
| 1   | pending | 2019-01-01 |

to

| id  | status  | updated_at |
|-----|---------|------------|
| 1   | shipped | 2019-01-02 |

SCD2 would capture that as 

| id  | status   | updated_at  | dbt_valid_from | dbt_valid_to |
|-----|----------|-------------|----------------|--------------|
| 1   | pending  | 2019-01-01  | 2019-01-01     | 2019-01-02   |
| 1   | shipped  | 2019-01-02  | 2019-01-02     | null         |

Example:
```
{% snapshot orders_snapshot %}

{{
    config(
      target_database='analytics',
      target_schema='snapshots',
      unique_key='id',

      strategy='timestamp',
      updated_at='updated_at',
    )
}}

select * from {{ source('jaffle_shop', 'orders') }}

{% endsnapshot %}
```

You'll need to tell dbt
1. Where to put the snapshot table to: `target_database`, `target_schema`
2. What is the strategy to detect changes: `strategy`
   1. If `timestamp` strategy, which column to look at: `updated_at`
   2. If `check` strategy, which columns to look at: `check_cols`
3. How to identify a unique record: `unique_key`
4. Whether reacting to hard deletes or not: `invalidate_hard_delete`

## Task
1. Create a snapshot on employees table. Snapshot models need to sit in the `/snapshots` folder. 
2. `dbt snapshot`
3. Update a record
4. `dbt snapshot`
5. Observe SCD2
