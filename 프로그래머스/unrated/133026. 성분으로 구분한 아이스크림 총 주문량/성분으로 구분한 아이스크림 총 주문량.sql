-- 코드를 입력하세요
SELECT ingredient_type, SUM(total_order) AS total_order
FROM icecream_info AS t1 ,first_half AS t2
WHERE t1.flavor = t2.flavor
GROUP BY ingredient_type
ORDER BY total_order