-- 1. rank staff based on total_sales. Display total_sales, total_rentals, avg_sale_per_rental 
-- business context: we would like to provide highest performing staff with rewards 

with total_sales as (
	select
		s.staff_id, 
		sum(p.amount) as sales
	from 
		staff as s inner join payment as p 
			on s.staff_id = p.staff_id 
	group by 
		s.staff_id 
), 
total_rentals as (
	select
		s.staff_id, 
		count(r.*) as rentals 
	from 
		staff as s inner join rental as r 
			on s.staff_id = r.staff_id 
	group by 
		s.staff_id 
)

select 
	s.first_name, 
	s.last_name, 
	ts.sales as total_sales, 
	tr.rentals as total_rentals, 
	round(ts.sales/nullif(tr.rentals,0),2) as avg_sale_per_rental
from
	staff as s inner join total_sales as ts 
		on s.staff_id = ts.staff_id 
	inner join total_rentals as tr 
		on s.staff_id = tr.staff_id 
order by total_sales desc 


-- 2. get the top 10 city's total sales, and the city's total sales as a percentage of country's total sales 
-- business context: we would like to know the top performing cities and how much % revenue they make as compared to the rest of the city's country 
with address_sales as (
	select 
		c.address_id, 
		sum(p.amount) as sales 
	from 
		payment p inner join customer c 
			on p.customer_id = c.customer_id 
	group by 
		c.address_id 
), 		
city_sales as (
	select 
		c.city_id, 
		c.city, 
		c.country_id, 
		sum(ads.sales) sales 
	from 
		city c inner join address ad
			on c.city_id = ad.city_id 
		inner join address_sales ads 
			on ad.address_id = ads.address_id
	group by 
		c.city_id, c.country_id 
), 
country_sales as (
	select 
		c.country_id,
		c.country, 
		sum(cs.sales) as sales
	from 
		country c inner join city_sales cs 
			on c.country_id = cs.country_id 
	group by 
		c.country_id 
)

select 
	cis.city as city_name, 
	cos.country as country_name, 
	cis.sales as city_sales, 
    cos.sales as country_sales, 
	round(cis.sales / nullif(cos.sales, 0), 2) as city_percentage_of_country 
from 
	city_sales cis inner join country_sales cos 
		on cis.country_id = cos.country_id 
order by city_sales desc 
limit 10 

