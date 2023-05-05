{% set exchange_list = engine.execute("select exchange_name from staging_exchange_codes") %}

{% set table_exists = engine.execute("select exists (select from pg_tables where tablename = '" + target_table + "')").first()[0] %}

{% if not table_exists %}
    drop table if exists {{ target_table }}; 
{% else %}
    {% set max_timestamp = engine.execute("select max(timestamp) from " + target_table).first()[0] %}
{% endif %}

{% if not table_exists %}
    create table {{ target_table }} as 
{% else %}
    insert into {{ target_table }}
{% endif %}
(
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
    {% if table_exists %}
    where 
        timestamp > '{{ max_timestamp }}'
    {% endif %}
)