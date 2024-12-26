-- 코드를 입력하세요
SELECT ingredient_type, sum(total_order) as total_order
from first_half h join icecream_info i
on h.flavor = i.flavor
group by ingredient_type
order by sum(total_order)
