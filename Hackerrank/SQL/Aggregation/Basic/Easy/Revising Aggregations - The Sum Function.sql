-- Query the total population of all cities in CITY where District is California.

-- https://www.hackerrank.com/challenges/revising-aggregations-sum/problem?isFullScreen=true

SELECT SUM(POPULATION)
FROM CITY
WHERE DISTRICT = 'California';