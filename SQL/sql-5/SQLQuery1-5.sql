/* ¬ывести количество студентов, посещающих лекции 
преподавател€ У ирилл яваскриптФ */

select count(St.id) as N' оличество студентов' from Teachers as T
join Lectures as L on L.TeacherId = T.id
join GroupsLectures as GL on GL.LectureId = L.id
join Groups as G on G.id = GL.GroupId
join GroupsStudents as GS on G.id = GS.GroupId
join Students as St on St.id = GS.StudentId
where T.Name = N' ирилл' and T.Surname = N'яваскрипт'
