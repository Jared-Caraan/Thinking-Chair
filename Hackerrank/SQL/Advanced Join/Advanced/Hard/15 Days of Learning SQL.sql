-- Write a query to print total number of unique hackers who made at least 1 submission each day (starting on the first day of the contest), and find the hacker_id and name of the hacker who made maximum number of submissions each day. If more than one such hacker has a maximum number of submissions, print the lowest hacker_id. The query should print this information for each day of the contest, sorted by the date.

-- https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem?isFullScreen=true

WITH CTE AS (
    SELECT submission_date, hacker_id
    FROM Submissions
    GROUP BY submission_date, hacker_id
),
CTE2 AS (
    SELECT submission_date, hacker_id, ROW_NUMBER() OVER (PARTITION BY hacker_id ORDER BY submission_date) AS row_num, DENSE_RANK() OVER (ORDER BY submission_date) AS dy
    FROM CTE
), 
CTE3 AS (
    SELECT submission_date, COUNT(hacker_id) AS cnt_hacks
    FROM CTE2
    WHERE dy = row_num
    GROUP BY submission_date
), 
CTE4 AS (
 SELECT submission_date, hacker_id, COUNT(hacker_id) AS cnt_hacker
 FROM Submissions
 GROUP BY submission_date, hacker_id
 ORDER BY submission_date, COUNT(hacker_id) DESC
),
CTE5 AS (
 SELECT submission_date, MAX(cnt_hacker) AS max_cnt
 FROM CTE4
 GROUP BY submission_date
),
CTE6 AS (
 SELECT CC.submission_date, MIN(CC.hacker_id) AS min_hacker
 FROM CTE5 C
 LEFT JOIN CTE4 CC
 ON C.submission_date = CC.submission_date AND C.max_cnt = CC.cnt_hacker
 GROUP BY CC.submission_date
 ORDER BY CC.submission_date
)
SELECT six.submission_date, three.cnt_hacks, six.min_hacker, h.name
FROM CTE6 six
LEFT JOIN Hackers H
ON six.min_hacker = H.hacker_id
LEFT JOIN CTE3 three
ON six.submission_date = three.submission_date
ORDER BY six.submission_date;
