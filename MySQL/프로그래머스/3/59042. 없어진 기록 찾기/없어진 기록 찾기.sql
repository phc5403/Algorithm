SELECT animal_id, name 
from animal_outs 
where animal_id NOT IN (select animal_id           
                        from animal_ins) 
order by animal_id
