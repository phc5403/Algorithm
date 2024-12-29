-- 코드를 입력하세요
# SELECT date_format(end_date, "%Y-%m-%d"), date_format(start_date, "%Y-%m-%d")
# select datediff(end_date, start_date)

select car_id, round(avg(datediff(end_date, start_date) + 1), 1) as average_duration
from CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by car_id
having average_duration >= 7
order by average_duration desc, car_id desc

# select car_id, round(avg(datediff(end_date, start_date)), 1) as average_duration
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# where car_id = 2
# group by car_id
# order by average_duration desc, car_id 

-- 2 | 20.1
# select *, avg(datediff(end_date, start_date))
# from car_rental_company_rental_history
# where car_id = 2
# group by history_id