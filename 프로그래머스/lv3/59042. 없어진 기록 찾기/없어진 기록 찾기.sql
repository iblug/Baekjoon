-- 코드를 입력하세요
SELECT t2.animal_id, t2.name
FROM animal_ins t1
RIGHT JOIN animal_outs t2
    USING (animal_id)
WHERE t1.animal_id IS NULL
ORDER BY 1;