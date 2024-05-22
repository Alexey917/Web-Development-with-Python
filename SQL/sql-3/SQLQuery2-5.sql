select * from Teachers

/* Вывестифамилии преподавателей, которые являются 
профессорами и ставка которых превышает 1050 */

select Surname  from Teachers 
where IsProfessor=1 and Salary > 1050