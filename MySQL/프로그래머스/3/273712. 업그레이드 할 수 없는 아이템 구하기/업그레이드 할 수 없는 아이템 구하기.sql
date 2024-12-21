-- 코드를 작성해주세요
select i.item_id, i.item_name, i.rarity
from item_info i join item_tree t
on i.item_id = t.item_id
where i.item_id NOT IN (select distinct parent_item_id
                        from item_tree
                        where parent_item_id is not null)
order by item_id desc

-- 다른 아이템의 parent_item_id로 사용되지 않는 아이템 찾기

# select distinct parent_item_id
# from item_tree
# where parent_item_id is not null