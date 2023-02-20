-- 코드를 입력하세요
SELECT t1.name, t1.datetime
FROM animal_ins t1
LEFT JOIN animal_outs t2
    USING (animal_id)
WHERE t2.datetime IS NULL
ORDER BY t1.datetime
LIMIT 3;