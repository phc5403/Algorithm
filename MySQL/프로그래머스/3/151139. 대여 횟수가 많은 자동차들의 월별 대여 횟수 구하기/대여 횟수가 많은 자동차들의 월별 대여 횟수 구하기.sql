WITH car_rentals AS (
    SELECT 
        CAR_ID,
        COUNT(*) AS TOTAL_RENTALS
    FROM 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE 
        START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY 
        CAR_ID
    HAVING 
        TOTAL_RENTALS >= 5
),
monthly_rentals AS (
    SELECT 
        DATE_FORMAT(START_DATE, '%Y-%m') AS MONTH_KEY,
        MONTH(START_DATE) AS MONTH,
        CAR_ID,
        COUNT(*) AS RECORDS
    FROM 
        CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE 
        START_DATE BETWEEN '2022-08-01' AND '2022-10-31'
    GROUP BY 
        DATE_FORMAT(START_DATE, '%Y-%m'), CAR_ID
)
SELECT 
    mr.MONTH,
    mr.CAR_ID,
    mr.RECORDS
FROM 
    monthly_rentals mr
JOIN 
    car_rentals cr
ON 
    mr.CAR_ID = cr.CAR_ID
ORDER BY 
    mr.MONTH ASC,
    mr.CAR_ID DESC;
