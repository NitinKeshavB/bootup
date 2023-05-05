select
    *
from
    {{ ref('lowest_salary_of_the_year') }} sal
    inner join {{ ref('minimum_legal_salaries') }} legal
    on sal.salary_year = legal.salary_year
where
    sal.lowest_salary < legal.minimum_salary