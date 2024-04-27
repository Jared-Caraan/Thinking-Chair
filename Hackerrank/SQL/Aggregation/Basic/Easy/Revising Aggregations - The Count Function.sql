-- Query a count of the number of cities in CITY having a Population larger than 100,000.

-- https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem?isFullScreen=true

SELECT COUNT(*)
FROM CITY
WHERE POPULATION > 100000;