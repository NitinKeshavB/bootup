{% snapshot dim_department %}

{{
    config(
      target_database='hr',
      target_schema='model',
      unique_key='dept_no',

      strategy='timestamp',
      updated_at='updated_at',
    )
}}

select * from {{ ref('departments') }}

{% endsnapshot %}