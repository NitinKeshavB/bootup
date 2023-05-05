with stg_address as (
    select *
    from {{ref('stg_address')}}
)

, stg_stateprovince as (
    select *
    from {{ref('stg_stateprovince')}}
)

, stg_countryregion as (
    select *
    from {{ref('stg_countryregion')}}
)

, transformed as (
    -- TODO 
)

select *
from transformed
