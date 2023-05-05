{{
    config(
        materialized='incremental',
        unique_key='sales_key',
        on_schema_change='fail'
    )
}}
with salesorderheader as (
    select
        salesorderid
        , customerid
        , creditcardid
        , shiptoaddressid
        , order_status
        , date(stg_salesorderheader.orderdate) orderdate
    from {{ ref('stg_salesorderheader') }} 
)

, salesorderdetail as (
    select
        salesorderid
        , salesorderdetailid
        , productid
        , orderqty
        , unitprice
        , unitprice * orderqty  as  revenue_wo_taxandfreight
        , modifieddate
    from {{ref('stg_salesorderdetail')}}
)

/* We then join salesorderdetail and salesorderheader to get the final fact table*/
, final as (
    select
        {{ dbt_utils.surrogate_key(['salesorderdetail.salesorderid', 'salesorderdetailid'])  }} sales_key
        , {{ dbt_utils.surrogate_key(['productid']) }} as product_key
        , {{ dbt_utils.surrogate_key(['customerid']) }} as customer_key 
        , {{ dbt_utils.surrogate_key(['creditcardid']) }} as creditcard_key
        , {{ dbt_utils.surrogate_key(['shiptoaddressid']) }} as ship_address_key
        , {{ dbt_utils.surrogate_key(['order_status']) }} as order_status_key
        , {{ dbt_utils.surrogate_key(['orderdate']) }} as order_date_key
        , salesorderdetail.salesorderid
        , salesorderdetail.salesorderdetailid
        , salesorderdetail.unitprice
        , salesorderdetail.orderqty
        , salesorderdetail.revenue_wo_taxandfreight
        , salesorderdetail.modifieddate
    from salesorderdetail
    left join salesorderheader on salesorderdetail.salesorderid = salesorderheader.salesorderid
)

select *
from final
{% if is_incremental() %}
    where modifieddate > (select max(modifieddate) from {{ this }})
{% endif %}
