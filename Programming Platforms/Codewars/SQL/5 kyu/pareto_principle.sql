'''
In the task, you need to calculate whether a Pareto principle is observed for a DVD rentals, which states that 20% of customers will be responsible for approximately 80% of the rentals. You need to write a query that would identify the top 20% of customers based on the number of rentals they had made, and then calculate the percentage of total rentals they accounted for. 
  
In the task you need to:

1. calculate the total number of rentals across all customers.
2. identify the top 20% of customers by rentals.
3. calculate the number of rentals by these top 20% of customers.
4. Finally, to calculate the percentage of rentals by the top 20% of customers compared to the total number of rentals.

In your query you need to return three pieces of information:

1. top_20%_rentals_count: The total number of rentals made by the top 20% of customers.
2. total_rentals_count: The total number of rentals made by all customers.
3. percentage_of_top_20%: The percentage of total rentals made by the top 20% of customers. Should be of numeric type, rounded to 2 decimal places

Notes:
1. for the sample tests, static dump of DVD Rental Sample Database is used, for the final solution - random tests.
2. Static dump will not provide belieavable percentage, but random test has been written to correlate with Pareto principle
3. What is meant by top 20% of customers? If there are 1000 customers in total, we would first order them by the number of rentals they have made, and then take the top 200 customers in terms of number of rentals. These 200 customers would be considered the "top 20%" of customers.
4. What we want to achieve is to cut off exactly 20% of customers regardless of tie. If 20 % is not the whole number - for example, for 599 customers it would be 119.8 - then we need to take upper bound, 120, not 119

Good luck!

Schema
(not all columns - only part of the domain required to solve this kata)

customer table:
Column       | Type     | Modifiers
------------ +----------+----------
customer_id  | integer  | not null
first_name   | varchar  | not null
last_name    | varchar  | not null

rental table:
Column       | Type      | Modifiers
-------------+-----------+----------
rental_id    | integer   | not null
customer_id  | integer   | not null

Desired Output
The desired output should look like this:

top_20%_rentals_count   | total_rentals_count  |     percentage_of_top_20%    
-----------------------+----------------------+--------------------------+
  7756                 | 10000                |   0.776e2                |
'''
-- Your SQL
with cte1 as (
  select customer_id, count(customer_id) as count_20
  from rental
  group by 1
  order by count_20 desc
  limit ( select ceil(count(distinct(customer_id)) * 0.2)::integer from rental )
), cte2 as (
  select customer_id, count(customer_id) as count_20
  from rental
  group by 1
  order by count_20 desc
), cte3 as (
  select
  (select sum(count_20)::integer from cte1) as "top_20%_rentals_count",
  (select sum(count_20)::integer from cte2) as total_rentals_count
)
select
  "top_20%_rentals_count",
  total_rentals_count,
  round(("top_20%_rentals_count" / total_rentals_count::numeric) * 100, 2) as "percentage_of_top_20%"
from cte3;
