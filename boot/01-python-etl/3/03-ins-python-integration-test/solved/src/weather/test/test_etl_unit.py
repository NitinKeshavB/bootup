from weather.etl.transform import Transform
from weather.etl.load import Load
import pandas as pd
import os 
import shutil


def test_transform():
    # assemble 
    df_input = pd.DataFrame({
        "name": ["perth", "sydney"],
        "dt": [1657982968, 1657984968],
        "id": [1, 2],
        "main.temp": [27, 21]
    })

    df_input_population = pd.DataFrame({
        "city_name": ["perth", "sydney"],
        "population": [20000000, 60000000]
    })

    df_expected = df_expected = pd.DataFrame({
        "datetime": [1657982968, 1657984968],
        "id": [1, 2],
        "name": ["perth", "sydney"],
        "temperature": [27, 21],
        "population": [20000000, 60000000],
        "unique_id": ["16579829681", "16579849682"]
    }).set_index("unique_id")
    df_expected["datetime"] = pd.to_datetime(df_expected["datetime"], unit="s")

    # act 
    df_output = Transform.transform(df=df_input, df_population=df_input_population)

    # assert 
    pd.testing.assert_frame_equal(left=df_output, right=df_expected,check_exact=True)

def test_load():
    # assemble 
    df = pd.DataFrame({
        "datetime": [1657982968, 1657984968],
        "id": [1, 2],
        "name": ["perth", "sydney"],
        "temperature": [27, 21],
        "population": [20000000, 60000000],
        "unique_id": ["16579829681", "16579849682"]
    }).set_index("unique_id")
    df["datetime"] = pd.to_datetime(df["datetime"], unit="s")
    if "data" not in os.listdir("weather/test"): 
        os.mkdir("weather/test/data") # temp data output 

    # act 
    Load.load(
        df=df, 
        load_target="file", 
        load_method="upsert", 
        target_file_directory="weather/test/data",
        target_file_name="test_output.parquet"
    )
    assert "test_output.parquet" in os.listdir("weather/test/data")
    # cleanup 
    shutil.rmtree("weather/test/data")
