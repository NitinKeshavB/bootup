with snp_product as (
    select *
    from {{ref('snp_product')}}
)

, stg_product_subcategory as (
    select * 
    from {{ ref('stg_productsubcategory')}}
)

, stg_product_category as (
    select * 
    from {{ ref('stg_productcategory')}}
)
 

, transformed as (
    select 
        {{ dbt_utils.surrogate_key(['snp_product.productid', 'dbt_valid_from', 'dbt_valid_to']) }} as product_key -- auto-incremental surrogate key
        , snp_product.productid
        , snp_product.name 
        , snp_product.productnumber
        , snp_product.color
        , snp_product.class
        , stg_product_subcategory.name as product_subcategory_name
        , stg_product_category.name as product_category_name
        , dbt_valid_from
        , dbt_valid_to
    from snp_product 
    left join stg_product_subcategory on snp_product.productsubcategoryid = stg_product_subcategory.productsubcategoryid
    left join stg_product_category on stg_product_subcategory.productcategoryid = stg_product_category.productcategoryid
)

select *
from transformed
