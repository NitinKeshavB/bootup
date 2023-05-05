-- 1. show the top 10 customers based on average amount spent per rental, and their total_rental and total_amount_spent figures 
-- note: same query as Q4 of the previous activity. You will need to refactor the existing query using CTEs. 

with amount_spent as (
	select 
		c.customer_id, 
		count(r.*) as number_of_rentals 
	from 
		rental as r inner join customer as c 
			on r.customer_id = c.customer_id 
	group by 
		c.customer_id 
), 
number_rentals as (
	select 
		c.customer_id, 
		sum(p.amount) as amount_spent
	from 
		payment as p inner join customer as c 
			on p.customer_id = c.customer_id 
	group by 
		c.customer_id
) 
 
select 
	c.first_name,
	c.last_name, 
	round(amount_spent/nullif(number_of_rentals,0),2) as avg_spent_per_rental, 
	amount_spent,
	number_of_rentals
from 
	customer as c inner join number_rentals as nr 
		on c.customer_id = nr.customer_id 
	inner join amount_spent as amt 
		on c.customer_id = amt.customer_id 
order by avg_spent_per_rental desc 
limit 10 


