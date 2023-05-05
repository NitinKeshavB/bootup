-- 1. Compare each film's length to the avg_yearly_length and avg_category_length 

with films as (
	select 
		f.film_id, 
		f.title, 
		f.release_year, 
		f.length, 
		c.category_id, 
		c.name as category_name
	from 
		film f inner join film_category fc 
			on f.film_id = fc.film_id 
		inner join category c 
			on fc.category_id = c.category_id 
), release_year_length as (
	select 
		release_year, 
		round(avg(length),2) length 
	from 
		films 
	group by release_year 
), 
category_length as (
	select 
		category_id, 
		round(avg(length),2) length 
	from 
		films 
	group by category_id 
)

select 
	f.film_id,
	f.title,
	f.release_year, 
	f.category_name,
	f.length, 
	ryl.length as release_year_length, 
	cl.length as category_length
from 
	films f inner join release_year_length ryl  
		on f.release_year = ryl.release_year 
	inner join category_length cl 
		on f.category_id = cl.category_id 
order by f.film_id

-- 2. now do the same thing using window functions 

with films as (
	select 
		f.film_id, 
		f.title, 
		f.release_year, 
		f.length, 
		c.category_id, 
		c.name as category_name
	from 
		film f inner join film_category fc 
			on f.film_id = fc.film_id 
		inner join category c 
			on fc.category_id = c.category_id 
) 
select 
	f.film_id,
	f.title,
	f.release_year, 
	f.category_name,
	f.length, 
	round(avg(f.length) over (partition by f.release_year), 2) as release_year_length,
	round(avg(f.length) over (partition by f.category_id), 2) as category_length
from films f 
order by film_id

-- 3. find each film's length rank within its category 

with films as (
	select 
		f.film_id, 
		f.title, 
		f.release_year, 
		f.length, 
		c.category_id, 
		c.name as category_name
	from 
		film f inner join film_category fc 
			on f.film_id = fc.film_id 
		inner join category c 
			on fc.category_id = c.category_id 
) 
select 
	f.film_id,
	f.title,
	f.release_year, 
	f.category_name,
	f.length, 
	round(avg(f.length) over (partition by f.release_year), 2) as release_year_length,
	round(avg(f.length) over (partition by f.category_id), 2) as category_length,
	rank() over (partition by f.category_id order by f.length desc) as length_rank_by_category
from films f 
order by film_id

-- 4. find each film's longest length within its category 

with films as (
	select 
		f.film_id, 
		f.title, 
		f.release_year, 
		f.length, 
		c.category_id, 
		c.name as category_name
	from 
		film f inner join film_category fc 
			on f.film_id = fc.film_id 
		inner join category c 
			on fc.category_id = c.category_id 
) 
select 
	f.film_id,
	f.title,
	f.release_year, 
	f.category_name,
	f.length, 
	round(avg(f.length) over (partition by f.release_year), 2) as release_year_length,
	round(avg(f.length) over (partition by f.category_id), 2) as category_length,
	rank() over (partition by f.category_id order by f.length desc) as length_rank_by_category,
	max(f.length) over (partition by f.category_id) as max_length_by_category
from films f 
order by film_id

