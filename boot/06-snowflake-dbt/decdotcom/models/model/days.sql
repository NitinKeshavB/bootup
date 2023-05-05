{{
    config(
        materialized='table',
        database='hr',
        schema='model'
    )
}}
{{ dbt_utils.date_spine(
    datepart="day",
    start_date="cast('1980-01-01' as date)",
    end_date="cast('2100-01-01' as date)"
   )
}}
