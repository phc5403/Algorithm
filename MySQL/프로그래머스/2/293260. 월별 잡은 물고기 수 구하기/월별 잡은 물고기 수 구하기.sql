-- 코드를 작성해주세요
select count(id) as fish_count, month(time) as month
from fish_info
group by month(time)
order by month(time)

-- 예시 데이터 -> 같은 달에 같은 종류를 중복해서 잡아도, ID가 달라서 별개로 인정함.
-- 잡은 물고기가 0 -> 출력 안함.