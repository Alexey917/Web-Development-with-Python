select * from Teachers

/*������� �������, ���������, ������ � �������� 
�����������, � ������� �������� � ��������� �� 160 
�� 550. �� ��� ��� � ���� ����� ���, � ������ ����, �������� ����� �� 60 �� 550 */

select Surname, Position, Salary, Premium from Teachers 
where IsAssistant=1 and Premium between 60 and 550