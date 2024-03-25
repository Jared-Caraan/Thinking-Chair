-- Hermione decides the best way to choose is by determining the minimum number of gold galleons needed to buy each non-evil wand of high power and age. Write a query to print the id, age, coins_needed, and power of the wands that Ron's interested in, sorted in order of descending power. If more than one wand has same power, sort the result in order of descending age.

-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true

-- Note: Ill-posed question

SELECT w.id, sub.age, sub.coins_needed, sub.power
FROM (
    SELECT wp.age, w.power, MIN(w.coins_needed) AS coins_needed
    FROM Wands w
    LEFT JOIN Wands_Property wp
    ON w.code = wp.code
    WHERE wp.is_evil = 0
    GROUP BY wp.age, w.power
) sub
INNER JOIN Wands w
ON sub.coins_needed = w.coins_needed AND sub.power = w.power
INNER JOIN Wands_Property wp
ON w.code = wp.code AND sub.age = wp.age
ORDER BY sub.power DESC, sub.age DESC;