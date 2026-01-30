-- Your goal is to write a function that removes the first and last characters of a string. You're given one parameter, the original string.

-- Important: Your function should handle strings of any length ≥ 2 characters. For strings with exactly 2 characters, return an empty string.
  
-- # write your SQL statement here: you are given a table 'removechar' with column 's', return a table with column 's' and your result in a column named 'res'.
SELECT s,
  CASE
    WHEN length(s) = 2 THEN ''
    ELSE substring(s, 2, length(s)-2)
  END as res
FROM removechar

-- Clever
select s, substring(s from '^.(.*).$') res
from removechar
