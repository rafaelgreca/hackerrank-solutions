SELECT AVG(population)
FROM city
WHERE district = 'California'
GROUP BY district;