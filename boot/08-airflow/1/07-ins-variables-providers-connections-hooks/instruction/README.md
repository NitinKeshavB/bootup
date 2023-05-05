# Instruction

## Concept

### Variables

Variables are a generic way to store and retrieve arbitrary content or settings as a simple key value store.

Variables are global, and should only be used for overall configuration that covers the entire installation.

Variables can be managed via
- UI
- Code
- CLI
- env

```shell
# Convention: AIRFLOW_VAR_{VARIABLE_NAME}
# To use String
export AIRFLOW_VAR_FOO=BAR
# To use JSON, store them as JSON strings
export AIRFLOW_VAR_FOO_BAZ='{"hello":"world"}'
```

```python
from airflow.models import Variable

foo = Variable.get("foo")
foo_json = Variable.get("foo_baz", deserialize_json=True)
```

```
{{ var.value.<variable_name> }}
```

### Connections

A Connection is essentially set of parameters - such as username, password and hostname, along with the type of system that it connects to.

Identified by `conn_id`.

Connections can be managed via
- UI
- Code
- CLI
- env

```shell
# Convention: AIRFLOW_CONN_{CONN_ID}

export AIRFLOW_CONN_MY_PROD_DATABASE='{
    "conn_type": "my-conn-type",
    "login": "my-login",
    "password": "my-password",
    "host": "my-host",
    "port": 1234,
    "schema": "my-schema",
    "extra": {
        "param1": "val1",
        "param2": "val2"
    }
}'

export AIRFLOW_CONN_MY_PROD_DATABASE='my-conn-type://login:password@host:port/schema?param1=val1&param2=val2'
```

```
{{ conn.<conn_id>.host }}
```

### Hooks

Get a hook from a connection.

A hook allows you to interact with the system on the other side of the connection.


### Providers

Airflow is built in modular way.

Airflow provides core scheduler functionality and allows you to do basic tasks.

The capabilities of Airflow can be extended by installing additional packages, called providers.

Common providers:
- PostgreSQL, MongoDB, Snowflake
- Amazon, Google, Microsoft Azure, ElasticSearch, Databricks
- Apache Spark, Celery, Docker, Kubernetes
- Slack, GitHub
- and more

## Task

Prerequisite - AWS:
1. create an AWS user called `airflow` with keys
2. create an S3 bucket called `decsydliu-airflow` with a folder called `ref`
3. upload `australian_capital_cities.csv` and `australian_city_population.csv` to the `ref` folder

Create connections:
- aws_decsydliu
- weather_api

Create variables:
- s3_bucket
- s3_key_ref_cities
- weather_api_key

Write DAG
- extract function
- extract task
