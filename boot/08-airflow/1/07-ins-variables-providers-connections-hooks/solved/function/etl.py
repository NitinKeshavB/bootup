def extract(s3_conn_id, s3_bucket, s3_key_ref_cities, api_conn_id, api_key, data_interval_end):
    import pandas as pd
    import json
    import os
    from airflow.providers.http.hooks.http import HttpHook
    from airflow.providers.amazon.aws.hooks.s3 import S3Hook
    # from airflow.operators.python import get_current_context

    # context = get_current_context()
    # ti = context["ti"]
    # ti.xcom_push("my_key", 1)

    # get city file
    s3_hook = S3Hook(aws_conn_id=s3_conn_id)
    cities_file = s3_hook.download_file(key=s3_key_ref_cities, bucket_name=s3_bucket)
    df_cities = pd.read_csv(cities_file)
    os.unlink(cities_file)

    # for each city
    http_hook = HttpHook(method="GET", http_conn_id=api_conn_id)
    expected_new_keys = {
        city_name: f's3://{s3_bucket}/landing/{data_interval_end}/{city_name}_{data_interval_end}.json'
        for city_name in df_cities["city_name"]
    }
    for city_name in df_cities["city_name"]:
        # call api
        params = {
            # ideally date_interval_end also a param
            "appid": api_key,
            "units": "metric",
            "q": city_name
        }
        resp = http_hook.run(endpoint="?", data=params)

        # serialise the json file into landing/
        if resp.status_code == 200:
            weather_data = resp.json()
            new_key = expected_new_keys[city_name]
            filename = new_key.split("/")[-1]
            tmp_file = f"/tmp/{filename}"
            with open(tmp_file, 'w') as f:
                json.dump(weather_data, f)
            s3_hook.load_file(filename=tmp_file, key=new_key, replace=True)
            os.unlink(tmp_file)
        else:
            raise Exception("Extracting weather api data failed. Please check if API limits have been reached.")
    # expected_new_keys['nonsense']='s3://decsydliu-airlfow/nonsense'
    return list(expected_new_keys.values())