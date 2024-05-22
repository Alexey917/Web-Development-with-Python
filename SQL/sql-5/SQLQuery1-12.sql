/* Вывести названия факультетов и количество дисциплин, которые на них читаются */

select F.Name, count(distinct Sb.Name) as [Количество дисциплин] from Lectures as L
join GroupsLectures as GL on L.id = GL.LectureId
join Groups as G on G.id = GL.GroupId
join Department as D on D.id = G.DepartmentId
join Faculties as F on F.id = D.FacultyId
join Subjects as Sb on Sb.id = L.SubjectId
group by F.Name
