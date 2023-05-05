-- upgrade: 
update purchasing.purchaseorderheader 
set status = 4,
    modifieddate = '2022-01-03',
    revisionnumber = 3
where purchaseorderid = 4013

-- downgrade: 
update purchasing.purchaseorderheader 
set status = 2
    modifieddate = '2022-01-02',
    revisionnumber = 2
where purchaseorderid = 4013
