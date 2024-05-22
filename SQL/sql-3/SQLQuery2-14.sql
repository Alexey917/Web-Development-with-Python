select * from Groups

/*Вывести названия групп 5-го курса, имеющих рейтинг 
в диапазоне от 2 до 4*/

select Name from Groups 
where Year=5 and Rating between 2 and 4