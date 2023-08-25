"""
Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
In SQL, id is the primary key for this table.
This table contains information about the temperature on a certain day.
 

Find all dates' Id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.

The result format is in the following example.

 

Example 1:

Input: 
Weather table:
+----+------------+-------------+
| id | recordDate | temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
Output: 
+----+
| id |
+----+
| 2  |
| 4  |
+----+
Explanation: 
In 2015-01-02, the temperature was higher than the previous day (10 -> 25).
In 2015-01-04, the temperature was higher than the previous day (20 -> 30).
"""

SELECT
  # W1.id AS PrevID,
  W2.id
  # W1.recordDate AS PrevDate,
  # W2.recordDate AS NewDate,
  # W1.temperature AS PrevTemp,
  # W2.temperature AS NewTemp,
  # W2.recordDate - W1.recordDate AS diff
FROM Weather W1, Weather W2
WHERE (DATEDIFF(W2.recordDate,W1.recordDate) = 1) AND W2.temperature > W1.temperature;
# ORDER BY 1;