{% snapshot snp_purchaseorderheader %}

{{
    config(
        target_schema='purchasing',
        strategy='timestamp',
        unique_key='purchaseorderid',
        updated_at='modifieddate',
    )
}}

select * from {{ source('purchasing', 'purchaseorderheader')}}

{% endsnapshot %}
