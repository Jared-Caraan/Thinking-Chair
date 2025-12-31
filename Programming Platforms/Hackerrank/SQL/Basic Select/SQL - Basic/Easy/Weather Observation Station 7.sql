-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. 
-- Your result cannot contain duplicates.

SELECT DISTINCT(CITY)
FROM STATION
WHERE LOWER(SUBSTRING(CITY, -1, 1)) IN ('a','e','i','o','u')