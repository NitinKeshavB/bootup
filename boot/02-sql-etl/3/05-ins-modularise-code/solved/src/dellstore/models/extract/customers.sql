{% set config = {
    "extract_type": "full"
} %}

select 
    customerid, 
    firstname,
    lastname, 
    address1,
    address2, 
    city,
    state,
    country,
    region, 
    email, 
    phone,
    age,
    income,
    gender
from 
    {{ source_table }}

