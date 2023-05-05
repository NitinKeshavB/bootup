with workorder as (
    select 
        workorderid
        , productid
        , orderqty
        , scrappedqty
        , date(startdate) as startdate
        , date(enddate) as enddate
        , date(duedate) as duedate
        , date(modifieddate) as modifieddate
        , scrapreasonid
    from {{ ref('stg_workorder') }}
)

, transform as (
    select 
        dim_date.month_end_date
        , workorder.productid
        , count(workorderid) workorderqty
        , sum(orderqty) orderqty
        , sum(scrappedqty) scrappedqty
    from workorder
    left join serving.dim_date on workorder.modifieddate = dim_date.date_day 
    group by 
        dim_date.month_end_date,
        workorder.productid
)

select 
    {{ dbt_utils.surrogate_key(['productid', 'month_end_date']) }} as workorder_monthly_key 
    , {{ dbt_utils.surrogate_key(['month_end_date']) }} as month_date_key 
    , {{ dbt_utils.surrogate_key(['productid']) }} as product_key 
    , workorderqty
    , orderqty
    , scrappedqty
from transform 
