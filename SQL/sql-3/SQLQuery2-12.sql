select * from Department

/*Вывести названия кафедр, которые в алфавитном располагаются до "Software developпment". Выводимое поле должно иметь название "Name 
of Department"*/

select top (select id 
from Department
where Name=N'Разработка ПО') Name as [Name of Department] from Department 
