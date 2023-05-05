drop table if exists {{ target_table }}; 

create table {{ target_table }} as (
    select 
        c.firstname, 
        c.lastname, 
        sum(o.netamount::numeric) as sales 
    from 
        staging_orders o inner join staging_customers c 
            on o.customerid = c.customerid
    group by 
        c.firstname, 
        c.lastname
    order by sales desc 
    limit 100 
);