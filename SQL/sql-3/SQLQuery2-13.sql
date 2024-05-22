select * from Teachers

/*Вывести фамилии ассистентов, имеющих зарплату 
(сумма ставки и надбавки) не более 1200*/

select Surname from Teachers 
where IsAssistant=1 and (Salary + Premium) <= 1200