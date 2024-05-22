/* Вывести название дисциплины, по которому читается 
меньше всего лекций */

select top 1 Sb.Name from Subjects as Sb
join Lectures as L on L.SubjectId = Sb.id
join Teachers as T on T.id = L.TeacherId
join GroupsLectures as GL on GL.LectureId = L.id
group by Sb.Name, T.Name + N' ' + T.Surname
order by count(GL.LectureId)