SELECT SUM(population)
FROM city
WHERE countrycode = 'JPN'
GROUP BY countrycode;