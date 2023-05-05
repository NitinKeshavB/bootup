-- upgrade: 
insert into sales.salesorderheader (
	salesorderid,
	revisionnumber, 
	orderdate, 
	duedate,
	shipdate, 
	status,
	onlineorderflag, 
	purchaseordernumber,
    accountnumber,
    customerid,
    salespersonid,
    territoryid,
    billtoaddressid,
    shiptoaddressid,
    shipmethodid,
    creditcardid,
    creditcardapprovalcode,
    currencyrateid,
    subtotal,
    taxamt,
    freight,
    totaldue,
    modifieddate
)  
values 
(75125, 1, '2022-01-01', '2022-02-09', null, 1, false, 'PO18850127500', '10-4020-000117', 29672, 279, 5, 921, 921, 5, 5618, '115213Vi29411', null, 1294.2529, 124.2483, 38.8276, 1457.3288, '2022-01-01'); 


-- downgrade: 
delete from sales.salesorderheader
where salesorderid in (75124);
