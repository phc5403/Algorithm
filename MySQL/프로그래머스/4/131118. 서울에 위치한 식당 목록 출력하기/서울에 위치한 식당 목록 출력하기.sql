-- 코드를 입력하세요
SELECT i.rest_id, i.rest_name, i.food_type, i.favorites, i.address, round(avg(r.review_score), 2) as score
FROM rest_info i JOIN rest_review r
ON i.rest_id = r.rest_id
WHERE i.address LIKE "서울%"
GROUP BY i.rest_id, i.rest_name, i.food_type, i.favorites, i.address
ORDER BY score DESC, i.favorites DESC;

# SELECT * FROM rest_info;
# SELECT * FROm rest_review;