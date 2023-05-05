import datetime

import pendulum

from airflow import DAG
from airflow.operators.datetime import BranchDateTimeOperator
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id='branching_ins',
        schedule_interval="0 */3 * * *",
        start_date=pendulum.now(tz="UTC").subtract(days=3),
        catchup=False,
        dagrun_timeout=datetime.timedelta(minutes=5),
        tags=['branching'],
) as dag:
    working_hours = EmptyOperator(task_id='working_hours')
    after_hours = EmptyOperator(task_id='after_hours')

    time_check = BranchDateTimeOperator(
        task_id='datetime_branch',
        use_task_logical_date=True,
        follow_task_ids_if_true=['working_hours'],
        follow_task_ids_if_false=['after_hours'],
        target_lower=pendulum.time(9, 0, 0),
        target_upper=pendulum.time(17, 0, 0)
    )
    time_check >> [working_hours, after_hours]
