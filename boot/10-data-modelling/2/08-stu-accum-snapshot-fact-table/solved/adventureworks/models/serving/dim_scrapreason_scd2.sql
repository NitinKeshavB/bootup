with snp_scrapreason as (
    select
        {{ dbt_utils.surrogate_key(['scrapreasonid', 'dbt_valid_from', 'dbt_valid_to']) }} as scrapreason_key 
        , scrapreasonid 
        , name 
    from {{ ref('snp_scrapreason') }}
) 

select * 
from snp_scrapreason
