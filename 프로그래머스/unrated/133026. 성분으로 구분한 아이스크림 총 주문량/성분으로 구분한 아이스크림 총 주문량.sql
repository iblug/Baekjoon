-- 코드를 입력하세요
SELECT ingredient_type, SUM(total_order) AS total_order
FROM icecream_info AS t1
INNER JOIN first_half AS t2
    ON t1.flavor = t2.flavor
GROUP BY ingredient_type
ORDER BY total_order