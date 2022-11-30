-- list some records for scores >= 10
SELECT second_table.score, second_table.name
FROM second_table
WHERE score >= 10
ORDER BY score DESC
