-- Verifying all the tables are present
select * from employees;
select * from job_history;
select * from jobs;
select * from departments;
 select * from locations;


-- Query1A: Select the names and job start dates of all employees who work for the department number 5.
--select E.f_name, E.l_name, JH.start_date
--from employees E 
--inner join job_history JH on E.emp_id = JH.empl_id
--where JH.dept_id = 5;


-- Query1B: Select the names, job start dates, and job titles of all employees who work for the department number 5.
--select E.f_name, E.l_name, JH.start_date, J.job_title
--from employees E 
--inner join job_history JH on E.emp_id = JH.empl_id
--inner join jobs J on JH.jobs_id = J.job_ident
--where JH.dept_id = 5;


-- Query 2A: Perform a Left Outer Join on the EMPLOYEES and DEPARTMENT tables 
-- and select employee id, last name, department id and department name for all employees
--select E.emp_id, E.l_name, D.dept_id_dep, D.dep_name
--from employees E 
--left join departments D on E.dep_id = D.dept_id_dep;


-- Query 2B: Re-write the query for 2A to limit the result set to include only the rows for employees born before 1980.
--select E.emp_id, E.l_name, D.dept_id_dep, D.dep_name
--from employees E 
--left join departments D on E.dep_id = D.dept_id_dep
--where year(E.b_date)  <  1980;


-- Query 2C: : Re-write the query for 2A to have the result set include all the
-- employees but department names for only the employees who were born before 1980.
--select E.emp_id, E.l_name, D.dept_id_dep, D.dep_name
--from employees E 
--left join departments D on E.dep_id = D.dept_id_dep and year(E.b_date)  <  1980;


-- Query 3A: Perform a Full Join on the EMPLOYEES and DEPARTMENT tables
-- and select the First name, Last name and Department name of all employees.
--select E.f_name, E.l_name, D.dep_name
--from employees E 
--full join departments D on E.dep_id = D.dept_id_dep;


-- Query 3B: Re-write Query 3A to have the result set include all employee
-- names but department id and department names only for male employees.
select E.f_name, E.l_name, D.dep_name
from employees E 
full join departments D on E.dep_id = D.dept_id_dep and E.sex = 'M';