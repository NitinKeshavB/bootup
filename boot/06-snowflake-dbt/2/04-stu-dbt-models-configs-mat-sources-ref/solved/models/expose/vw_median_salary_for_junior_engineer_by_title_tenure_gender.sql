{{
    config(
        materialized='view',
        database='hr',
        schema='expose'
    )
}}
select
    *
from
    {{ ref('median_salary_for_junior_by_title_tenure_gender') }}
where
    title = 'Assistant Engineer'