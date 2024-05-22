/* Вывести номера корпусов, если суммарный фонд финансирования расположенных в них кафедр превышает 100000 */

select Building, sum(Financing) as [Суммарный фонд] from Department
group by Building
having sum(Financing) > 100000
