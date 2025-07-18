-- 11. List records with score >= 10 from second_table ordered by descending score
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC;
