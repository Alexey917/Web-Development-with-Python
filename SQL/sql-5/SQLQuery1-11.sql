/* Вывести номера аудиторий и количество кафедр, чьи 
лекции в них читаются */

select L.Room, count(distinct D.Name) as [Количество кафедр] from Lectures as L
join GroupsLectures as GL on L.id = GL.LectureId
join Groups as G on G.id = GL.GroupId
join Department as D on D.id = G.DepartmentId
group by L.Room
