-- Write a query to output the start and end dates of projects listed by the number of days it took to complete the project in ascending order. If there is more than one project that have the same number of completion days, then order by the start date of the project.

-- https://www.hackerrank.com/challenges/sql-projects/problem?isFullScreen=true

WITH CTE AS (
    SELECT P.Start_Date, ROW_NUMBER() OVER( PARTITION BY PP.End_Date ) AS End_Date
    FROM Projects P
    LEFT JOIN Projects PP
    ON P.Start_Date = PP.End_Date
    WHERE PP.End_Date IS NULL
),
CTE2 AS (
    SELECT P.End_Date, ROW_NUMBER() OVER( PARTITION BY PP.Start_Date ) AS Start_Date
    FROM Projects P
    LEFT JOIN Projects PP
    ON P.End_Date = PP.Start_Date
    WHERE PP.Start_Date IS NULL
)
SELECT C.Start_Date, CC.End_Date
FROM CTE C
INNER JOIN CTE2 CC
ON C.End_Date = CC.Start_Date
ORDER BY CC.End_Date - C.Start_Date, C.Start_Date;

