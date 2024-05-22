/* ������� �������� ����� 2-�� ����� ������� ���������� ��, ������� ����� �� 1 ���� � ������ ������(������� �������� ������ � ���������� �� ����� ������) */

select G.Name, G.Year, L.Date, datepart (ISO_WEEK, L.Date) as [����� ������], count(L.id) as [���������� ���] from Groups as G
join Department as D on D.id = G.DepartmentId
join GroupsLectures as GL on GL.GroupId = G.id
join Lectures as L on L.id = GL.LectureId
where D.Name = N'���������� ��' and G.Year = 2 and datepart (ISO_WEEK, L.Date) = (select top 1 datepart (ISO_WEEK, L.Date) from Lectures as L order by L.Date) 
group by G.Name, G.Year, L.Date
order by L.Date


