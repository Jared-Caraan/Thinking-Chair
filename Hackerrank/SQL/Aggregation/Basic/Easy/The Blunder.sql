-- Write a query calculating the amount of error (i.e.: actual-miscalculated average monthly salaries), and round it up to the next integer.

-- https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true

SELECT ROUND(ROUND(AVG(Salary),0) - ROUND(AVG(REPLACE(Salary, 0, '')),0),0)
FROM EMPLOYEES;