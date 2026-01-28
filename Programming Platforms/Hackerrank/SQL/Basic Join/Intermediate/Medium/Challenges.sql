-- Write a query to print the hacker_id, name, and the total number of challenges created by each student. Sort your results by the total number of challenges in descending order. If more than one student created the same number of challenges, then sort the result by hacker_id. If more than one student created the same number of challenges and the count is less than the maximum number of challenges created, then exclude those students from the result.

-- https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true

WITH cte1 AS (
    SELECT c.hacker_id, COUNT(c.challenge_id) AS cnt, ROW_NUMBER() OVER (PARTITION BY COUNT(c.challenge_id) ORDER BY COUNT(c.challenge_id)) AS row_cnt
    FROM Challenges c
    GROUP BY c.hacker_id
),
cte2 AS (
    SELECT c.hacker_id, h.name, c.cnt, c.row_cnt, LEAD(c.row_cnt, 1, 0) OVER (PARTITION BY c.cnt) AS ld, RANK() OVER (ORDER BY c.cnt DESC) AS rnk
    FROM cte1 c
    LEFT JOIN Hackers h
    ON c.hacker_id = h.hacker_id
)
SELECT c.hacker_id, c.name, c.cnt
FROM cte2 c
WHERE rnk = 1 OR (c.row_cnt = 1 AND c.ld = 0)
ORDER BY c.cnt DESC, c.hacker_id;