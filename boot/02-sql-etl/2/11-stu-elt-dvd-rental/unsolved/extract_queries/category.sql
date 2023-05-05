select 
    category_id,
    name,
    last_update
from 
    {{ source_table }} 