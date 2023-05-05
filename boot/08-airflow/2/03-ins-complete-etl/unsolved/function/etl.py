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


def transform(s3_conn_id, s3_bucket, s3_keys, s3_key_ref_populations, data_interval_end):
    import pandas as pd
    import json
    import os
    from airflow.providers.amazon.aws.hooks.s3 import S3Hook

    s3_hook = S3Hook(aws_conn_id=s3_conn_id)

    # concatenate all json
    df_concat = pd.DataFrame()
    for k in s3_keys:
        json_file = s3_hook.download_file(key=k, bucket_name=s3_bucket)
        with open(json_file, 'r') as f:
            df_weather_city = pd.json_normalize(json.load(f))
        df_concat = pd.concat([df_concat, df_weather_city])
        os.unlink(json_file)

    # set city names to lowercase
    df_concat["city_name"] = df_concat["name"].str.lower()

    # merge with population
    population_file = s3_hook.download_file(key=s3_key_ref_populations, bucket_name=s3_bucket)
    df_population = pd.read_csv(population_file)
    df_merged = pd.merge(left=df_concat, right=df_population, on=["city_name"])
    os.unlink(population_file)

    # select columns
    df_selected = df_merged[["dt", "id", "name", "main.temp", "population"]]

    # add new column unique_id
    df_selected["unique_id"] = df_selected["dt"].astype(str) + df_selected["id"].astype(str)

    # convert unix timestamp column to datetime
    df_selected["dt"] = pd.to_datetime(df_selected["dt"], unit="s")

    # rename colum names to more meaningful names
    df_selected = df_selected.rename(columns={
        "dt": "datetime",
        "main.temp": "temperature"
    })

    # uploading back to s3
    tmp_file = '/tmp/selected.csv'
    df_selected.to_csv(tmp_file, index=False)
    expected_new_key = f's3://{s3_bucket}/staging/{data_interval_end}/{data_interval_end}.csv'
    s3_hook.load_file(filename=tmp_file, key=expected_new_key, replace=True)
    os.unlink(tmp_file)

    return expected_new_key
