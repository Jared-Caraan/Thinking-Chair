-- Query the difference between the maximum and minimum populations in CITY.

-- https://www.hackerrank.com/challenges/population-density-difference/problem?isFullScreen=true

SELECT MAX(POPULATION) - MIN(POPULATION)
FROM CITY;