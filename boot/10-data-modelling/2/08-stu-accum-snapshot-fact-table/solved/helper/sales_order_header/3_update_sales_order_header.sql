-- upgrade: 
update sales.salesorderheader 
set status = 3,
    modifieddate = '2022-01-04',
    revisionnumber = 3
where salesorderid = 75125

-- downgrade: 
update purchasing.purchaseorderheader 
set status = 2,
    modifieddate = '2022-01-02',
    revisionnumber = 2
where salesorderid = 75125
