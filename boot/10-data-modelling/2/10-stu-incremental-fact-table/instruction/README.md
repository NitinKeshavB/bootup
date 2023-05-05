# Instruction

## Task 

1. Create an incremental fact table for `fct_sales` called `fct_sales_incr` since the table is large. 

```
# note: you can re-create an incremental by using the --full-refresh flag
dbt run -m fct_sales_incr --full-refresh
```
