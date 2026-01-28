-- Query the average population for all cities in CITY, rounded down to the nearest integer.

-- https://www.hackerrank.com/challenges/average-population/problem?isFullScreen=true

SELECT FLOOR(AVG(POPULATION))
FROM CITY;