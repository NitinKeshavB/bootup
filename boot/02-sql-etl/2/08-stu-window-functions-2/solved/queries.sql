-- 1. calculate the cumulative sum of sales by month for each payment 

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


-- 2. for each film, show the most popular film in each category based on the number of rentals 
with films as (
	select 
		f.film_id, 
		f.title,
		c.category_id, 
		c.name as category_name, 
		count(r.*) rental_count
	from 
		film f inner join film_category fc 
			on f.film_id = fc.film_id 
		inner join category as c 
			on c.category_id = fc.category_id 
		inner join inventory i 
			on i.film_id = f.film_id 
		inner join rental r 
			on r.inventory_id = i.inventory_id 
	group by 
		f.film_id, 
		f.title,
		c.category_id, 
		c.name as category_name, 
)

select 
	film_id, 
	title,
	category_name, 
	last_value(title) over (
		partition by category_id 
		order by rental_count
		rows between unbounded preceding and unbounded following 
		-- we need to specify unbounded preceding and following because the frame_end defaults to the current row 
	) most_popular_film_in_category
from 
	films 
order by category_name 
