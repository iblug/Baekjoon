-- 코드를 입력하세요
SELECT t1.animal_id, t1.name
FROM animal_ins t1
INNER JOIN animal_outs t2
    USING (animal_id)
WHERE t1.datetime > t2.datetime
ORDER BY t1.datetime;