{% snapshot dim_employee %}

{{
    config(
      target_database='hr',
      target_schema='model',
      unique_key='emp_no',

      strategy='timestamp',
      updated_at='updated_at',
    )
}}

select * from {{ source('hr', 'employees') }}

{% endsnapshot %}