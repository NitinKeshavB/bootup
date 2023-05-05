# Incremental models 

## Task 

Implement an incremental model for `staging_trades` and `serving_trades` using the following steps: 

1. Check if the target table exists. 

```
{% set table_exists = engine.execute("select exists (select from pg_tables where tablename = '" + target_table + "')").first()[0] %}
```

2. If the target table does not exist (first load), then use CTAS to create the target table. 

3. If the target table already exists (subsequent load), then get the target_current_max_incremental_value from the target table, and use the following syntax structure to insert data into the target table: 


```sql
insert into target_table (
    select * 
    from source_table 
    where source_incremental_column > target_current_max_incremental_value
)
```
