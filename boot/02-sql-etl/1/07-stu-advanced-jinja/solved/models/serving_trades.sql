drop table if exists {{ target_table }}; 

{% set exchange_list = engine.execute("select exchange_name from staging_exchange_codes") %}

create table {{ target_table }} as (
    select 
        id, 
        timestamp,  
        exchange_name,
        trade_price, 
        trade_size, 
        trade_conditions, 
        tape,
        {% for exchange in exchange_list %}
            case when exchange_name = '{{ exchange[0] }}' then 1 else 0 end as {{ exchange[0].replace(" ", "").replace(")","").replace("(","").lower() }}_flag
            {% if not loop.last %}
                , 
            {% endif %}
        {% endfor %}
    from 
        staging_trades st inner join staging_exchange_codes sec 
        on st.exchange = sec.exchange_code
)