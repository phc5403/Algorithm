-- 코드를 입력하세요
SELECT a.apnt_no, p.pt_name, p.pt_no, a.mcdp_cd, d.dr_name, a.apnt_ymd
from patient p join doctor d join appointment a
on p.pt_no = a.pt_no and d.dr_id = a.mddr_id
where a.mcdp_cd = "CS" and date_format(apnt_ymd, "%Y-%m-%d") = "2022-04-13" and
apnt_cncl_yn = "N"
order by a.apnt_ymd