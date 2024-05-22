select * from Faculties

/*  Вывести таблицу факультетов в виде одного поля в следующем формате:
"The dean of faculty [faculty] is [dean]." */

select N'Декан факультета' + N' ' + Name + N':  ' + Dean 
as [The dean of faculty] from Faculties