# Instruction

HR has another request:

- Can we build a table to calculate the median starting salary of Junior employees by their title, gender and the year they started the role?
  - Junior employee means Assistant Engineer and Staff
  - Starting salary means the salary when they started their role
- We also have a dashboard that visualises the same information, but only for Assistant Engineers. Maybe we can build a view for that?

## Task

Work on
1. `model/sources.yml`
2. `model/median_salary_for_junior_by_title_tenure_gender.sql` 
3. `expose/vw_median_salary_for_junior_engineer_by_title_tenure_gender.sql`

---
### General steps
- Define sources
- Write models
  - What sources do you need?
  - What columns do you need from each source?
  - What do you aggregate on?
  - Use CTE to build step by step (get juniors -> get their starting salaries, also add in their gender before aggregation)
- Config block
  - Which database and schema?
  - Which materialisation?
- dbt run! (with a plus)
