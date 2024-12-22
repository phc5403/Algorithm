-- 코드를 작성해주세요
SELECT count(id) fish_count, max(length) max_length, fish_type
FROM fish_info
GROUP BY fish_type
HAVING avg(if(length is null, 10, length)) >= 33
ORDER BY fish_type