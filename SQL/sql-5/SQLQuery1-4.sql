/* Вывести названия аудиторий и количество лекций, 
проводимых в них */

select Room, count(id) as N'Количество лекций в ауд.' from Lectures
group by Room
