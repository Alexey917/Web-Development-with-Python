/* Вывести количество лекций в каждый день недели */

select L.Date, datepart (ISO_WEEK, L.Date) as [номер недели], datepart (WEEKDAY, L.Date) as [день недели], count(L.id) as [количество лекций] from Lectures as L
join Teachers as T on T.id = L.TeacherId
join Subjects as Sb on Sb.id = L.SubjectId
group by  L.Date
order by [номер недели]
-- Пн - 1, Вс - 7
