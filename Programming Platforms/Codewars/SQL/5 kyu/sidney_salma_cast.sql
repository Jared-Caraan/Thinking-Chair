'''
Given film_actor and film tables from the DVD Rental sample database find all movies both Sidney Crowe (actor_id = 105) and Salma Nolte (actor_id = 122) cast in together and order the result set alphabetically.

film schema
Column      | Type                        | Modifiers
------------+-----------------------------+----------
title       | character varying(255)      | not null
film_id     | smallint                    | not null
  
film_actor schema
Column      | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | smallint                    | not null
film_id     | smallint                    | not null
last_update | timestamp without time zone | not null
  
actor schema
Column      | Type                        | Modifiers
------------+-----------------------------+----------
actor_id    | integer                     | not null 
first_name  | character varying(45)       | not null
last_name   | character varying(45)       | not null
last_update | timestamp without time zone | not null 

The desired output:

title
-------------
Film Title 1
Film Title 2
...
title - Film title
'''
with cte1 as (
  select f.title, f.film_id, fa.actor_id, row_number() over (partition by f.film_id) as row_num
  from film f
  left join film_actor fa
  on f.film_id = fa.film_id
  WHERE fa.actor_id = 105 OR fa.actor_id = 122
)
select title
from cte1
where row_num = 2
order by 1;

-- Clever
SELECT f.title
FROM film f
JOIN film_actor fa on fa.film_id = f.film_id
WHERE fa.actor_id IN (105,122)
GROUP BY f.film_id
HAVING COUNT(*) = 2
ORDER BY f.title ASC
