-- 코드를 입력하세요
SELECT animal_id, name
from animal_ins
where name LIKE "%el%" AND animal_type = "dog"
order by name