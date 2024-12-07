-- 코드를 작성해주세요
select count(nain.fish_name) as fish_count
from fish_info inf join fish_name_info nain
on inf.fish_type = nain.fish_type
where nain.fish_name = "BASS" or nain.fish_name = "SNAPPER"