/* ¬ывести количество зан€тий, проводимых в аудитории У201 */

select count(Room) as N' оличество зан€тий в 201 ауд.' from Lectures
where Room = 201