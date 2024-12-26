-- 코드를 작성해주세요
select score, e.emp_no, emp_name, position, email
from (select sum(score) as score, emp_no
      from hr_grade
      group by emp_no
      order by sum(score) desc
      limit 1) as sub_table JOIN hr_employees e
ON sub_table.emp_no = e.emp_no



# select sum(score), emp_no
# from hr_grade
# group by emp_no
# order by sum(score) desc
# limit 1
    