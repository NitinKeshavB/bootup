{% set config = {
    "extract_type": "incremental", 
    "incremental_column": "orderdate",
    "key_columns": ["orderid"]
} %}

select 
    orderid, 
    orderdate,
    customerid, 
    netamount,
    tax, 
    totalamount
from 
    {{ source_table }}

{% if is_incremental %}
    where orderdate > '{{ incremental_value }}'
{% endif %}
