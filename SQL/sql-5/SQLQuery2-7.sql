/* Вывести названия факультетов, суммарный фонд финансирования кафедр которых больше суммарного 
фонда финансирования кафедр факультета “Компьютерные науки” */

select F.Name, sum(D.Financing) as [Суммарный фонд] from Faculties as F
join Department as D on D.FacultyId = F.id
group by F.Name
having sum(D.Financing) + 35000 > (
	select sum(D.Financing)  from Faculties as F
		join Department as D on D.FacultyId = F.id
		where F.Name = N'Компьютерные науки'
	) and not F.Name = N'Компьютерные науки'
order by F.Name