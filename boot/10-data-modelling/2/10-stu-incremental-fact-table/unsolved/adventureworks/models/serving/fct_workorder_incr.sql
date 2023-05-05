{{
    config(
        materialized='incremental',
        unique_key='workorder_key',
        on_schema_change='fail'
    )
}}

with workorder as (
    select 
        workorderid
        , productid
        , orderqty
        , scrappedqty
        , date(startdate) as startdate
        , date(enddate) as enddate
        , date(duedate) as duedate
        , scrapreasonid
        , modifieddate
    from {{ ref('stg_workorder') }}
)
, transform as (
    select 
        {{ dbt_utils.surrogate_key(['workorderid']) }} as workorder_key
        , {{ dbt_utils.surrogate_key(['productid']) }} as product_key 
        , case when scrapreasonid is null then null 
            else {{ dbt_utils.surrogate_key(['scrapreasonid']) }} 
        end as scrapreason_key 
        , {{ dbt_utils.surrogate_key(['startdate']) }} as start_date_key
        , {{ dbt_utils.surrogate_key(['enddate']) }} as end_date_key
        , {{ dbt_utils.surrogate_key(['duedate']) }} as due_date_key
        , workorderid
        , orderqty
        , scrappedqty
        , modifieddate
    from workorder    
)

select 
    workorder_key
    , product_key 
    , scrapreason_key 
    , start_date_key
    , end_date_key
    , due_date_key
    , workorderid
    , orderqty
    , scrappedqty
    , modifieddate -- used for incremental load 
from transform
{% if is_incremental() %}
    where modifieddate > (select max(modifieddate) from {{ this }})
{% endif %}
