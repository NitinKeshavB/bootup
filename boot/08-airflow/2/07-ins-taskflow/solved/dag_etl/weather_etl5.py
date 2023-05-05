import datetime
import pendulum

from airflow.providers.amazon.aws.sensors.s3 import S3KeySensor
from airflow.providers.amazon.aws.operators.s3 import S3ListOperator
from airflow.decorators import dag
from function.etl_taskflow import extract, transform, load
from airflow import XComArg


@dag(
    schedule_interval='0 0 * * *',
    start_date=pendulum.datetime(2022, 1, 1, tz="UTC"),
    catchup=False,
    render_template_as_native_obj=True,
    dagrun_timeout=datetime.timedelta(minutes=5),
    tags=['weather'],
)
def weather_etl5():
    data_interval_end = "{{ data_interval_end.format('YYYYMMDDHHmmss') }}"

    aws_conn_id = "aws_decsydliu"
    s3_bucket = "{{ var.value.S3_BUCKET }}"
    s3_key_ref_cities = "{{ var.value.S3_KEY_REF_CITIES }}"
    s3_key_ref_populations = "{{ var.value.S3_KEY_REF_POPULATIONS }}"

    api_conn_id = "weather_api"
    weather_api_key = "{{ var.value.WEATHER_API_KEY }}"

    pg_conn_id = "postgres_decsydliu"

    expected_landing_keys = extract(
        s3_conn_id=aws_conn_id,
        s3_bucket=s3_bucket,
        s3_key_ref_cities=s3_key_ref_cities,
        api_conn_id=api_conn_id,
        api_key=weather_api_key,
        data_interval_end=data_interval_end
    )

    verify_extract = S3KeySensor.partial(
        task_id="verify_extract",
        aws_conn_id=aws_conn_id,
        poke_interval=10,
        timeout=30
    ).expand(
        bucket_key=expected_landing_keys
    )

    list_files = S3ListOperator(
        task_id="list_files",
        aws_conn_id=aws_conn_id,
        bucket=s3_bucket,
        prefix=f"landing/{data_interval_end}/",
    )

    verify_extract >> list_files

    staging_keys = transform(
        s3_conn_id=aws_conn_id,
        s3_bucket=s3_bucket,
        # s3_keys="{{ ti.xcom_pull('list_files') }}",
        s3_keys=XComArg(list_files),
        s3_key_ref_populations=s3_key_ref_populations,
        data_interval_end=data_interval_end
    )

    verify_transform = S3KeySensor(
        task_id="verify_transform",
        aws_conn_id=aws_conn_id,
        poke_interval=10,
        timeout=30,
        bucket_key=[staging_keys]
    )

    load_task = load(
        s3_conn_id=aws_conn_id,
        s3_bucket=s3_bucket,
        postgres_conn_id=pg_conn_id,
        data_interval_end=data_interval_end
    )

    verify_transform >> load_task


runthis = weather_etl5()
