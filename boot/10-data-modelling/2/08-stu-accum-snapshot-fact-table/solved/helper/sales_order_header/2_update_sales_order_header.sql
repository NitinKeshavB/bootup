-- upgrade: 
update sales.salesorderheader 
set status = 2,
    modifieddate = '2022-01-02',
    revisionnumber = 2
where salesorderid = 75125

-- downgrade: 
update purchasing.purchaseorderheader 
set status = 1,
    modifieddate = '2022-01-01',
    revisionnumber = 1
where salesorderid = 75125
