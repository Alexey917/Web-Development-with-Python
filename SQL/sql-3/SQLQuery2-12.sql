select * from Department

/*������� �������� ������, ������� � ���������� ������������� �� "Software develop�ment". ��������� ���� ������ ����� �������� "Name 
of Department"*/

select top (select id 
from Department
where Name=N'���������� ��') Name as [Name of Department] from Department 
