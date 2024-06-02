-- Write a query to output the names of those students whose best friends got offered a higher salary than them. Names must be ordered by the salary amount offered to the best friends. It is guaranteed that no two students got same salary offer.

-- https://www.hackerrank.com/challenges/placements/problem?isFullScreen=true

SELECT S.Name
FROM Students S
LEFT JOIN Packages P
ON S.ID = P.ID
LEFT JOIN (
    SELECT FF.ID, FF.Friend_ID, SS.Name
    FROM Friends FF
    LEFT JOIN Students SS
    ON FF.Friend_ID = SS.ID
) A
ON A.ID = S.ID
LEFT JOIN Packages PP
ON PP.ID = A.Friend_ID
WHERE PP.Salary > P.Salary
ORDER BY PP.Salary;

-- select name
-- from students as s 
-- inner join friends as f on s.id = f.id 
-- inner join packages as p1 on s.id = p1.id 
-- inner join packages as p2 on f.friend_id = p2.id 
-- where p2.salary > p1.salary
-- order by p2.salary 