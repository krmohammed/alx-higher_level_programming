-- lists all records without null name

SELECT * FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
