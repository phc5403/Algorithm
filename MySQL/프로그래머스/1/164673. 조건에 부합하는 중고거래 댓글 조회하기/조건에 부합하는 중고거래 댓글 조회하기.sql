-- 코드를 입력하세요
SELECT b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.created_date, "%Y-%m-%d") as created_date
FROM used_goods_board b JOIN used_goods_reply r
ON b.board_id = r.board_id
WHERE year(b.created_date) = 2022 and month(b.created_date) = 10  
ORDER BY r.created_date, b.title

/* 
1. 2022년 10월 -> 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일

2. 댓글 작성일 기준 오름차순
3. 게시글 제목 기준 오름차순
*/
