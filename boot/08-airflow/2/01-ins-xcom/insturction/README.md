# Instruction

# Concept

## XCOM
XComs (short for “cross-communications”) are a mechanism that let Tasks talk to each other, as by default Tasks are entirely isolated and may be running on entirely different machines.

An XCom is identified by
- a key (essentially its name)
- task_id
- dag_id

XCOMs are designed for small amounts of data; do not use them to pass around large values, like dataframes.

Many operators e.g. PythonOperator push a XCOM called `return_value`. And XCOM pulls use this key as default as well.

`value = task_instance.xcom_pull(task_ids='pushing_task')`

`{{ task_instance.xcom_pull(task_ids='foo', key='table_name') }}`

## XCOM vs Variable
XComs are per-task-instance and designed for communication within a DAG run.
Variables are global and designed for overall configuration and value sharing.


# Task

Write a new DAG.

Use S3ListOperator to list the files in S3.

Use PythonOperator to transform the data.

Use XCOM to let PythonOperator aware of the files in S3.
