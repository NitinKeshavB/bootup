import pandas as pd 
import requests 

class Extract():

    @staticmethod
    def extract_city(
            api_key:str,
            city_name:str=None,
            temperature_units:str="metric"
        )->pd.DataFrame:
        """
        Extracting data from the weather API. 
        - api_key: api key 
        - city name: name of the city e.g. perth
        - temperature_units: choose one of "metric" or "imperial" or "standard"
        """
        params = {
            "q": city_name,
            "units": temperature_units,
            "appid": api_key
        }
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather", params=params)
        if response.status_code == 200: 
            weather_data = response.json()
        else: 
            raise Exception("Extracting weather api data failed. Please check if API limits have been reached.")
        df_weather_cities = pd.json_normalize(weather_data)
        return df_weather_cities

    @staticmethod
    def extract(
            api_key:str,
            fp_cities:str,
            temperature_units:str="metric"
        )->pd.DataFrame:
        """
        Perform extraction using a filepath which contains a list of cities. 
        - api_key: api key 
        - fp_cities: filepath to a CSV file containing a list of cities 
        - temperature_units: choose one of "metric" or "imperial" or "standard"
        """

        # read list of cities
        df_cities = pd.read_csv(fp_cities)
        # request data for each city (json) and push to a list 
        df_concat = pd.DataFrame()
        for city_name in df_cities["city_name"]:
            df_extracted = Extract.extract_city(api_key=api_key,city_name=city_name,temperature_units=temperature_units)
            df_concat = pd.concat([df_concat,df_extracted])
        return df_concat.reset_index().drop(labels=["index"], axis=1)
    
    @staticmethod
    def extract_population(
        fp_population:str
    )->pd.DataFrame:
        """Extracts data from the population file"""
        df_population = pd.read_csv(fp_population)
        return df_population