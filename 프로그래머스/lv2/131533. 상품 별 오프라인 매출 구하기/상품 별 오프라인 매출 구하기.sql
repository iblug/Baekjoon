-- 코드를 입력하세요
SELECT PRODUCT_CODE, SUM(price * sales_amount) AS `SALES`
FROM product AS t1
INNER JOIN offline_sale AS t2
    ON t1.product_id = t2.product_id
GROUP BY product_code
ORDER BY 
    `SALES` DESC,
    product_code
