-- Ketty gives Eve a task to generate a report containing three columns: Name, Grade and Mark. Ketty doesn't want the NAMES of those students who received a grade lower than 8. The report must be in descending order by grade -- i.e. higher grades are entered first. If there is more than one student with the same grade (8-10) assigned to them, order those particular students by their name alphabetically. Finally, if the grade is lower than 8, use "NULL" as their name and list them by their grades in descending order. If there is more than one student with the same grade (1-7) assigned to them, order those particular students by their marks in ascending order.

-- https://www.hackerrank.com/challenges/the-report/problem?isFullScreen=true

WITH cte1 AS(
    SELECT s.Name, s.Marks, G.Min_Mark, G.Max_Mark, G.Grade
    FROM Students s
    LEFT JOIN Grades G
    ON s.Marks BETWEEN G.Min_Mark AND G.Max_Mark
)
SELECT 
CASE 
    WHEN Grade >= 8 THEN Name 
    ELSE "NULL"
END AS Name, Grade, Marks
FROM cte1
ORDER BY Grade DESC,
CASE WHEN Grade >= 8 THEN Name END ASC,
CASE WHEN Grade < 8 THEN Marks END ASC;