/* Вывести названия групп, у которых больше одного 
куратора. (нет таких) */

select G.Name, C.Name, C.Surname from Curators as C
join GroupsCurators as GC on GC.CuratorId = C.id
join Groups as G on G.id = GC.GroupId
order by G.Name
