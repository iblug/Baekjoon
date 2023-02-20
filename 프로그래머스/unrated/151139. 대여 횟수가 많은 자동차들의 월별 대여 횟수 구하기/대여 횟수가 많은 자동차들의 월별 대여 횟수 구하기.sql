-- 코드를 입력하세요
# SELECT MONTH(start_date) as month, car_id, count(car_id) as records
# FROM car_rental_company_rental_history
# WHERE start_date BETWEEN '2022-08-01' AND '2022-10-30'
# GROUP BY car_id, MONTH(start_date)
# HAVING records >= 5
# ORDER BY month, car_id desc;

SELECT MONTH(start_date) AS month, car_id, count(car_id) as records
FROM car_rental_company_rental_history
WHERE car_id IN (
    SELECT car_id
    FROM car_rental_company_rental_history
    WHERE start_date BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY car_id
    HAVING COUNT(car_id) >= 5
)
    AND start_date BETWEEN '2022-08-01' AND '2022-10-31'
GROUP BY car_id, month
ORDER BY month, car_id DESC;

# SELECT *
# FROM car_rental_company_rental_history
# WHERE start_date BETWEEN '2022-08-01' AND '2022-10-30'
