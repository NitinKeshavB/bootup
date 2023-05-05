-- upgrade: 
update sales.salesorderheader 
set status = 5,
    modifieddate = '2022-01-08',
    revisionnumber = 4
where salesorderid = 75125

-- downgrade: 
update purchasing.purchaseorderheader 
set status = 3,
    modifieddate = '2022-01-04',
    revisionnumber = 3
where salesorderid = 75125