# Dynamic date config 

Excellent work at configuring your pipeline to work with metadata! 

## Task

Now here's a challenge, the user of your pipeline has asked you to add features that would allow them to configure the pipeline to extract data from different dates more easily. 

They would like to see the following functionality and configuration in YAML: 

```
# if date_picker is set to "date_range", then use the start_date and end_date in the extract function
date_picker: "date_range"
start_date: "2020-01-01"
end_date: "2020-01-02"

# if date_picker is set to "most_recent_weekday", then use the most recent weekday as the start_time, and set end_time to start_time + 1 day. 
date_picker: "most_recent_weekday"

# if date_picker is set to "days_from_start", then use the start_date as start_time, and start_date + days_from_start as the end_time
date_picker: "days_from_start"
start_date: "2020-01-01"
days_from_start: 5

# if date_picker is set to "days_from_end", then use the end_date - days_from_end as the start_time, and end_date as the end_time
date_picker: "days_from_end"
start_date: "2020-01-05"
days_from_end: 5
```

Tips: 

1. Have a look at `utility/date_time.py`
    - `get_most_recent_weekday_from_today()` has already been implemented for you. 
    - You will need to implement `get_end_date()` and `get_start_date()`
2. In `trading_price_pipeline.py` you will need to read in the YAML, and based on what `date_picker` is set to, configure `start_time` and `end_time` accordingly. 


