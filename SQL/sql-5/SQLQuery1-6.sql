/* Вывести среднюю ставку преподавателей факультета 
“Компьютерные науки”. */

select avg(distinct T.Salary) as N'Средняя ставка' from Teachers as T
join Lectures as L on L.TeacherId = T.id
join GroupsLectures as GL on GL.LectureId = L.id
join Groups as G on G.id = GL.GroupId
join Department as D on D.id = G.DepartmentId
join Faculties as F on F.id  = D.FacultyId
where F.Name = N'Компьютерные науки'

