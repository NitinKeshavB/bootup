# Instruction

Jane the HR gave you a CSV file containing a mapping of `dept_no` and the actual department names. This makes department related report more readable.

She also asks if there's a way to demonstrate the reliability of the data, as many reports go to C-levels.

## Concept
### Seeds

- Seeds are CSV files
- Seeds can be referenced using `ref()` just like other tables
- Seeds are version controlled because it sits in you code base
- Use it for small mapping data that changes infrequently, or extra data needed for a quick scratch analysis

Run `dbt seed` to take effect

Seed can be configured as well. Some common ones including:
- quote_columns
- column_types
- the general configs also apply

## Task
`dbt seed --full-refresh`

## Concept
### Tests
- Tests are `select` queries that seeks to grab failing/erroneous/wrong records
- Zero rows is pass
- Two major types of tests
  - Singular tests
  - Generic tests

#### Singular tests
- SQL file that contains a `select` query. Just like the vanilla definition of tests.
- File name = test name

e.g. if `total_amount` less than zero, then fail
```
select
    order_id,
    sum(amount) as total_amount
from {{ ref('fct_payments' )}}
group by 1
having not(total_amount >= 0)
```
#### Generic tests
Tests that take parameters, which makes them generic.

e.g. if a column is null, then fail
```
{% test not_null(model, column_name) %}

    select *
    from {{ model }}
    where {{ column_name }} is null

{% endtest %}
```
There are four generic tests come with dbt installation:
- unique
- not_null
- accepted_values
- relationships (referential integrity)

e.g.
```
version: 2

models:
  - name: orders
    columns:
      - name: order_id
        tests:
          - unique
          - not_null
      - name: status
        tests:
          - accepted_values:
              values: ['placed', 'shipped', 'completed', 'returned']
      - name: customer_id
        tests:
          - relationships:
              to: ref('customers')
              field: id
```

### Config and Properties
At this stage, you are probably confused about these yml files.

Basically all resources in dbt can be declared in yml files. e.g. sources, models, seeds etc.

These resources have properties that describe how they are. Some properties are dedicated for a certain type of resource.
And some properties are general to all:
- columns
- config
- description
- docs
- quote
- tests

Config property is a special one among other properties. Because configs can be set at different places, they are applied hierarchically. Or in other words, configs can be inherited or overwritten.

Similar to properties there are some specialised configs and there are some general ones.

[Ref: different configs and properties](https://docs.getdbt.com/reference/configs-and-properties)

## Task
`dbt test --select avg_salary_for_senoirs_by_tenure2`

## Concept
### Jinja

Jinja and Macros are what makes SQL scripts programmable.

You have already used Jinja e.g. `{{ ref() }}`, `{{ source() }}` and `{{ this }}`.

e.g.
```
{% set payment_methods = ["bank_transfer", "credit_card", "gift_card"] %}
select
    order_id,
    {% for payment_method in payment_methods %}
    sum(case when payment_method = '{{payment_method}}' then amount end) as {{payment_method}}_amount,
    {% endfor %}
    sum(amount) as total_amount
from app_data.payments
group by 1
```
compiles into

```
select
    order_id,
    sum(case when payment_method = 'bank_transfer' then amount end) as bank_transfer_amount,
    sum(case when payment_method = 'credit_card' then amount end) as credit_card_amount,
    sum(case when payment_method = 'gift_card' then amount end) as gift_card_amount,
    sum(amount) as total_amount
from app_data.payments
group by 1
```
Be mindful that overusing Jinja will make readability awful.

[Ref: dbt Jinja](https://docs.getdbt.com/reference/dbt-jinja-functions)

### Macros
Macros are like functions in other programming languages. The generic test we just wrote is somewhat like a marco.

e.g.
defining a macro
```
{% macro cents_to_dollars(column_name, precision=2) %}
    ({{ column_name }} / 100)::numeric(16, {{ precision }})
{% endmacro %}
```
using a marco
```
select
  id as payment_id,
  {{ cents_to_dollars('amount') }} as amount_usd,
  ...
from app_data.payments

```
this will be compiled to
```
select
  id as payment_id,
  (amount / 100)::numeric(16, 2) as amount_usd,
  ...
from app_data.payments
```

### Packages

Why write your own, when you just need to import macros from packages written by others?
Get the best code from the community!

1. find a package from https://hub.getdbt.com/
2. put install info in `packages.yml`, the same level as `dbt_project.yml`
3. run `dbt deps`

One popular package is [dbt_utils](https://hub.getdbt.com/dbt-labs/dbt_utils/latest/)

You can also import another dbt project of yours in the same repo.
