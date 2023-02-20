-- 코드를 입력하세요
SELECT t1.animal_id, t1.name
FROM animal_ins t1
INNER JOIN animal_outs t2
    USING (animal_id)
ORDER BY
    (t2.datetime - t1.datetime) DESC
LIMIT 2;