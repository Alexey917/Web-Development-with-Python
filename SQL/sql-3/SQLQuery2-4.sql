select * from Faculties

/*  ������� ������� ����������� � ���� ������ ���� � ��������� �������:
"The dean of faculty [faculty] is [dean]." */

select N'����� ����������' + N' ' + Name + N':  ' + Dean 
as [The dean of faculty] from Faculties