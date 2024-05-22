/*¬ывести минимальное и максимальное количество 
студентов среди всех групп. */

select top 1 G.name,count(St.id) as count_of_students from Groups as G
join GroupsStudents as GS on G.id = GS.GroupId
join Students as St on St.id = GS.StudentId
group by G.name

union all

select top 1 G.name,count(St.id) as count_of_students from Groups as G
join GroupsStudents as GS on G.id = GS.GroupId
join Students as St on St.id = GS.StudentId
group by G.name
order by count_of_students desc



--N'количество студентов в каждой группе'