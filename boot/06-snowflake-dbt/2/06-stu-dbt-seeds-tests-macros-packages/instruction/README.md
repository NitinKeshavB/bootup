# Instruction
HR would like to see the lowest salary in each year. (to simplify, use the `from_date` in `salaries` table as the year for that salary)

They have two different visualisations that needs `$99999.00` and `$99999` format separately.

They would like to you build a test to make sure the salaries are above the minimum wage of that year.

They also want to have a calendar table for future use.

## Task
To satisfy this requirement:
1. create `packages.yml`, install dependencies https://hub.getdbt.com/dbt-labs/dbt_utils/latest/
2. Use `dbutils.date_spine` to write a model in `models/model/calendar.sql` that has these columns:
   1. the date
   2. day (`date_part()`)
   3. month
   4. year
   5. quarter
   6. 3 letter weekday name (`dayname()`)
3. modify `seeds/seeds.yml`, seed minimum_legal_salaries.csv
4. write a marco in `marcos/salary_formatted.sql`, it takes a parameter called `show_cents`, use jinja if-else and  `to_varchar(COL_NAME, FORMAT)`
5. write a table model in `models/model/lowest_salary_of_the_year.sql` to hr.model that has these columns:
   1. lowest_salary (integer)
   2. lowest_salary_show_cents
   3. lowest_salary_no_cents
   4. salary_year
6. write a singular test in `tests/legal_salary_check.sql` : salary should be above each year's legal minimum
7. change the seed file to increase any salary by 10k and observe the test fail