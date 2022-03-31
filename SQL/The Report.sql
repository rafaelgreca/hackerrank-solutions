SELECT s.name, g.grade, s.marks
FROM students s JOIN grades g
ON s.marks BETWEEN g.min_mark AND g.max_mark
WHERE g.grade >= 8
ORDER BY g.grade DESC, s.name ASC;

SELECT NULL, g.grade, s.marks
FROM students s JOIN grades g
ON s.marks BETWEEN g.min_mark AND g.max_mark
WHERE g.grade < 8
ORDER BY g.grade DESC, s.marks ASC;