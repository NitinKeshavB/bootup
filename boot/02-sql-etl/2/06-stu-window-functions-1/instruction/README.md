# Window functions

## Task 

Answer the following questions by writing Window Function queries. 

1. compare each customer's sales against the average city's sales, average country's sales, the customer's rank by sales, the customer's rank against city sales, the customer's rank against country sales

2. compare each film's rental sales to it's average category sales, average release year sales, the film's rank, the film's rank in its category, the film's rank in it's release year 

Hint: You will have to use the following functions: 
- `avg()`
- `rank()` and `over (partition by <your_column> order by <your_column>)`

Verify your output against `query_results.md`. 

Entity Relationship Diagram (ERD). 

![erd-diagram.png](erd-diagram.png)
