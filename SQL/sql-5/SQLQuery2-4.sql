/*  ������� ������� � ����� ��������������, ������ 
������� ���� ������� ������ ����������� (������� � ������ 1000, ����� ���� ���� �� �������) */

select T.Surname, Name from Teachers as T
where (T.Salary + 1000 > (select avg(T.Salary) from Teachers as T where T.IsProfessor = 1)) and  not T.IsProfessor = 1


