{{
    config(
        materialized='table',
        database='hr',
        schema='model'
    )
}}
with agg as (
    select
        min(salary) as lowest_salary,
        date_part(year, from_date) salary_year
    from
        {{ source('payroll', 'salaries') }}
    group by
        salary_year
)
select
    lowest_salary,
    {{ salary_formatted('lowest_salary', true) }} as lowest_salary_show_cents,
    {{ salary_formatted('lowest_salary', false) }} as lowest_salary_no_cents,
    salary_year
from agg