-- 코드를 입력하세요
SELECT date_format(sales_date, "%Y-%m-%d") as sales_date, product_id, user_id, sales_amount
FROM (
    SELECT date_format(sales_date, "%Y-%m-%d") as sales_date, product_id, user_id, sales_amount
    FROM online_sale
    WHERE year(sales_date) = 2022 and month(sales_date) = 3

    UNION ALL

    SELECT date_format(sales_date, "%Y-%m-%d") as sales_date, product_id, null as user_id, sales_amount
    FROM offline_sale
    WHERE year(sales_date) = 2022 and month(sales_date) = 3) as temp
ORDER BY sales_date, product_id, user_id

