"""
Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
 

Write a solution to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Products table:
+------------+-----------+-------------+
| product_id | new_price | change_date |
+------------+-----------+-------------+
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
+------------+-----------+-------------+
Output: 
+------------+-------+
| product_id | price |
+------------+-------+
| 2          | 50    |
| 1          | 35    |
| 3          | 10    |
+------------+-------+
"""

WITH cte AS (
    SELECT
        *
    FROM Products
    WHERE change_date <= '2019-08-16'
),
cte2 AS (
   SELECT
        product_id,
        new_price,
        MAX(change_date) AS max_date
    FROM cte
    GROUP BY 1
),
cte3 AS (
    SELECT P.product_id, P.new_price FROM Products P
    INNER JOIN cte2 c
    ON P.product_id = c.product_id AND P.change_date = c.max_date
)
SELECT product_id, new_price AS price
FROM cte3
UNION
SELECT P.product_id, 10
FROM Products P
LEFT JOIN cte3 c
ON P.product_id = c.product_id
WHERE c.product_id IS NULL;

"""
-- Alternative solution

WITH t AS (
    SELECT
        product_id, new_price,
        rank() OVER(PARTITION BY product_id ORDER BY change_date DESC) rnk
    FROM Products
    WHERE change_date <= '2019-08-16'
)

SELECT p.product_id, IFNULL(t.new_price, 10) price
FROM Products p LEFT JOIN t USING(product_id)
WHERE t.rnk = 1 or t.rnk IS NULL
GROUP BY p.product_id
"""