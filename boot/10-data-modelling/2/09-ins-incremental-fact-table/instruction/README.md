# Instruction

## Task 

1. Create an incremental fact table for `fct_workorder` called `fct_workorder_incr` since the table is large 

```
# note: you can re-create an incremental by using the --full-refresh flag
dbt run -m fct_workorder_incr --full-refresh
```
