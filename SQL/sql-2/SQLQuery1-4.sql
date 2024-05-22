select * from [овощиИфрукты]

/*Отображение всех овощей и фруктов в кратком описании, которых есть указанное слово. Например, 
слово: семейства*/

select * from [овощиИфрукты]
where [тип] in ('овощ', 'фрукт') and [краткое содержание] like '%семейства%';