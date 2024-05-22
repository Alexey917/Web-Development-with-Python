/* Вывести названия дисциплин и полные имена преподавателей, читающих наибольшее количество лекций 
по ним */

select Sb.Name, T.Name + N' ' + T.Surname as full_name, count(GL.LectureId) as [Количество лекций] from Subjects as Sb
join Lectures as L on L.SubjectId = Sb.id
join Teachers as T on T.id = L.TeacherId
join GroupsLectures as GL on GL.LectureId = L.id
group by Sb.Name, T.Name + N' ' + T.Surname


