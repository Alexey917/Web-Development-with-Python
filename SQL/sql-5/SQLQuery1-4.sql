/* ������� �������� ��������� � ���������� ������, 
���������� � ��� */

select Room, count(id) as N'���������� ������ � ���.' from Lectures
group by Room
