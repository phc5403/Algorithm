-- 코드를 입력하세요
SELECT concat("/home/grep/src/", b.board_id, "/", f.file_id, f.file_name, f.file_ext) as file_path
from used_goods_board b join used_goods_file f
on b.board_id = f.board_id
where views = (select max(views)
              from used_goods_board)
order by f.file_id desc

# select * 
# from used_goods_board b join used_goods_file f
# on b.board_id = f.board_id
# where views = 301
# order by views desc



/*
BOARD_ID	WRITER_ID	TITLE	CONTENTS	PRICE	CREATED_DATE	STATUS	VIEWS	FILE_ID	FILE_EXT	FILE_NAME	BOARD_ID

B0008	hong02	자전거 판매합니다	출퇴근용으로 구매했다가 사용하지 않아서 내놔요	40000	2022-10-04 00:00:00	SALE	301	MOV_000008	.avi	photo1	B0008

B0008	hong02	자전거 판매합니다	출퇴근용으로 구매했다가 사용하지 않아서 내놔요	40000	2022-10-04 00:00:00	SALE	301	IMG_000011	.png	photo	B0008

*/