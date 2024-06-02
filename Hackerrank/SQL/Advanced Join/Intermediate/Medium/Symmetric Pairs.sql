-- Two pairs (X1, Y1) and (X2, Y2) are said to be symmetric pairs if X1 = Y2 and X2 = Y1.

-- Write a query to output all such symmetric pairs in ascending order by the value of X. List the rows such that X1 ≤ Y1.

-- https://www.hackerrank.com/challenges/symmetric-pairs/problem?isFullScreen=true

WITH CTE AS (
    SELECT X, Y, ROW_NUMBER() OVER (PARTITION BY Y) AS row_num
    FROM Functions
    WHERE X = Y
),
CTE2 AS (
    SELECT X, Y
    FROM CTE
    WHERE row_num = 2
    UNION ALL
    SELECT X, Y
    FROM Functions
    WHERE ( CONCAT(Y, ' - ', X) IN ( SELECT CONCAT(X, ' - ', Y)  FROM Functions) AND X <> Y ) AND X <= Y
    ORDER BY X
)
SELECT X, Y
FROM CTE2
ORDER BY X;

-- WITH cte AS (
--     SELECT f1.*
--     FROM functions AS f1  
--     INNER JOIN (
--         SELECT x, y 
--         FROM functions
--         ) AS f2 
--     ON f1.x = f2.y AND f1.y = f2.x
--     WHERE f1.x <= f1.y
--     ) 
-- SELECT * 
-- FROM cte
-- GROUP BY x, y 
-- HAVING COUNT(*) > 1 -- remove case where x = y and one record only
-- OR x < y 
-- ORDER BY x