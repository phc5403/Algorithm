-- 코드를 입력하세요
SELECT user_id, nickname, concat(city, " ",street_address1, " ", street_address2) as "전체주소",
concat(left(tlno, 3), "-", mid(tlno, 4, 4), "-", right(tlno, 4)) as "전화번호"
from USED_GOODS_BOARD b join USED_GOODS_USER u
on b.writer_id = u.user_id
group by b.writer_id
having count(writer_id) > 2
order by user_id desc