-- 1. what are the top 10 categories of films 
select
	c.name, 
	count(*) as number_of_films 
from 
	film as f 
	inner join film_category as fc 
		on f.film_id = fc.film_id
	inner join category as c 
		on fc.category_id = c.category_id 
group by 
	c.name
order by 
	number_of_films desc 
limit 10 

-- 2. who are the top 10 customers with the most number of rentals 
select 
	c.first_name, 
	c.last_name, 
	count(r.*) as number_of_rentals 
from 
	rental as r inner join customer as c 
		on r.customer_id = c.customer_id 
group by 
	c.first_name, 
	c.last_name
order by 
	number_of_rentals desc 
limit 10 

-- 3. who are the top 10 customers with the most amount spent 
select 
	c.first_name, 
	c.last_name, 
	sum(p.amount) as amount_spent
from 
	payment as p inner join customer as c 
		on p.customer_id = c.customer_id 
group by 
	c.first_name, 
	c.last_name
order by 
	amount_spent desc 
limit 10 

-- 4. show the top 10 customers based on average amount spent per rental, and their total_rental and total_amount_spent figures
select 
	customer.first_name,
	customer.last_name, 
	round(amount_spent/nullif(number_of_rentals,0),2) as avg_spent_per_rental, 
	amount_spent,
	number_of_rentals
from 
	customer inner join 
	(
		select 
			c.customer_id, 
			count(r.*) as number_of_rentals 
		from 
			rental as r inner join customer as c 
				on r.customer_id = c.customer_id 
		group by 
			c.customer_id 
	) as number_rentals 
		on customer.customer_id = number_rentals.customer_id 
	inner join 
	(
		select 
			c.customer_id, 
			sum(p.amount) as amount_spent
		from 
			payment as p inner join customer as c 
				on p.customer_id = c.customer_id 
		group by 
			c.customer_id
	) as amount_spent 
		on customer.customer_id = amount_spent.customer_id 
order by avg_spent_per_rental desc 
limit 10 	


