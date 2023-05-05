-- upgrade: 
update purchasing.purchaseorderheader 
set status = 2,
    modifieddate = '2022-01-02',
    revisionnumber = 2
where purchaseorderid = 4013

-- downgrade: 
update purchasing.purchaseorderheader 
set status = 1
    modifieddate = '2022-01-01',
    revisionnumber = 1
where purchaseorderid = 4013
