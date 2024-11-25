-- 코드를 작성해주세요
# 1. YEAR() 사용
-- where year(time) = 2021;

# 2. BETWEEN 사용 -> 성능 최적화
-- where time between '2021-01-01' and '2021-12-31';

select count(fish_type) fish_count
from fish_info
where time between '2021-01-01' and '2021-12-31';