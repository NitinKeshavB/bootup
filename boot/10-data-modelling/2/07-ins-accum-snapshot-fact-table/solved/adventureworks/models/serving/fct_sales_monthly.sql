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
    from {{ref('stg_salesorderdetail')}}
)

, dates as (
    select * from {{ ref('dim_date') }}
)

, transform as (
    select 
        dates.month_end_date as order_month_end_date
        , order_status
        , sum(salesorderdetail.orderqty) as orderqty
        , sum(salesorderdetail.revenue_wo_taxandfreight) as revenue_wo_taxandfreight
    from salesorderdetail
    left join salesorderheader on salesorderdetail.salesorderid = salesorderheader.salesorderid
    left join dates on salesorderheader.orderdate = dates.date_day
    group by 
        order_status
        , dates.month_end_date
)

, final as (
    select
        
        {{ dbt_utils.surrogate_key(['order_month_end_date']) }} as order_date_key
        , {{ dbt_utils.surrogate_key(['order_status']) }} as order_status_key
        , orderqty
        , revenue_wo_taxandfreight
    from transform
)

select *
from final
