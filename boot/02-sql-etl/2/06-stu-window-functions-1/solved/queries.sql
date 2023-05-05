-- 1. compare each customer's sales against the average city's sales, average country's sales, 
-- the customer's rank by sales, the customer's rank against city sales, the customer's rank against country sales

with customer_sales as (
	select 
		c.customer_id,
		c.first_name,
		c.last_name,
		ci.city_id, 
		ci.city, 
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
		ci.city_id, 
		ci.city, 
		co.country_id,
		co.country
)

select 
	customer_id, 
	first_name, 
	last_name, 
	city,
	country,
	sales, 
	round(avg(sales) over (partition by city_id),2) as avg_city_sales, 
	round(avg(sales) over (partition by country_id),2) as avg_country_sales, 
	rank() over (order by sales desc) as rank_customer_sales,
	rank() over (partition by city_id order by sales desc) as rank_city_sales,
	rank() over (partition by country_id order by sales desc) as rank_country_sales
from 
	customer_sales
order by customer_id 

-- 2. compare each film's rental sales to it's average category sales, average release year sales, 
-- the film's rank, the film's rank in its category, the film's rank in it's release year 

with film_sales as (
	select 
		f.film_id, 
		f.title,
		f.release_year, 
		c.category_id, 
		c.name as category_name,
		sum(p.amount) as sales 
	from 
		film f inner join film_category fc 
			on f.film_id = fc.film_id 
		inner join category as c 
			on c.category_id = fc.category_id 
		inner join inventory i 
			on i.film_id = f.film_id 
		inner join rental r 
			on r.inventory_id = i.inventory_id 
		inner join payment as p 
			on p.rental_id = r.rental_id 
	group by 
		f.film_id, c.category_id	 
)

select 
	film_id, 
	title, 
	release_year, 
	category_name, 
	sales, 
	avg(sales) over (partition by release_year) as avg_sales_by_release_year,
	avg(sales) over (partition by category_id) as avg_sales_by_category,
	rank() over (order by sales desc) as rank_sales, 
	rank() over (partition by release_year order by sales desc) as rank_sales_by_release_year, 
	rank() over (partition by category_id order by sales desc) as rank_sales_by_category
from
	film_sales 
order by film_id 
