{{
    config(
        materialized='table',
        database='hr',
        schema='model'
    )
}}
select
    round(avg(sal.salary), 2) as average_salaries,
    emp.year_became_senior,
    count(1) as num_of_emp,
    current_timestamp(0) as inserted_at
from
    {{ ref('current_senior') }} emp
    left join {{ ref('current_salary') }} sal
    on emp.emp_no = sal.emp_no
group by
    emp.year_became_senior
