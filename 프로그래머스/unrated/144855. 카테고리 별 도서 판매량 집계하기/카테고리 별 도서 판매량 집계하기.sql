-- 코드를 입력하세요
SELECT category, SUM(sales) AS total_sales
FROM book t1
INNER JOIN book_sales t2
    USING (book_id)
WHERE MONTH(sales_date) = 1 AND YEAR(sales_date) = 2022
GROUP BY category
ORDER BY category