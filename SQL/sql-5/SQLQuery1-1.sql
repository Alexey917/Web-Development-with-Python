/* Вывести количество преподавателей кафедры Разработка ПО */

select count(T.Name) as N'Количество преподавателей кафедры Разработка ПО' from Department as D
join Groups as G on D.id = G.DepartmentId
join GroupsLectures as GL on G.id = GL.GroupId
join Lectures as L on L.id = GL.LectureId
join Teachers as T on T.id = L.TeacherId
where D.Name = N'Разработка ПО' 