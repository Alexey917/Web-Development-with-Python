select * from Department

/* ¬ывести названи€ кафедр, фонд финансировани€ 
которых меньше 11000 или больше 25000 */

select Name  from Department 
where Financing not between 11000 and 25000