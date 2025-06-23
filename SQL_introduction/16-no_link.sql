-- 
SELECT score, name
FROM second_table
WHERE NAME is not null and NAME != ''
ORDER BY score DESC;