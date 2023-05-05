-- upgrade: 
insert into production.workorder (
	workorderid,
	productid, 
	orderqty, 
	scrappedqty,
	startdate, 
	enddate,
	duedate, 
	modifieddate
) 
values 
( 72592, 722, 10, 0, '2022-01-01', null, '2022-01-12', '2022-01-01'),
( 72593, 791, 10, 0, '2022-01-01', null, '2022-01-12', '2022-01-01'),
( 72594, 891, 10, 0, '2022-01-01', null, '2022-01-12', '2022-01-01')

-- downgrade:
delete from production.workorder
where workorderid in (72592, 72593, 72594)
