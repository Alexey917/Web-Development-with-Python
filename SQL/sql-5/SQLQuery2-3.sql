/* ������� �������� �����, ������� �������(������� 
������� ���� ��������� ������) ������, ��� ������� 
������ �16�Ԕ. */

select G.Name from Groups as G
join GroupsStudents as GS on GS.GroupId = G.id
join Students as St on St.id = GS.StudentId
group by G.Name
having avg(St.Rating) > (
select avg(St.Rating) from Groups as G
join GroupsStudents as GS on GS.GroupId = G.id
join Students as St on St.id = GS.StudentId
where G.Name = N'16��'
group by G.Name
)

