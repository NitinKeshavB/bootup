drop table if exists {{ target_table }}; 

create table {{ target_table }} as (
    select * from orders
);