import datetime as dt
import logging 

class DateTime():

    @staticmethod
    def get_today()->str:
        return dt.date.today().strftime("%Y-%m-%d")

    @staticmethod
    def get_most_recent_weekday_from_today()->str:
        """
        Get the most recent weekday from today's date. 
        Usage example:
            get_most_recent_weekday_from_today()
            returns:
                "2022-01-01"
        """
        date = dt.date.today()
        while date.weekday() > 4: # Mon-Fri are 0-4
            date -= dt.timedelta(days=1)
        return date.strftime("%Y-%m-%d")

    @staticmethod
    def get_end_date(
            start_date:str=None, 
            days_from_start:int=None
        )->str:
        """
        Get the end date by counting forwards from the start date
        - start_date: date where the date range begins 
        - days_from_start: number of days from the start_date used to calculate the end_date
        Usage example: 
        - get_end_date("2020-01-01", 5)
            returns: 
                "2020-01-05"
        """
        if start_date is not None and days_from_start is not None: 
            dte_start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
            dte_end_date = dte_start_date + dt.timedelta(days=days_from_start)
            return dte_end_date.strftime("%Y-%m-%d")
        else: 
            raise Exception("The parameters passed in results in no action being performed.")

    @staticmethod
    def get_start_date(
            end_date:str=None, 
            days_from_end:int=None
        )->str:
        """
        Get the start date by counting backwards from the end date
        - end_date: date where the date range stops 
        - days_from_end: number of days from the end_date used to calculate the start_date
        Usage example: 
        - get_start_date("2020-01-05", 5)
            returns: 
                "2020-01-01"
        """
        if end_date is not None and days_from_end is not None: 
            dte_end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
            dte_start_date = dte_end_date - dt.timedelta(days=days_from_end)
            return dte_start_date.strftime("%Y-%m-%d")
        else: 
            raise Exception("The parameters passed in results in no action being performed.")

    @staticmethod
    def generate_datetime_ranges(
        start_date:str=None, 
        end_date:str=None, 
        )->list:
        """ 
        Generates a range of datetime ranges. 
        - start_date: provide a str with the format "yyyy-mm-dd"
        - end_date: provide a str with the format "yyyy-mm-dd" 
        Usage example: 
        - generate_datetime_ranges(start_date="2020-01-01", end_date="2022-01-02")
            returns: 
                [
                    'start_time': '2020-01-01T00:00:00.00Z', 'end_time': '2020-01-02T00:00:00.00Z'}, 
                    {'start_time': '2020-01-02T00:00:00.00Z', 'end_time': '2020-01-03T00:00:00.00Z'}
                ]
        """

        date_range = []
        if start_date is not None and end_date is not None: 
            dte_start_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
            dte_end_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
            date_range = [
                {
                    "start_time": (dte_start_date + dt.timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%S.00Z"),
                    "end_time": (dte_start_date + dt.timedelta(days=i) + dt.timedelta(days=1)).strftime("%Y-%m-%dT%H:%M:%S.00Z"),
                }
            for i in range((dte_end_date - dte_start_date).days)]
        else: 
            raise Exception("The parameters passed in results in no action being performed.")

        return date_range  