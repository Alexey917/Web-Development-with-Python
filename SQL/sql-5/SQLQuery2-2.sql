/* Вывести названия групп 2-го курса кафедры Разработка ПО, которые имеют по 1 паре в первую неделю(Условие пришлось менять в зависимост от своих данных) */

select G.Name, G.Year, L.Date, datepart (ISO_WEEK, L.Date) as [номер недели], count(L.id) as [количество пар] from Groups as G
join Department as D on D.id = G.DepartmentId
join GroupsLectures as GL on GL.GroupId = G.id
join Lectures as L on L.id = GL.LectureId
where D.Name = N'Разработка ПО' and G.Year = 2 and datepart (ISO_WEEK, L.Date) = (select top 1 datepart (ISO_WEEK, L.Date) from Lectures as L order by L.Date) 
group by G.Name, G.Year, L.Date
order by L.Date


