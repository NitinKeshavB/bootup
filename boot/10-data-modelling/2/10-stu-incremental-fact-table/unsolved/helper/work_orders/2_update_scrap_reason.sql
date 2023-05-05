-- upgrade: 
update production.scrapreason
set 
	name = 'Handling or transport damage', 
	modifieddate = '2022-01-03'
where scrapreasonid = 7 

-- downgrade: 
update production.scrapreason
set 
	name = 'Handling damage', 
	modifieddate = '2008-04-30'
where scrapreasonid = 7 