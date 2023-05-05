import datetime
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.operators.s3 import S3ListOperator
from function.alpaca_functions import transform

with DAG(
        dag_id='alpaca_etl2',
        schedule_interval='0 0 * * *',
        start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
        catchup=False,
        render_template_as_native_obj=True,
        dagrun_timeout=datetime.timedelta(minutes=5),
        tags=['weather'],
) as dag:
    data_interval_start = "{{ data_interval_start.to_rfc3339_string() }}"
    data_interval_end = "{{ data_interval_end.to_rfc3339_string() }}"

    aws_conn_id = "aws_decsydliu"
    s3_bucket = "{{ var.value.S3_BUCKET_ALPACA }}"
    s3_key_ref_exchange_codes = "{{ var.value.S3_KEY_REF_EXCHANGE_CODES }}"

    list_files = S3ListOperator(
        task_id="list_files",
        aws_conn_id=aws_conn_id,
        bucket=s3_bucket,
        prefix=f"landing/{data_interval_end}/",
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform,
        op_kwargs={
            "s3_conn_id": aws_conn_id,
            "s3_bucket": s3_bucket,
            "s3_keys": "{{ ti.xcom_pull('list_files') }}",
            "s3_key_ref_exchange_codes": s3_key_ref_exchange_codes,
            "data_interval_end": data_interval_end
        }
    )

    list_files >> transform_task
