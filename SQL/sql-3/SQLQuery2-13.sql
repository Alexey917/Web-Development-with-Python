select * from Teachers

/*������� ������� �����������, ������� �������� 
(����� ������ � ��������) �� ����� 1200*/

select Surname from Teachers 
where IsAssistant=1 and (Salary + Premium) <= 1200