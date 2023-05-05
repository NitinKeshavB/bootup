{% snapshot snp_scrapreason %}

{{
    config(
        target_schema='production',
        strategy='timestamp',
        unique_key='scrapreasonid',
        updated_at='modifieddate',
    )
}}

select * from {{ source('production', 'scrapreason')}}

{% endsnapshot %}