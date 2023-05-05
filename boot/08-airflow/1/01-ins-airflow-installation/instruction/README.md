# Instruction

## Concept

Airflow is a platform that runs DAG.
- DAG = workflow
- node in DAG = task

Theoretically it orchestrates and runs anything you tell it to run. It cares only about dags and is agnostic to what is actually run.

### Components
- **A webserver** that hosts web UI
- **A scheduler** that triggers workflow and submits tasks to executor
- **An executor** that runs tasks
- **A metadata database** used by the scheduler, executor and webserver to store state
- **A folder of DAG files** read by the scheduler and executor

![](images/arch-diag-basic.png)

Depends on the executor type, you could have a multi node setup.

This means the above components run in different nodes. And your tasks run in different workers on different machines.

This scale things up and is often a choice for enterprise level production load e.g. `KubenetesExecutor`, if you don't use a managed service like MWAA.

But for the easiness of setting things up, we will use the `SequentialExecutor` and `sqlite` as metadata db.

## Task
1. Create a `dags` folder, copy the `dag_example` folder into it
2. Start the Airflow docker container
3. `airflow.cfg`
   1. `dags_folder` where dags are read from
   2. `executor`
   3. `dag_dir_list_interval` new dags appear after this interval
   4. `min_file_process_interval` updated dags are re-parsed after this interval
4. UI walk through
   1. All Dag view, then enable one
   2. Dag detail view
5. There are some cli as well