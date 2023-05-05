# Instruction

## Task

```
|-- dag_example
|-- dag_practice
  |-- my_first_dag_stu.py
  |-- branching_stu.py
|-- dag_etl
|-- function
```

Write a dag in `branching_stu.py`:
- disable catchup
- schedule once a day
- have 2 empty operators that represents `four_working_day` and `long_weekend` respectively
- use `BranchDayOfWeekOperator` to switch between 2 empty operators

Hint: Get weekday constants from `from airflow.utils.weekday import WeekDay`

Backfill for a week in the past month.

