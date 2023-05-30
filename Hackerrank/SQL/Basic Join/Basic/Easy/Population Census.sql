-- Given the CITY and COUNTRY tables, query the sum of the populations of all cities where the CONTINENT is 'Asia'.

-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

SELECT SUM(CTY.POPULATION)
FROM CITY CTY
INNER JOIN COUNTRY CNT
ON CTY.COUNTRYCODE = CNT.CODE
WHERE CNT.CONTINENT = 'Asia'