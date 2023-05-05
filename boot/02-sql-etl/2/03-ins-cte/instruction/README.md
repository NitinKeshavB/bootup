# Common table expressions (CTEs)

## Concept 

A Common Table Expression, also called as CTE in short form, is a temporary named result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement.

CTEs are an excellent way of breaking down a complex query into multiple steps, and also for reusing queries across multiple steps. The way we use it is similar to how we break steps down when working with Pandas DataFrames.

```
# pandas 
1. Create df_A
2. Create df_B 
3. df_final = df_A join with df_B 

# CTE
1. Create expression_A
2. Create expression_B
3. final = expression_A join with expression_B
```

## Implement 

CTEs begins by using a `with` followed by the expression name and query. To view the CTE result we use a Select query with the CTE expression name. For example: 

```sql 
with step_one as (
    select * from table_x 
), 
step_two as (
    select * from table y 
)

select * 
from table_x inner join table_y
    on table_x.id = table_y.id 
```

Let's now apply this concept on our DVD rental database. 

