/* Вывести полные имена преподавателей и количество 
читаемых ими дисциплин */

select T.name + N'' + T.Surname as N'Полное имя', count(SubjectId) as N'Количество читаемых дисциплин' from Lectures as L
join Teachers as T on T.id = L.TeacherId
join Subjects as Sb on Sb.id = L.SubjectId
group by T.name, T.Surname