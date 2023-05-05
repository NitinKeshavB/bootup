{% snapshot snp_scrapreason_v2 %}

{{
    config(
        target_schema='production',
        strategy='check',
        unique_key='scrapreasonid',
        check_cols='all'
    )
}}

select * from {{ source('production', 'scrapreason')}}

{% endsnapshot %}
