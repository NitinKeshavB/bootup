-- 1. top 10 actors with most number of films 
select 
	concat(a.first_name, ' ', a.last_name) as actor_name, 
	count(f.*) as number_films 
from 
	actor as a 
	inner join film_actor as fa 
		on a.actor_id = fa.actor_id 
	inner join film as f 
		on f.film_id = fa.film_id 
group by 
	actor_name
order by 
	number_films desc 
limit 10 

-- 2. display the number of films found in store 1 but not in store 2 
select 
	count(distinct(film_id)) 
from inventory 
where store_id = 1 and film_id not in (
	select
		distinct(film_id) 
	from inventory 
	where store_id = 2 
)
