{% set config = {
    "extract_type": "incremental", 
    "incremental_column": "payment_date"
} %}

select 
    payment_id, 
    customer_id, 
    staff_id, 
    rental_id, 
    amount,
    payment_date 
from 
    {{ source_table }}

{% if is_incremental %}
    where payment_date > '{{ incremental_value }}'
{% endif %}
