-- List records with names in second_table ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
