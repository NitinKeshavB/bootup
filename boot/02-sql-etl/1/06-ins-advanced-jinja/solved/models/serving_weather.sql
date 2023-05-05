drop table if exists {{ target_table }}; 

{% set list_of_weather = engine.execute("select distinct weather_main from staging_weather") %}

create table {{ target_table }} as (
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
); 