select * from Teachers

/* Âûâåñòè äëÿ ïðåïîäàâàòåëåé èõ ôàìèëèþ, ïðîöåíò 
ñòàâêè ïî îòíîøåíèþ ê íàäáàâêå è ïðîöåíò ñòàâêè 
ïî îòíîøåíèþ ê çàðïëàòå (ñóììà ñòàâêè è íàäáàâêè) */

select Surname, (Salary*100)/Premium as [% ñòàâêè ê íàäáàâêå], 
(Salary*100)/(Premium + Salary) as [% ñòàâêè ê çàðïëàòå] from Teachers 