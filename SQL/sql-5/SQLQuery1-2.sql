/* ������� ���������� ������, ������� ������ ������������� ����� ��������� */

select count(GL.LectureId) as N'���������� ������' from Groups as G
join GroupsLectures as GL on G.id = GL.GroupId
join Lectures as L on L.id = GL.LectureId
join Teachers as T on T.id = L.TeacherId
where T.Surname = N'���������' and T.Name = N'����' 