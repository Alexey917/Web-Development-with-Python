select * from Teachers

/* ������� ������� � ��������� ��������������, ������� �� �������� ������������ */

select Surname, Position from Teachers 
where not IsProfessor=1