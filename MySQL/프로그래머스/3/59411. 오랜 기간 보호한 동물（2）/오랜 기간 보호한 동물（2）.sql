-- 코드를 입력하세요
SELECT i.animal_id, i.name
from animal_ins i join animal_outs o
on i.animal_id = o.animal_id
group by datediff(o.datetime, i.datetime)
order by datediff(o.datetime, i.datetime) desc
limit 2

# datediff(o.datetime, i.datetime) as date