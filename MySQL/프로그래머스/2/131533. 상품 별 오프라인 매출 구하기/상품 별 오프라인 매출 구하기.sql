-- 코드를 입력하세요
SELECT p.product_code, sum(p.price * o.sales_amount) as sales
FROM product p JOIN offline_sale o
ON p.product_id = o.product_id
GROUP BY p.product_code
ORDER BY sales desc, p.product_code asc


/*
1. 상품코드 별 매출액(= 판매가 * 판매량)
2. 매출액을 기준으로 내림차순
3. 매출액이 같다면, 상품코드를 기준으로 오름차순
*/
