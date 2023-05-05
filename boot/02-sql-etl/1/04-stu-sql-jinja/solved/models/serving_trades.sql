drop table if exists {{ target_table }}; 

create table {{ target_table }} as (
    select 
        id, 
        timestamp,  
        exchange_name,
        trade_price, 
        trade_size, 
        trade_conditions, 
        tape
    from 
        staging_trades st inner join staging_exchange_codes sec 
        on st.exchange = sec.exchange_code
)