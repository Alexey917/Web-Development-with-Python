select * from Teachers

/*¬ывести фамилии ассистентов со ставкой меньше 550 
или надбавкой меньше 200*/

select Surname from Teachers 
where IsAssistant=1 and (Salary < 550 or Premium < 200)