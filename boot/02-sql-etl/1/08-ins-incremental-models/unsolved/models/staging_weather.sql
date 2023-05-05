drop table if exists {{ target_table }}; 

create table {{ target_table }} as (
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
); 
