-- upgrade: 
update sales.salesorderheader 
set revisionnumber = 2,
    modifieddate = '2022-01-03',
    shipdate = '2022-01-03'
where salesorderid = 75124;

update sales.salesorderdetail 
set modifieddate = '2022-01-03'
where salesorderid = 75124 and salesorderdetailid = 121318;

update sales.salesorderdetail 
set modifieddate = '2022-01-03'
where salesorderid = 75124 and salesorderdetailid = 121319;

-- downgrade: 
update sales.salesorderheader 
set revisionnumber = 1,
    modifieddate = '2022-01-01',
    shipdate = null
where salesorderid = 75124;
