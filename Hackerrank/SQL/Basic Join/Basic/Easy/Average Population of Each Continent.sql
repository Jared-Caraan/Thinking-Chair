-- Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their respective average city populations (CITY.Population) rounded down to the nearest integer.

-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

SELECT CNT.CONTINENT, FLOOR(AVG(CTY.POPULATION))
FROM COUNTRY CNT
INNER JOIN CITY CTY
ON CNT.CODE = CTY.COUNTRYCODE
GROUP BY CNT.CONTINENT