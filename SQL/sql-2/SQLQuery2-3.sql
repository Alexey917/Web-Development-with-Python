select * from [овощиИфрукты]

/* Показать количество овощей и фруктов заданного 
цвета*/

select count(*) as [красные овощи и фрукты] from [овощиИфрукты]
where [цвет] = 'красный'
