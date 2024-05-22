/* Вывести количество лекций, которые читает преподаватель “Илья Дворников” */

select count(GL.LectureId) as N'Количество лекций' from Groups as G
join GroupsLectures as GL on G.id = GL.GroupId
join Lectures as L on L.id = GL.LectureId
join Teachers as T on T.id = L.TeacherId
where T.Surname = N'Дворников' and T.Name = N'Илья' 