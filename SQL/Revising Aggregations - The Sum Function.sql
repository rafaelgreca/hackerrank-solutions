SELECT SUM(population)
FROM city
WHERE district = 'California'
GROUP BY district;