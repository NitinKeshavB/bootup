-- upgrade: 
update production.workorder 
set scrapreasonid = 7,
    modifieddate = '2022-01-03',
    enddate = '2022-01-03',
    scrappedqty = 10
where workorderid = 72593

-- downgrade: 
update production.workorder 
set scrapreasonid = null,
    modifieddate = '2022-01-01',
    enddate = null,
    scrappedqty = 0
where workorderid = 72593
