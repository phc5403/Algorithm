-- 코드를 입력하세요
SELECT user_id, product_id
FROM online_sale
GROUP BY user_id, product_id
HAVING count(*) > 1
ORDER BY user_id, product_id DESC;

-- 15 : 12