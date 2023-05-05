# Instruction

## Concept

### PythonOperator

A commonly used operator is `PythonOperator` from `airlfow.operators.python`.

If you are picky about the runtime, there's also `PythonVirtualenvOperator` and `ExternalPythonOperator`.


### Logging

Loggings are configurable in `airflow.cfg` under `[logging]`.

By default, it is stored locally at `/opt/airflow/logs` and shows `INFO`.

It is possible to set remote logging and have your logs in S3 or other Cloud storages.

## Task
Let's write our first DAG using the `PythonOperator`!