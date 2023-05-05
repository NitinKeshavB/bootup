-- 1. compute a cumulative sum 
-- calculate the cumulative sum of sales for each payment 

select 
	payment_id, 
	payment_date, 
	concat(extract(year from payment_date), '-', extract(month from payment_date)) as payment_year_month,
	amount, 
	sum(amount) over (
		partition by concat(extract(year from payment_date), '-', extract(month from payment_date)) 
		order by payment_date asc 
		rows between unbounded preceding and current row -- (optional) this is optional because this is the default behaviour 
	) as cumulative_sales
from payment 
order by payment_date asc


-- 2. get the most popular item in each category : 
-- for each customer, show the most highest spending customer in each country based on the sales amount
with customer_sales as (
	select 
		c.customer_id,
		c.first_name,
		c.last_name,
		concat(c.first_name, ' ', c.last_name) as full_name, 
		co.country_id,
		co.country,
		sum(p.amount) sales
	from 
		customer c inner join payment p 
			on c.customer_id = p.customer_id  
		left join address a 
			on c.address_id = a.address_id 
		inner join city ci
			on ci.city_id = a.city_id 
		inner join country co 
			on co.country_id = ci.country_id 
	group by 
		c.customer_id,
		c.first_name,
		c.last_name,
		full_name,
		co.country_id,
		co.country
)

select 
	customer_id,
	full_name,
	sales,
	country, 
	last_value(full_name) over (
		partition by country_id
		order by sales desc 
		rows between unbounded preceding and unbounded following 
	) as highest_spending_customer_in_country
from customer_sales 
order by country 
