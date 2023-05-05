import datetime
import pendulum

from airflow import DAG
from airflow.operators.weekday import BranchDayOfWeekOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.weekday import WeekDay

with DAG(
        dag_id='branching_stu',
        schedule_interval="0 8 * * *",
        start_date=pendulum.now(tz="UTC").subtract(months=1),
        catchup=True,
        dagrun_timeout=datetime.timedelta(minutes=5),
        tags=['branching'],
) as dag:
    four_working_day = EmptyOperator(task_id='four_working_day')
    long_weekend = EmptyOperator(task_id='long_weekend')

    weekend_check = BranchDayOfWeekOperator(
        task_id='weekend_check',
        week_day={WeekDay.FRIDAY, WeekDay.SATURDAY, WeekDay.SUNDAY},
        use_task_logical_date=True,
        follow_task_ids_if_true='long_weekend',
        follow_task_ids_if_false='four_working_day'
    )

    weekend_check >> [four_working_day, long_weekend]
