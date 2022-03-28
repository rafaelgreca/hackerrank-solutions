SELECT CONCAT(name, '(', LEFT(occupation, 1), ')') as name_occupation
FROM occupations
ORDER BY name_occupation ASC;

SELECT CONCAT('There are a total of ', COUNT(name), ' ', LOWER(occupation), 's.')
FROM occupations
GROUP BY occupation
ORDER BY COUNT(name), occupation;