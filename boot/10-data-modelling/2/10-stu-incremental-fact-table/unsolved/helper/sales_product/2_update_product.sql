-- upgrade: 
update production.product
set 
	name = 'Road-650 Maroon, 44',
    color = 'Maroon', 
	modifieddate = '2022-01-03'
where productid = 762

-- downgrade: 
update production.product
set 
	name = 'Road-650 Red, 44',
    color = 'Red', 
	modifieddate = '2008-04-30'
where productid = 762
