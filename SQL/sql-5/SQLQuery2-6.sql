/*  Вывести названия групп, имеющих рейтинг(средний 
рейтинг всех студентов группы) меньше, чем минимальный рейтинг групп 5-го курса. */

select G.Name from Groups as G
join GroupsStudents as GS on GS.GroupId = G.id
join Students as St on St.id = GS.StudentId
group by G.Name
having avg(St.Rating) < (
	select top 1 avg(St.Rating) as [mid] from Groups as G
		join GroupsStudents as GS on GS.GroupId = G.id
		join Students as St on St.id = GS.StudentId 
		where G.Year = 5
		group by G.Name
		order by mid
	)



