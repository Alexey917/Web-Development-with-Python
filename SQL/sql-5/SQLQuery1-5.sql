/* ������� ���������� ���������, ���������� ������ 
������������� ������� ��������� */

select count(St.id) as N'���������� ���������' from Teachers as T
join Lectures as L on L.TeacherId = T.id
join GroupsLectures as GL on GL.LectureId = L.id
join Groups as G on G.id = GL.GroupId
join GroupsStudents as GS on G.id = GS.GroupId
join Students as St on St.id = GS.StudentId
where T.Name = N'������' and T.Surname = N'���������'
