from weather.etl.extract import Extract
from weather.etl.transform import Transform
import os 


def test_extract_transform_integration():
    # assemble 
    api_key = os.environ.get("api_key")

    df = Extract.extract(
        api_key=api_key, 
        fp_cities="weather/data/australian_capital_cities.csv",
        temperature_units="metric"
    )
    df_population = Extract.extract_population(fp_population="weather/data/australian_city_population.csv")

    # act 
    df_transformed = Transform.transform(df=df, df_population=df_population)

    # assert 
    assert df_transformed.iloc[0][["name"]].to_dict() == {"name": "Canberra"}
