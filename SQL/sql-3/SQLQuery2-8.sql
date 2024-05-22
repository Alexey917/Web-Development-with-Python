select * from Teachers

/* Вывести фамилии и должности преподавателей, которые не являются профессорами */

select Surname, Position from Teachers 
where not IsProfessor=1