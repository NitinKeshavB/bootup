{{
    config(
        materialized='ephemeral'
    )
}}
select
    emp_no,
    salary
from
   {{ source('payroll', 'salaries') }}
where
    to_date = '9999-01-01'
