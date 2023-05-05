{% set config = {
    "extract_type": "incremental", 
    "incremental_column": "last_update"
} %}

select 
    inventory_id, 
    film_id,
    store_id, 
    last_update 
from 
    {{ source_table }}

{% if is_incremental %}
    where last_update > '{{ incremental_value }}'
{% endif %}
