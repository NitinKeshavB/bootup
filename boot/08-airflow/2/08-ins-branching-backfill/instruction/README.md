# Instruction

## Concept

### Branching

Branching operators are a special kind of operators that works like if-else.

Some common ones:

```
from airflow.operators.python import BranchPythonOperator
from airflow.operators.datetime import BranchDateTimeOperator
from airflow.operators.weekday import BranchDayOfWeekOperator
```
`BranchDateTimeOperator` and `BranchDayOfWeekOperator` are straightforward.

`BranchPythonOperator` accepts a Python function. The function must return a string or a list. The return value is the `task_id` to be executed next, other branches are skipped.

Use with caution, if used in a wrong flow logic, this operator might break idempotence.

### Backfill

Backfill lets you manually run a dag for all the intervals within the start date and end date. Start and end dates can be overridden.

Catchup is automatic and respects start and end dates.

```
airflow dags backfill -s 2022-10-01 -e 2022-10-02
```

## Task

Write a dag:
- disable catchup
- schedule for every 3 hours
- use `BranchDateTimeOperator` to switch between 2 empty operators that represent work hours and after hours respectively

Backfill for a day in the past week.