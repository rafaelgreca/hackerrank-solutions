SELECT DISTINCT(city)
FROM station
WHERE LOWER(RIGHT(city, 1)) in ('a', 'e', 'i', 'o', 'u');