select
    raw_obj:dept_no::varchar as dept_no,
    value:emp_no::varchar as emp_no,
    value:from_date::timestamp as from_date,
    value:to_date::timestamp as to_date
from
    HR.SOURCE.DEPT_MANAGER,
    lateral flatten(input => raw_obj:managers)
order by
    dept_no, from_date asc
;