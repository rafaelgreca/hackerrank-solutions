SELECT h.hacker_id, h.name, SUM(u.score)
FROM hackers h JOIN (SELECT hacker_id, challenge_id, MAX(score) as score
FROM submissions GROUP BY hacker_id, challenge_id) u
ON h.hacker_id = u.hacker_id
GROUP BY h.hacker_id, h.name
HAVING SUM(u.score) > 0
ORDER BY SUM(u.score) DESC, h.hacker_id ASC;