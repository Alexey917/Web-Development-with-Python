/* ������� ���������� ������ � ������ ���� ������ */

select L.Date, datepart (ISO_WEEK, L.Date) as [����� ������], datepart (WEEKDAY, L.Date) as [���� ������], count(L.id) as [���������� ������] from Lectures as L
join Teachers as T on T.id = L.TeacherId
join Subjects as Sb on Sb.id = L.SubjectId
group by  L.Date
order by [����� ������]
-- �� - 1, �� - 7
