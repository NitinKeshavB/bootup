import pandas as pd 

class Transform():

    @staticmethod
    def transform(
            df:pd.DataFrame, 
            df_population:str=None
        )->pd.DataFrame:
        """
        Transform the raw dataframes. 
        - df: the dataframe produced from extract(). 
        - df_population: the dataframe produced from extract_population(). 
        """
        # set city names to lowercase 
        df["city_name"] = df["name"].str.lower()
        df_merged = pd.merge(left=df, right=df_population, on=["city_name"])
        df_selected = df_merged[["dt", "id", "name", "main.temp", "population"]] 
        df_selected["unique_id"] = df_selected["dt"].astype(str) + df_selected["id"].astype(str)
        # convert unix timestamp column to datetime 
        df_selected["dt"] = pd.to_datetime(df_selected["dt"], unit="s")
        # rename colum names to more meaningful names
        df_selected = df_selected.rename(columns={
            "dt": "datetime",
            "main.temp": "temperature"
        })
        df_selected = df_selected.set_index(["unique_id"])
        return df_selected 