-- 코드를 입력하세요
SELECT animal_id, name
FROM (
    SELECT t2.animal_id, t2.name, t1.datetime
    FROM animal_ins t1
    RIGHT JOIN animal_outs t2
        USING (animal_id)
) AS t1
WHERE datetime IS NULL
ORDER BY 1;