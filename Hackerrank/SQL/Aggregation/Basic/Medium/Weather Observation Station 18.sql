-- Query the Manhattan Distance between points P1 and P2 and round it to a scale of 4 decimal places.

-- https://www.hackerrank.com/challenges/weather-observation-station-18/problem?isFullScreen=true

SELECT ROUND(ABS(MIN(LAT_N) - MAX(LAT_N)) + ABS(MIN(LONG_W) - MAX(LONG_W)),4)
FROM STATION