Table: Student

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
+-------------+---------+
This table may contain duplicate rows.
Each row of this table indicates the name of a student and the continent they came from.
 

A school has students from Asia, Europe, and America.

Write a solution to pivot the continent column in the Student table so that each name is sorted alphabetically and displayed underneath its corresponding continent. The output headers should be America, Asia, and Europe, respectively.

The test cases are generated so that the student number from America is not less than either Asia or Europe.

The result format is in the following example.

 

Example 1:

Input: 
Student table:
+--------+-----------+
| name   | continent |
+--------+-----------+
| Jane   | America   |
| Pascal | Europe    |
| Xi     | Asia      |
| Jack   | America   |
+--------+-----------+
Output: 
+---------+------+--------+
| America | Asia | Europe |
+---------+------+--------+
| Jack    | Xi   | Pascal |
| Jane    | null | null   |
+---------+------+--------+
 

Follow up: If it is unknown which continent has the most students, could you write a solution to generate the student report?

Solution:
with cte_america as(
    select name as America, row_number() over(
        order by name
    ) as join_rank
    from student
    where continent ='America'
    order by name 
),
cte_asia as(
    select name as Asia, row_number() over(
        order by name
    ) as join_rank
    from student
    where continent ='Asia'
    order by name 
),
cte_europe as(
    select name as Europe, row_number() over(
        order by name
    ) as join_rank
    from student
    where continent ='Europe'
    order by name 
)

select America,Asia,Europe
from cte_america a
left join cte_asia asia
on a.join_rank=asia.join_rank
left join cte_europe e
on a.join_rank=e.join_rank
order by a.join_rank


---------------If we dont know the max continent:



with cte1 as 
(select 
row_number() over (partition by continent order by name) as rk,
name, 
continent
from Student)
select
max(case when continent = 'America' then name end) as America,
max(case when continent = 'Asia' then name end) as Asia,
max(case when continent = 'Europe' then name end) as Europe
from cte1
group by rk
order by rk