with stg_purchaseorderheader as (
    select
        purchaseorderid
        , revisionnumber
        , status
        , employeeid
        , vendorid
        , shipmethodid
        , date(orderdate) as orderdate
        , date(shipdate) as shipdate 
        , subtotal
        , taxamt
        , freight
    from {{ ref('stg_purchaseorderheader') }}
)

-- crosstab does not work with CTEs, therefore exact table names must be used 
, purchaseorderheader_pivot as ( 
    select * 
    from crosstab(
        'select purchaseorderid, status, modifieddate from purchasing.snp_purchaseorderheader',
        $$VALUES (1), (2), (3), (4)$$
    ) as ct(
        "purchaseorderid" int,
        "pending_date" date,
        "approved_date" date,
        "rejected_date" date,
        "complete_date" date
    ) 
)

, transform as (
    select 
        purchaseorderheader_pivot.purchaseorderid
        , revisionnumber
        , employeeid
        , vendorid
        , shipmethodid
        , orderdate
        , shipdate 
        , status
        , subtotal
        , taxamt
        , freight 
        , pending_date
        , approved_date
        , rejected_date
        , complete_date
        , case 
            when date_part('day', approved_date::timestamp - pending_date::timestamp) > 0 
            then date_part('day', approved_date::timestamp - pending_date::timestamp) 
            else 0 
        end as days_reviewing
        , case 
            when date_part('day', complete_date::timestamp - approved_date::timestamp) > 0 
            then date_part('day', complete_date::timestamp - approved_date::timestamp) 
            else 0 
        end as days_completing
        , case 
            when date_part('day', rejected_date::timestamp - pending_date::timestamp) > 0 
            then date_part('day', rejected_date::timestamp - pending_date::timestamp) 
            else 0 
        end as days_rejecting
    from purchaseorderheader_pivot 
    left join stg_purchaseorderheader on purchaseorderheader_pivot.purchaseorderid = stg_purchaseorderheader.purchaseorderid 
)

select 
    {{ dbt_utils.surrogate_key(['purchaseorderid']) }} as purchaseorderheader_key
    , purchaseorderid
    , revisionnumber
    , {{ dbt_utils.surrogate_key(['employeeid']) }} as employee_key 
    , {{ dbt_utils.surrogate_key(['vendorid']) }}  as vendor_key
    , {{ dbt_utils.surrogate_key(['shipmethodid']) }} as ship_method_key
    , {{ dbt_utils.surrogate_key(['status']) }} as purchase_status_key
    , {{ dbt_utils.surrogate_key(['orderdate']) }} as order_date_key 
    , {{ dbt_utils.surrogate_key(['shipdate']) }} as ship_date_key
    , {{ dbt_utils.surrogate_key(['pending_date']) }} as pending_date_key
    , {{ dbt_utils.surrogate_key(['approved_date']) }} as approved_date_key 
    , {{ dbt_utils.surrogate_key(['rejected_date']) }} as rejected_date_key
    , {{ dbt_utils.surrogate_key(['complete_date']) }} as complete_date_key
    , days_reviewing
    , days_completing
    , days_rejecting
    , subtotal
    , taxamt
    , freight 
from transform 
