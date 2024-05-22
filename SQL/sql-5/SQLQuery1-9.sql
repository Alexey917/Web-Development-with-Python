/* ������� ������ ����� �������������� � ���������� 
�������� ��� ��������� */

select T.name + N'' + T.Surname as N'������ ���', count(SubjectId) as N'���������� �������� ���������' from Lectures as L
join Teachers as T on T.id = L.TeacherId
join Subjects as Sb on Sb.id = L.SubjectId
group by T.name, T.Surname