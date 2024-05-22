/* ������� �������� �����������, ��������� ���� �������������� ������ ������� ������ ���������� 
����� �������������� ������ ���������� ������������� ����� */

select F.Name, sum(D.Financing) as [��������� ����] from Faculties as F
join Department as D on D.FacultyId = F.id
group by F.Name
having sum(D.Financing) + 35000 > (
	select sum(D.Financing)  from Faculties as F
		join Department as D on D.FacultyId = F.id
		where F.Name = N'������������ �����'
	) and not F.Name = N'������������ �����'
order by F.Name