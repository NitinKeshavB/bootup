# Multi Day ETL 

Now that you have learnt the basics of working with Python Dates, you are going to apply these concepts on creating a function that returns a date list that can be used in your `Extract` logic to extract data from multiple days. 

## Task

1. Implement the `generate_datetime_ranges()` function. Read the function docstring to understand what the function needs to do, and implement the section marked `TODO`. 

```python
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
    # TODO: implement this function

    return date_range  
``` 

2. Modify your `requests` extraction logic to loop over the date list returned from `generate_datetime_ranges()`. Modify the section marked as `TODO` and verify that you are able to extract data for multiple days.

```python
# TODO: modify this entire code cell to use generate_datetime_ranges() and loop through a list of dates 
```

