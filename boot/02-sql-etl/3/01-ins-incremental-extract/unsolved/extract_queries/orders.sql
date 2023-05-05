select 
    orderid, 
    orderdate,
    customerid, 
    netamount,
    tax, 
    totalamount
from 
    {{ source_table }}
