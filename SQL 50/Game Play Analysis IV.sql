"""
Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 

Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

The result format is in the following example.

 

Example 1:

Input: 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output: 
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
Explanation: 
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33
"""

WITH cte1 AS(
    SELECT A.player_id, A.earliest, B.total_count
    FROM (
        SELECT
            player_id,
            'dummy' AS dummy_col,
            MIN(event_date) AS earliest
        FROM Activity
        GROUP BY 1,2
    ) A
    LEFT JOIN(
        SELECT
            'dummy' AS dummy_col,
            COUNT(distinct(player_id)) AS total_count
        FROM Activity
    ) B
    ON A.dummy_col = B.dummy_col
)
SELECT
    IF(ROUND((COUNT(A.player_id) / cte1.total_count), 2) IS NULL, 0, ROUND((COUNT(A.player_id) / cte1.total_count), 2)) AS fraction
FROM Activity A
LEFT JOIN cte1
ON cte1.player_id = A.player_id
WHERE DATEDIFF(A.event_date, cte1.earliest) = 1;

"""
-- Alternative solution

SELECT ROUND(
    COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2
) AS fraction
FROM Activity a
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY)) IN 
(
    SELECT player_id, MIN(event_date) FROM Activity GROUP BY player_id
);

-- Alternative solution
WITH cte AS(
    SELECT 
        player_id,
        event_date,
        DATE_SUB(event_date, INTERVAL 1 DAY) = MIN(event_date) OVER (PARTITION BY player_id) AS r 
    FROM activity
)
SELECT ROUND(SUM(r) / COUNT(DISTINCT player_id),2) AS fraction FROM cte
"""