select * from Teachers

/*Вывести фамилии и должности преподавателей, которые были приняты на работу до 01.01.2000 */

select Surname, Position from Teachers 
where EmploymentDate < N'20000101'