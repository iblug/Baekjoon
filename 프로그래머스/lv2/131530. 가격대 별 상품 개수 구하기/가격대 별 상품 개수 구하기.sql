-- 코드를 입력하세요
SELECT TRUNCATE(price / 10000,0)*10000 AS `price_group`, count(*) AS `products`
FROM product
GROUP BY TRUNCATE(price / 10000,0)
ORDER BY `price_group`;

