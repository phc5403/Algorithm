-- 코드를 입력하세요
SELECT history_id, car_id, date_format(start_date, "%Y-%m-%d") as start_date, date_format(end_date, "%Y-%m-%d") as end_date, CASE
# WHEN date_format(start_date, "%Y-%m") = "2022-09" and datediff(end_date, start_date) + 1 >= 30 then "장기 대여"
WHEN datediff(end_date, start_date) + 1 >= 30 then "장기 대여"
ELSE "단기 대여"
END as rent_type
from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where date_format(start_date, "%Y-%m") = "2022-09"
order by history_id desc

# select date_format(start_date, "%Y-%m")
# select *
# from car_rental_company_rental_history
# where datediff(end_date, start_date) >= 30 and date_format(start_date, "%Y-%m") = "2022-09"