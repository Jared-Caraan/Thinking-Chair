-- The total score of a hacker is the sum of their maximum scores for all of the challenges. Write a query to print the hacker_id, name, and total score of the hackers ordered by the descending score. If more than one hacker achieved the same total score, then sort the result by ascending hacker_id. Exclude all hackers with a total score of  from your result.

-- https://www.hackerrank.com/challenges/contest-leaderboard/problem?isFullScreen=true

SELECT sub.hacker_id, h.name, SUM(sub.score) AS score
FROM (
    SELECT s.hacker_id, s.challenge_id, MAX(s.score) AS score
    FROM Submissions s
    GROUP BY s.hacker_id, s.challenge_id
    ORDER BY s.hacker_id
) sub
LEFT JOIN Hackers h
ON sub.hacker_id = h.hacker_id
GROUP BY sub.hacker_id, h.name
HAVING SUM(sub.score) <> 0
ORDER BY SUM(sub.score) DESC, sub.hacker_id;