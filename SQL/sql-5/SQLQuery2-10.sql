/* Вывести количество студентов и читаемых дисциплин на кафедре Разработка ПО  */

select count(distinct St.id) as [Количество студентов], count(distinct Sb.id) as [Читаемые дисциплины] from Subjects as Sb
join Lectures as L on L.SubjectId = Sb.id
join Teachers as T on T.id = L.TeacherId
join GroupsLectures as GL on GL.LectureId = L.id
join Groups as G on G.id = GL.GroupId
join GroupsStudents as GS on GS.GroupId = G.id
join Students as St on St.id = GS.StudentId
join Department as D on D.id = G.DepartmentId
where D.Name = N'Разработка ПО'


--count(St.id) as [Количество студентов], count(Sb.id) as [Читаемые дисциплины]