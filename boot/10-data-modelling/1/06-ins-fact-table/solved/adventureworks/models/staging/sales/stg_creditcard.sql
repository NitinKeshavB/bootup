with source_data as (
    select
        creditcardid
        , cardtype
        , expyear
        , modifieddate
        , expmonth
        , cardnumber
    from {{ source('sales', 'creditcard') }}
)
select *
from source_data