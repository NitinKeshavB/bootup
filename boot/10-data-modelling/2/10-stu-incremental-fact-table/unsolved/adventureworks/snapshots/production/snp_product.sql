{% snapshot snp_product %}

{{
    config(
        target_schema='production',
        strategy='timestamp',
        unique_key='productid',
        updated_at='modifieddate',
    )
}}

select * from {{ source('production', 'product')}}

{% endsnapshot %}