{{
    config(
        materialized='table',
        database='hr',
        schema='model'
    )
}}
select
    emp_no,
    date_part(year, from_date) as year_became_senior,
    current_timestamp(0) as inserted_at
from
   {{ source('hr', 'titles') }}
where
    title like 'Senior%'
    and to_date = '9999-01-01'