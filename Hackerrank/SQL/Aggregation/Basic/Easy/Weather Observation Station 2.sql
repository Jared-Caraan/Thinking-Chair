-- Query the following two values from the STATION table:

-- 1. The sum of all values in LAT_N rounded to a scale of 2 decimal places.
-- 2. The sum of all values in LONG_W rounded to a scale of 2 decimal places.

-- https://www.hackerrank.com/challenges/weather-observation-station-2/problem?isFullScreen=true

SELECT ROUND(SUM(LAT_N),2), ROUND(SUM(LONG_W),2)
FROM STATION;