SELECT s.name
FROM friends f JOIN packages p
ON f.id = p.id JOIN students s
ON s.id = f.id JOIN packages p2
ON p2.id = f.friend_id JOIN students s2
ON f.friend_id = s2.id
WHERE p2.salary > p.salary
ORDER BY p2.salary;