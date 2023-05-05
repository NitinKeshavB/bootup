drop table if exists {{ target_table }}; 

create table {{ target_table }} as (
    select 
        exchange_code, 
        exchange_name
    from 
        raw_exchange_codes
); 