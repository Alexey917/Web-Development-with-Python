select * from Faculties

/*  Вывести названия факультетов кроме факультета 
“Computer Science” */

select Name from Faculties 
where not Name=N'Компьютерные науки' 