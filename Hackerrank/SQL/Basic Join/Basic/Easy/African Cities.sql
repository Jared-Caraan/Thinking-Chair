-- Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

SELECT CTY.NAME
FROM CITY CTY
INNER JOIN COUNTRY CNT
ON CTY.COUNTRYCODE = CNT.CODE
WHERE CNT.CONTINENT = 'Africa'