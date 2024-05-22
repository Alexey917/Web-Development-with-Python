/* Вывести названия групп, имеющих рейтинг(средний 
рейтинг всех студентов группы) больше, чем рейтинг 
группы “16ИФ”. */

select G.Name from Groups as G
join GroupsStudents as GS on GS.GroupId = G.id
join Students as St on St.id = GS.StudentId
group by G.Name
having avg(St.Rating) > (
select avg(St.Rating) from Groups as G
join GroupsStudents as GS on GS.GroupId = G.id
join Students as St on St.id = GS.StudentId
where G.Name = N'16ИФ'
group by G.Name
)

