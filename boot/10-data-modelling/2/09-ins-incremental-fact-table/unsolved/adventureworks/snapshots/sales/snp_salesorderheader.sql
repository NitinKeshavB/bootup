{% snapshot snp_salesorderheader %}

{{
    config(
        target_schema='sales',
        strategy='timestamp',
        unique_key='salesorderid',
        updated_at='modifieddate',
    )
}}

select * from {{ source('sales', 'salesorderheader')}}

{% endsnapshot %}
