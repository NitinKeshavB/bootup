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
        i as id, 
        to_timestamp(t, 'YYYY-MM-DDTHH:MI:SS') as timestamp, 
        x as exchange, 
        p as trade_price, 
        s as trade_size, 
        c as trade_conditions, 
        z as tape
    from 
        raw_trades
    {% if table_exists %}
    where 
        to_timestamp(t, 'YYYY-MM-DDTHH:MI:SS') > '{{ max_timestamp }}'
    {% endif %}
); 