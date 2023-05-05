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

, snp_scrapreason as ( 
    select *
    from {{ ref('snp_scrapreason') }}
)

, final as (
    select 
        row_number() over (partition by workorder.workorderid order by workorder.modifieddate desc) as latest_row
        , workorder.workorderid
        , workorder.productid
        , workorder.orderqty
        , workorder.scrappedqty
        , workorder.startdate
        , workorder.enddate
        , workorder.duedate
        , workorder.modifieddate
        , workorder.scrapreasonid
        , snp_scrapreason.dbt_valid_from
        , snp_scrapreason.dbt_valid_to
    from workorder 
    left join snp_scrapreason on workorder.scrapreasonid = snp_scrapreason.scrapreasonid
        and workorder.modifieddate between snp_scrapreason.dbt_valid_from and coalesce(snp_scrapreason.dbt_valid_to, '2999-01-01')
)

select 
    {{ dbt_utils.surrogate_key(['workorderid']) }} as workorder_key
    , {{ dbt_utils.surrogate_key(['productid']) }} as product_key 
    , case when scrapreasonid is null then null 
        else {{ dbt_utils.surrogate_key(['scrapreasonid', 'dbt_valid_from', 'dbt_valid_to']) }}
    end as scrapreason_key  
    , {{ dbt_utils.surrogate_key(['startdate']) }} as start_date_key
    , {{ dbt_utils.surrogate_key(['enddate']) }} as end_date_key
    , {{ dbt_utils.surrogate_key(['duedate']) }} as due_date_key
    , workorderid
    , orderqty
    , scrappedqty
from final 
where latest_row = 1 
