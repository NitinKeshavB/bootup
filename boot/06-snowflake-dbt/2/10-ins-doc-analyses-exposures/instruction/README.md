# Instruction
You have done a great job to help DEC.com sorting out its data!

HR is so satisfied with you work that they have convinced the CEO to expand your team. They ask if you could produce a good documentation so that you can easily transfer the knowledge to new team members?

## Concept

### Analyses
Just like a model, but not materialised at all.

Run `dbt compile` and find your compiled SQL.

### Exposures
A way to document your downstream applications.
It can be defined anywhere in any `.yml` file. But for clarity, put exposures in a separate file, and maybe call it `exposure_xxx.yml`

Example:
```
exposures:
  
  - name: weekly_jaffle_metrics
    type: dashboard
    maturity: high
    url: https://bi.tool/dashboards/1
    description: >
      Did someone say "exponential growth"?
    
    depends_on:
      - ref('fct_orders')
      - ref('dim_customers')
      - source('gsheets', 'goals')
      
    owner:
      name: Claire from Data
      email: data@jaffleshop.com
```
Enable graph operation to fully refresh or test an application.

`dbt run -s +exposure:weekly_jaffle_metrics`

`dbt test -s +exposure:weekly_jaffle_metrics`

### Documentation
`dbt docs generate`

`dbt docs serve`

Lineage graph

Fill up your `descriptions`!
