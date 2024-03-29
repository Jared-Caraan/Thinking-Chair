"""
Table: Seat

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
id is a continuous increment.
 

Write a solution to swap the seat id of every two consecutive students. If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.

The result format is in the following example.

 

Example 1:

Input: 
Seat table:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
Output: 
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
Explanation: 
Note that if the number of students is odd, there is no need to change the last one's seat.
"""

WITH cte AS (
    SELECT
        *,
        ROW_NUMBER() OVER () AS row_num
    FROM Seat
)
SELECT
    id,
    CASE
        WHEN row_num = (SELECT COUNT(*) FROM Seat) AND row_num % 2 <> 0 THEN student
        WHEN row_num % 2 = 0 THEN (SELECT student FROM Seat WHERE id = row_num -1)
        WHEN row_num % 2 <> 0 THEN (SELECT student FROM Seat WHERE id = row_num + 1)
    END AS student
FROM cte

"""
-- Alternative solution
select 
CASE
  WHEN (id = (select max(id) from Seat) and id mod 2 = 1) THEN id
  WHEN (id mod 2 = 1) THEN id+1
  WHEN (id mod 2 = 0) THEN id-1
END AS id, student
FROM Seat
ORDER BY id;
"""