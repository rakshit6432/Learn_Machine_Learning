select * from employees;
select * from departments;

-- Retrieve the list of employees who earn more than the average salary
-- select * from employees where salary > (select avg(salary) from employees);

-- select avg salary and emp_id, salary from employees
--select emp_id, salary,
--	(select avg(salary) as avg_salary from employees) from employees;

-- Retrieve only the employee records that correspond to departments in the departments table:
--select * from employees
--	where dep_id in (select dept_id_dep from departments);

--To retrieve only the list of employees from a specific location:
--- Employees table doesn't contain location information
--- Need to get location info from departments table
--select * from employees
--	where dep_id in (select dept_id_dep from departments where loc_id='L0002');

-- To retrieve the department id and name for employees who earn more than $70,000:
select * from employees
	where dep_id in (select dept_id_dep from departments where salary > 70000);

