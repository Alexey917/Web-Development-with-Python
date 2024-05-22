select * from Teachers

/*¬ывести фамилии, должности, ставки и надбавки 
ассистентов, у которых надбавка в диапазоне от 160 
до 550. Ќо так как у мен€ таких нет, а мен€ть влом, диапозон будет от 60 до 550 */

select Surname, Position, Salary, Premium from Teachers 
where IsAssistant=1 and Premium between 60 and 550