select * from [овощиИфрукты]

/*Отображение всех фруктов с калорийностью в указанном диапазоне*/

select [название], [калорийность] from [овощиИфрукты]
where [тип] = 'фрукт' and [калорийность] between 70 and 100;