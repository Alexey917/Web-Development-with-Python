/* Вывести количество лекций для каждой пары преподаватель-аудитория */

select L.Room, T.Name + N' ' + T.Surname as [Преподаватель], count(L.id) as [Количество лекций] from Lectures as L
join GroupsLectures as GL on L.id = GL.LectureId
join Groups as G on G.id = GL.GroupId
join Department as D on D.id = G.DepartmentId
join Faculties as F on F.id = D.FacultyId
join Subjects as Sb on Sb.id = L.SubjectId
join Teachers as T on L.TeacherId = T.id
group by L.Room, T.Surname, T.Name
