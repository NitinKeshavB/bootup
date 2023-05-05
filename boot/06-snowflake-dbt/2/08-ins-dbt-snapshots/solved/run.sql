dbt snapshot

select * from hr.model.dim_employee where emp_no = '10002';

update  hr.source.employees set last_name='Johnson', updated_at=current_timestamp() where emp_no='10002' ;

dbt snapshot

select * from hr.model.dim_employee where emp_no = '10002';
