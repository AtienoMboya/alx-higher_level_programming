-- lists all records of the table
SELECT `score`, `name`
FROM second_table
WHERE `name` IS NOT EMPTY
ORDER BY `score` DESC;
