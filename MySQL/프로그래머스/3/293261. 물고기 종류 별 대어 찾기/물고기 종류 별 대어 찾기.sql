-- 코드를 작성해주세요
select i.id, n.fish_name, i.length
from fish_info i JOIN fish_name_info n
on i.fish_type = n.fish_type
where (i.fish_type, i.length) IN (
    select fish_type, max(length)
    from fish_info
    group by fish_type)
order by i.id