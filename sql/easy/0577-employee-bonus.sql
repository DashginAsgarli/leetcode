# Write your MySQL query statement below
select name, bonus 
from Employee  as em
left join Bonus as b
on em.empId = b.empId
where bonus is null or bonus < 1000  