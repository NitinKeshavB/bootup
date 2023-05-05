with stg_salesorderheader as (
    select
        salesorderid
        , revisionnumber
        , customerid
        , creditcardid
        , shiptoaddressid
        , order_status
        , date(orderdate) as orderdate
        , date(shipdate) as shipdate
        , subtotal 
        , taxamt 
        , freight 
        , totaldue 
    from {{ ref('stg_salesorderheader') }} 
)

, salesorderheader_pivot as ( 
    select * 
    from crosstab(
        'select salesorderid, status, modifieddate from sales.snp_salesorderheader',
        $$VALUES (1), (2), (3), (4), (5), (6)$$
    ) as ct(
        "salesorderid" int,
        "in_process_date" date,
        "approved_date" date,
        "backordered_date" date,
        "rejected_date" date,
        "shipped_date" date,
        "cancelled_date" date
    ) 
)

, transform as (
    select 
        salesorderheader_pivot.salesorderid
        , revisionnumber
        , customerid
        , creditcardid
        , shiptoaddressid
        , order_status
        , orderdate
        , shipdate
        , subtotal 
        , taxamt 
        , freight 
        , totaldue 
        , in_process_date
        , approved_date
        , backordered_date
        , rejected_date
        , shipped_date
        , cancelled_date
        , case 
            when date_part('day', approved_date::timestamp - in_process_date::timestamp) > 0 
            then date_part('day', approved_date::timestamp - in_process_date::timestamp) 
            else 0 
        end as days_to_process
        , case 
            when date_part('day', shipped_date::timestamp - approved_date::timestamp) > 0 
            then date_part('day', shipped_date::timestamp - approved_date::timestamp) 
            else 0 
        end as days_to_ship
        , case 
            when date_part('day', rejected_date::timestamp - in_process_date::timestamp) > 0 
            then date_part('day', rejected_date::timestamp - in_process_date::timestamp) 
            else 0 
        end as days_to_reject
    from salesorderheader_pivot 
    left join stg_salesorderheader on salesorderheader_pivot.salesorderid = stg_salesorderheader.salesorderid 
)


select
    {{ dbt_utils.surrogate_key(['salesorderid'])  }} salesorderheader_key
    , {{ dbt_utils.surrogate_key(['customerid']) }} as customer_key 
    , {{ dbt_utils.surrogate_key(['creditcardid']) }} as creditcard_key
    , {{ dbt_utils.surrogate_key(['shiptoaddressid']) }} as ship_address_key
    , {{ dbt_utils.surrogate_key(['order_status']) }} as order_status_key
    , {{ dbt_utils.surrogate_key(['orderdate']) }} as order_date_key
    , {{ dbt_utils.surrogate_key(['shipdate']) }} as ship_date_key
    , {{ dbt_utils.surrogate_key(['in_process_date']) }} as in_process_date_key
    , {{ dbt_utils.surrogate_key(['approved_date']) }} as approved_date_key
    , {{ dbt_utils.surrogate_key(['backordered_date']) }} as backordered_date_key
    , {{ dbt_utils.surrogate_key(['rejected_date']) }} as rejected_date_key
    , {{ dbt_utils.surrogate_key(['shipped_date']) }} as shipped_date_key
    , {{ dbt_utils.surrogate_key(['cancelled_date']) }} as cancelled_date_key
    , salesorderid
    , days_to_process
    , days_to_ship
    , days_to_reject
    , subtotal 
    , taxamt 
    , freight 
    , totaldue 
from transform

