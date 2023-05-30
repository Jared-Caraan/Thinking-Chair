-- Pivot the Occupation column in OCCUPATIONS so that each Name is sorted alphabetically and displayed underneath its corresponding Occupation. The output column headers should be Doctor, Professor, Singer, and Actor, respectively.

-- Note: Print NULL when there are no more names corresponding to an occupation.

WITH A AS(
    SELECT ROW_NUMBER() OVER() R,
    Occupation, Name
    FROM OCCUPATIONS
    WHERE Occupation = 'Doctor'
    ORDER BY Name
),
    B AS(
    SELECT ROW_NUMBER() OVER() R,
    Occupation, Name
    FROM OCCUPATIONS
    WHERE Occupation = 'Professor'
    ORDER BY Name
),
    C AS(
    SELECT ROW_NUMBER() OVER() R,
    Occupation, Name
    FROM OCCUPATIONS
    WHERE Occupation = 'Singer'
    ORDER BY Name
),
    D AS(
    SELECT ROW_NUMBER() OVER() R,
    Occupation, Name
    FROM OCCUPATIONS
    WHERE Occupation = 'Actor'
    ORDER BY Name
)
SELECT A.Name, B.Name, C.Name, D.Name
FROM A
RIGHT JOIN B ON B.R = A.R
LEFT JOIN C ON C.R = B.R
LEFT JOIN D ON D.R = B.R