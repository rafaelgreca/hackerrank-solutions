SELECT DISTINCT(city)
FROM station
WHERE LOWER(LEFT(city, 1)) in ('a', 'e', 'i', 'o', 'u') AND LOWER(RIGHT(city, 1)) in ('a', 'e', 'i', 'o', 'u');