-- select * from petsale;

-- Getting the sum of  QUANTITY
-- select sum(quantity) from petsale;

-- Using max to get the max SALEPRICE
-- select max(saleprice) from petsale;

-- Using min to get the min ID where ANIMAL is Dog
-- select min(ID) from petsale where animal='Dog';

-- Using Average for SALEPRICE
-- select avg(saleprice) from petsale;

-- Performing mathematical operations and then using aggregate functions
-- select avg(saleprice / quantity) from petsale where animal='Dog';

-- Round up or down every value in SALEPRICE
-- select round(saleprice) from petsale;

-- Retrieve the length of each value in ANIMAL
-- select length(animal) from petsale;

-- Retrieve ANIMAL values in UPPERCASE;
-- select ucase(animal) from petsale;

-- Use the function in a where clause
-- select * from petsale where lcase(animal) = 'cat';

-- Use the DISTINCT() function to get unique values;
-- select distinct(ucase(animal)) from petsale;

-- Extract the DAY portion from a date
-- select day(saledate) from petsale where animal='Cat';

-- Get the number of sales during the month of May
-- select count(quantity) from petsale where month(saledate) = '06';

-- What date is it 3 days after each sale date
-- select (saledate + 3 days) from petsale;

-- Find how many days have passed since each SALEDATE till now
select (current_date - SALEDATE) from PETSALE;

