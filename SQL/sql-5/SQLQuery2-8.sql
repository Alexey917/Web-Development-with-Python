/* ������� �������� ��������� � ������ ����� ��������������, �������� ���������� ���������� ������ 
�� ��� */

select Sb.Name, T.Name + N' ' + T.Surname as full_name, count(GL.LectureId) as [���������� ������] from Subjects as Sb
join Lectures as L on L.SubjectId = Sb.id
join Teachers as T on T.id = L.TeacherId
join GroupsLectures as GL on GL.LectureId = L.id
group by Sb.Name, T.Name + N' ' + T.Surname


