select * from Teachers

/*������� ������� ����������� �� ������� ������ 550 
��� ��������� ������ 200*/

select Surname from Teachers 
where IsAssistant=1 and (Salary < 550 or Premium < 200)