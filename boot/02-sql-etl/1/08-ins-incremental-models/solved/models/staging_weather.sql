{% set table_exists = engine.execute("select exists (select from pg_tables where tablename = '" + target_table + "')").first()[0] %}

{% if not table_exists %}
    drop table if exists {{ target_table }}; 
{% else %}
    {% set max_datetime = engine.execute("select max(datetime) from " + target_table).first()[0] %}
{% endif %}

{% if not table_exists %}
    create table {{ target_table }} as 
{% else %}
    insert into {{ target_table }}
{% endif %}
(
    select 
        to_timestamp(dt) as datetime, 
        id, 
        name, 
        cast(coord ->> 'lon' as numeric) as lon,
        cast(coord ->> 'lat' as numeric) as lat,
        weather -> 0 ->> 'main' as weather_main,
        weather -> 0 ->> 'description' as weather_description,
        base, 
        cast(main ->> 'temp' as numeric) as temperature,
        cast(main ->> 'pressure' as numeric) as pressure,
        cast(main ->> 'humidity' as numeric) as humidity,
        cast(clouds ->> 'all' as numeric) as clouds
    from raw_weather
    {% if table_exists %}
    where 
        to_timestamp(dt) > '{{ max_datetime }}'
    {% endif %}
); 
