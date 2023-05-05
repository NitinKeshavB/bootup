{% set table_exists = engine.execute("select exists (select from pg_tables where tablename = '" + target_table + "')").first()[0] %}

{% set list_of_weather = engine.execute("select distinct weather_main from staging_weather") %}


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
        datetime, 
        id, 
        name, 
        lon,
        lat,
        weather_main,
        weather_description,
        base, 
        temperature,
        pressure,
        humidity,
        clouds,
        {% for weather in list_of_weather -%}
            case when weather_main = '{{ weather[0] }}' then 1 else 0 end as {{ weather[0].lower() }}_flag
            {%- if not loop.last -%}
                , 
            {%- endif %}
        {% endfor %}
    from 
        staging_weather
    {% if table_exists %}
    where 
        datetime > '{{ max_datetime }}'
    {% endif %}
); 