{% set table_exists = engine.execute("select exists (select from pg_tables where tablename = '" + target_table + "')").first()[0] %}

{% if not table_exists %}
    drop table if exists {{ target_table }}; 
{% else %}
    {% set max_date = engine.execute("select max(date) from " + target_table).first()[0] %}
{% endif %}

{% if not table_exists %}
    create table {{ target_table }} as 
{% else %}
    insert into {{ target_table }}
{% endif %}
(
    select 
        exchange_name,
        timestamp::date as date, 
        round(sum(trade_size)::numeric, 2) as trade_size, 
        round(sum(trade_size * trade_price)::numeric, 2) as trade_value
    from 
        serving_trades
    {% if table_exists %}
    where 
        timestamp::date > '{{ max_date }}'
    {% endif %}
    group by 
        exchange_name, date
    order by 
        exchange_name, date
); 