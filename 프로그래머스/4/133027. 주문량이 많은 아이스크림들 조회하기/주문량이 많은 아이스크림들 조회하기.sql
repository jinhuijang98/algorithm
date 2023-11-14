-- 코드를 입력하세요
select fh.flavor as flavor
from first_half as fh
inner join july as j
on fh.flavor = j.flavor
group by flavor
order by sum(fh.total_order) + sum(j.total_order) desc
limit 3