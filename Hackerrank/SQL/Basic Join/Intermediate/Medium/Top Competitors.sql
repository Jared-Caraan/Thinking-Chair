-- Julia just finished conducting a coding contest, and she needs your help assembling the leaderboard! Write a query to print the respective hacker_id and name of hackers who achieved full scores for more than one challenge. Order your output in descending order by the total number of challenges in which the hacker earned a full score. If more than one hacker received full scores in same number of challenges, then sort them by ascending hacker_id.

-- https://www.hackerrank.com/challenges/full-score/problem?isFullScreen=true

SELECT sub.hacker_id, h.name
FROM(
    SELECT s.hacker_id, COUNT(*) AS count
    FROM Submissions s
    LEFT JOIN Challenges c
    ON s.challenge_id = c.challenge_id
    LEFT JOIN Difficulty d
    ON c.difficulty_level = d.difficulty_level
    WHERE s.score = d.score
    GROUP BY s.hacker_id
    HAVING COUNT(*) > 1
) sub
LEFT JOIN Hackers h
ON sub.hacker_id = h.hacker_id
ORDER BY sub.count DESC, sub.hacker_id;