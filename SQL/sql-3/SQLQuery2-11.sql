select * from Teachers

/*������� ������� � ��������� ��������������, ������� ���� ������� �� ������ �� 01.01.2000 */

select Surname, Position from Teachers 
where EmploymentDate < N'20000101'