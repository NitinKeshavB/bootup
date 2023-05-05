-- upgrade: 
insert into purchasing.purchaseorderheader ( 
    purchaseorderid, 
    revisionnumber,
    status, 
    employeeid,
    vendorid,
    shipmethodid,
    orderdate,
    shipdate,
    subtotal,
    taxamt,
    freight,
    modifieddate
)
values 
(4013, 1, 1, 258, 1580, 3, '2022-01-01', '2022-01-10', 201.04, 16.0832, 5.026, '2022-01-01')

-- downgrade: 
delete from purchasing.purchaseorderheader 
where purchaseorderid = 4013
