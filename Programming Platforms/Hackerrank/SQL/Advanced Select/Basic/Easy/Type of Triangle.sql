-- Write a query identifying the type of each record in the TRIANGLES table using its three side lengths. 
-- Output one of the following statements for each record in the table:

-- Equilateral: It's a triangle with 3 sides of equal length.
-- Isosceles: It's a triangle with 2 sides of equal length.
-- Scalene: It's a triangle with 3 sides of differing lengths.
-- Not A Triangle: The given values of A, B, and C don't form a triangle.

SELECT
    (
        CASE
            WHEN ((A + B) > C) AND ((A = B && A <> C) OR (A = C && A <> B) OR (B = C && A <> B)) THEN 'Isosceles'
            WHEN ((A + B) > C) AND (A = B && B = C) THEN 'Equilateral'
            WHEN ((A + B) > C) AND (A <> B && B <> C && A <> C) THEN 'Scalene'
            WHEN ((A + B) <= C) THEN 'Not A Triangle'
            ELSE ''
        END
    ) AS TRIANGLE
FROM TRIANGLES