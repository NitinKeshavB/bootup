# Instruction

## Concept 

If we try joining fct tables to dim tables without taking into account the slowly changing dimension, then we end up only using the latest values from the dimension table and forgo keeping history. 

## Task 

1. Create a new fact table `fct_workorder_scd2` that takes into account the slowly changing dimension from `dim_scrapreason_scd2`


