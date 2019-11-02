<h1>Week 1 - Introduction to Databases and Basic SQL</h1>



<h2>Introduction to Databases</h2>

__SQL__ is a language used for relational databases to query or get data out of a database. SQL is short for its original name __Structured Query Language__. SQL is a language used for a database to query data.

__Data__ is a collection of facts in the form of words, numbers or even pictures. Data is one of the most critical assets of any business. Data is important, so it needs to be secure and it needs to be stored and accessed quickly. The answer is a database.

A __Database__ is a repository of data. It is a program that stores data. A database also provides the functionality for adding, modifying and querying that data. There are different kinds of databases of different requirements.

The data can be stored in various forms. When data is stored in tabular form, the data is organized in tables like in a spreadsheet, it is a __relational database__. A table is a collection of related things like a list of employees or a list of book authors. In a relational database, you can form relationships between tables.

A set of software tools for the data in the database is called a __database management system__ or __DBMS__ for short. For relational databases, it's called a _relational database management system_ or _RDBMS_. RDBMS is a set of software tools that controls the data such as access, organization and storage. Examples of relational database management systems are, my SQL, Oracle Database, DB2 Warehouse on Cloud and DB2 Express C.

There are five simple SQL commands:
- __CREATE__ a table,
- __INSERT__ data to populate the table,
- __SELECT__ data from the table,
- __UPDATE__ data in the table,
- __DELETE__ data from the table.


<h2>Basic SQL</h2>


- _Data definition language_ or DDL statements are used to define, change, or drop data.
- _Data manipulation language_ or DML statements are used to read and modify data.
- The _primary key_ of a relational table uniquely identifies each tuple or row in a table.


<h3>CREATE Table</h3>

The CREATE statement is one of the data definition language statements. Data definition language statements or DDL statements are used to create database objects.

The general syntax to create a table:

```sql
create table TABLENAME (
    COLUMN1 datatype,
    COLUMN2 datatype,
    COLUMN3 datatype,
    ...
);
```

To create a table called TEST with two columns - ID of type integer, and Name of type varchar, we could create it using the following SQL statement:

```sql
create table TEST (
    ID integer,
    Name varchar(30)
);
```

Additional keywords in a create table statement:

```sql
create table COUNTRY (
    ID int NOT NULL,
    CCODE char(2),
    NAME varchar(30)
    PRIMARY KEY (ID)
)
```

In the above example:
    - "NOT NULL" -  it cannot contain a NULL or an empty value.
    - PRIMARY KEY - the database does not allow Primary Keys to have NULL values and is a unique identifier in a table

To drop a table:

```sql
drop table COUNTRY;
```

<h3>SELECT Table</h3>

After creating a table and inserting data into the table, we want to see the data. To see the data, we use the SELECT statement. The SELECT statement is a data manipulation language statement and is called a query, and the output we get from executing this query is called a result set or a result table.

The general syntax of SELECT statements is:

```sql
select COLUMN1, COLUMN2, ... from TABLE1;
```

To retrieve a list of all country names and their IDs from the COUNTRY table we would issue:

```sql
select ID, NAME from COUNTRY;
```

To retrieve all columns from the COUNTRY table we could use "*" instead of specifying individual column names:

```sql
select * from COUNTRY;
```

The WHERE clause can be added to your query to filter results or get specific rows of data. To retrieve data for all rows in the COUNTRY table where the ID is less than 5:

```sql
select * from COUNTRY WHERE ID < 5;
```

In case of character based columns the values of the predicates in the where clause need to be enclosed in single quotes. To retrieve the data for the country with country code "CA" we would issue:

```sql
select * from COUNTRY WHERE CCODE = 'CA';
```

<h3>COUNT, DISTINCT, LIMIT</h3>

__COUNT:__

COUNT() is a built in function that retrieves the number of rows matching the query criteria.

To get the number of rows in a table:

```sql
select COUNT(*) from tablename
```

For example to get rows in the MEDALS table where Country is Canada:

```sql
select COUNT(COUNTRY) from MEDALS
    where COUNTRY='CANADA'
```

__DISTINCT:__

DISTINCT is used to remove duplicate values from a result set.

To retrieve unique values in a column:

```sql
select DISTINCT columnname from tablename
```

For example to get the list of unique countries that recieved GOLD medals:

```sql
select DISTINCT COUNTRY from MEDALS
    where MEDALTYPE = 'GOLD'
```

__LIMIT:__

LIMIT is used for restricting the number of rows retrieved from the database.

To retrieve just the first 10 rows in a table:

```sql
select * from tablename LIMIT 10
```

For example to retrieve 5 rows in the MEDALS table for a particular year:

```sql
select * from MEDALS
    where YEAR = 2019 LIMIT 5
```

<h3>INSERT Statement</h3>

To insert data into a table, we use the INSERT statement. The INSERT statement is used to add new rows to a table. The INSERT statement is one of the data manipulation language statements.

The general syntax of INSERT statements is:

```sql
INSERT INTO tablename
    (Column1, Column2, ...)
VALUES
    (Value1, Value2, ...)
```

For example:

```sql
INSERT INTO AUTHOR
    (AUTHOR_ID, LASTNAME, FIRSTNAME, EMAIL)
VALUES
    ('A1', 'Mithrakumar', 'Mukesh', 'mukesh@mukeshmithrakumar.com')
```

<h3>UPDATE and DELETE Statements</h3>

__UPDATE Statement:__

The data in a table can be altered with the UPDATE statement. The UPDATE statement is one of the data manipulation language or DML statements.

The general syntax of UPDATE statements is:

```sql
UPDATE tablename
SET ColumnName = Value
WHERE condition
```

For example:

```sql
UPDATE AUTHOR
SET LASTNAME = 'Alia'
    FIRSTNAME = 'Bhatt'
WHERE AUTHOR_ID = 'A2'
```

Note that if you do not specify the WHERE clause, all the rows in the table will be updated.

__DELETE Statement:__

The rows are removed with the DELETE statement. The DELETE statement is one of the data manipulation language statements used to read and modify data.

The general syntax of UPDATE statements is:

```sql
DELETE FROM tablename
WHERE condition
```

For example:

```sql
DELETE from AUTHOR
WHERE AUTHOR_ID IN ('A2', 'A3')
```

Note that if you do not specify the WHERE clause, all the rows in the table will be removed.


<h2>Relational Database Concepts</h2>


<h3>Information and Data Models</h3>

The figure below illustrates the relationship between an information model and a data model.

<img src="../5. Databases and SQL for Data Science/images/Information_and_Data_Models.png">

An _information model_ is an abstract formal representation of entities that includes their properties, relationships, and the operations that can be performed on them. The entities being modeled can be from the real world, such as a library.

Information models and data models are different and serve different purposes. An information model is at the conceptual level and defines relationships between objects. _Data models_ are defined in a more concrete level, are specific and include details. A data model is the blueprint of any database system

There are several types of information models. The most familiar is the _hierarchical_, typically used to show organization charts. The hierarchical model organizes its data using a tree structure.

The _relational model_ is the most used data model for databases, because this model allows for data independence. Data is stored in simple data structure tables. This provides logical data independence, physical data independence, and physical storage independence.

An _entity-relationship_ data model or ER data model, is an alternative to a relational data model. An entity-relationship model proposes thinking of a database as a collection of entities, rather than being used as a model on its own. The ER model is used as a tool to design relational databases. In the ER model, entities are objects that exist independently of any other entities in the database. The building blocks of an ER diagram are entities and attributes. Entities have attributes, which are the data elements that characterize the entity. Attributes tell us more about the entity. A book is an example of an entity, the book title, the edition of the book, the year the book was written etc are its attributes. The entity book becomes a table in the database, and the attributes become the columns in the table.

<img src="../5. Databases and SQL for Data Science/images/book_table.png">

<h3>Types of Relationships</h3>

The building blocks of a relationship are:

<img src="../5. Databases and SQL for Data Science/images/entity_bb.png">

<img src="../5. Databases and SQL for Data Science/images/entity_relationships.png">

<img src="../5. Databases and SQL for Data Science/images/one_to_one_relationship.png">

<img src="../5. Databases and SQL for Data Science/images/one_to_many_relationship.png">

<img src="../5. Databases and SQL for Data Science/images/many_to_many_relationship.png">

<h3>Mapping Entities to Tables</h3>

<img src="../5. Databases and SQL for Data Science/images/erd_to_table.png">

<img src="../5. Databases and SQL for Data Science/images/mapping_erd_to_table.png">

<h3>Relational Model Concepts</h3>

The relational model was first proposed in 1970, and is based on a mathematical model and mathematical terms. The building blocks of the _relational model_ are _relation_ and _sets_. The relational model of data is based on the concept of relation. A relation is a mathematical concept based on the idea of sets. A set is unordered collection of distinct elements. It is a collection of items of the same type. It would have no order and no duplicates. A relational database is a set of relations.

A relation is also the mathematical term for a table. A table is a combination of rows and columns. A relation is made up of two parts, _relational schema_ and _relational instance_. A relational schema specifies the name of a relation and the attributes. For example for an entity Author:

<img src="../5. Databases and SQL for Data Science/images/author_entity.png">

Author is the name of the relation. Author_ ID is an attribute which can hold the data type char, which is a character string of a fixed length. Likewise, lastname, firstname, email and city have the data type varchar, which is a character string of a variable length. The last attribute country, also has a data type of char. This constitutes the _relational schema_.

A _relational instance_ is a table made up of the attributes or columns and the tuples or rows. The columns are the _attributes_ or _fields_. The rows are _tuples_. _Degree_ refers to the number of attributes or columns in a relation. _Cardinality_ refers to the number of tuples or rows.

<img src="../5. Databases and SQL for Data Science/images/relation_instance.png">

In this example, the degree is six because there are six columns, and the cardinality is five because there are five tuples or rows.

<h3>Additional Information</h3>

__Create Schema:__

A SQL schema is identified by a schema name, and includes a authorization identifier to indicate the user or account who owns the schema. Schema elements include tables, constraints, views, domains and other constructs that describe the schema.

A schema is created using the CREATE SCHEMA statement. The data types used can be: numeric, character-string, bit-string, Boolean, DATE, timestamp, etc. For example,

```sql
CREATE SCHEMA LIBRARY AUTHORIZATION 'Mukesh'
```

__CREATE TABLE Statement:__

The CREATE TABLE statement includes these clauses:
- DEFAULT
- CHECK

Use the DEFAULT clause in the CREATE TABLE statement to specify the default value for the database server to insert into a column when no explicit value for the column is specified.

Use the CHECK clause to designate conditions that must be met before data can be assigned to a column during an INSERT or UPDATE statement.

During an insert or update, if the check constraint of a row evaluates to false, the database server returns an error. The database server does not return an error if a row evaluates to NULL for a check constraint. In some cases, you might want to use both a check constraint and a NOT NULL constraint.

__SELECT Statement:__

The basic structure of the SELECT statement is formed from three clauses: SELECT, FROM and WHERE.
- `<attribute list>` is a list of attribute names whose values are to be retrieved by the query
- `<table list>` is a list of the relation names required to process the query
- `<condition>` is a conditional(Boolean) expression that identifies the tuples to be retrieved by the query

In situations where you might want to use multiple IF-THEN-ELSE statements, you can often use a single SELECT statement instead. The SELECT statement allows a CLIST to select actions from a list of possible actions. An action consists of one or more statements or commands. The SELECT statement has the following syntax, ending with the END statement. You can use the SELECT statement with or without the initial test expression.

```sql
SELECT [test expression]
WHEN [expression1]
...
(action)
...
WHEN [expression2]
WHEN [expression3]
...
[OTHERWISE]
...
(action)
...
END
```



<h1>Week 2 - Advanced SQL</h1>



<h2>String Patterns, Ranges, Sorting, and Grouping</h2>


<h3>Using String Patterns, Ranges</h3>

__Retrieving rows from a table__

<img src="../5. Databases and SQL for Data Science/images/retrieving_select.png">

__Retrieving rows using a String Pattern__

<img src="../5. Databases and SQL for Data Science/images/retrieving_select_pattern.png">

__Retrieving rows using a Range__

<img src="../5. Databases and SQL for Data Science/images/retrieving_select_range.png">

__Retrieving rows using a Set of Values__

<img src="../5. Databases and SQL for Data Science/images/retrieving_select_set.png">

<h3>Sorting Result Sets</h3>

To display the result of a query set in alphabetical order, we add the order by clause to the select statement.

<img src="../5. Databases and SQL for Data Science/images/order_by.png">

To sort in descending order, use the key word" desc."

<img src="../5. Databases and SQL for Data Science/images/order_by_desc.png">

Another way of specifying the sort column is to indicate the column sequence number. For example, instead of specifying the column name pages, the number two is used:

<img src="../5. Databases and SQL for Data Science/images/order_by_seq.png">

<h3>Grouping Result Sets</h3>

__Eliminating duplicates using DiSTINCT clause__

<img src="../5. Databases and SQL for Data Science/images/select_distinct.png">

__GROUP BY clause__

<img src="../5. Databases and SQL for Data Science/images/group_by.png">

The "as count" keyword assigns a column name to the result set.

__Restricting the result set using HAVING clause__

<img src="../5. Databases and SQL for Data Science/images/group_by_having.png">

Note that the "where" clause is for the entire result set, but the "having" clause works only with the "group by" clause.


<h2>Functions, Sub-Queries, Multiple Tables</h2>


<h3>Built-in Database Functions</h3>

__Aggregate functions__

An aggregate function takes a collection of light values, such as all of the values in a column, as input, and returns a single value or null. Examples of aggregate functions include: sum, minimum, maximum and average.

```sql
-- Getting the sum of SALEPRICE
select sum(SALEPRICE) as SUM_OF_SALEPRICE from PETSALE;

-- Using max to get the max QUANTITY
select max(QUANTITY) from PETSALE;

-- Using min to get the min ID where ANIMAL is Dog
select min(ID) from PETSALE where ANIMAL='Dog';

-- Using Average for SALEPRICE
select avg(SALEPRICE) from PETSALE;

-- Performing mathematical operations and then using aggregate functions
select avg(SALEPRICE / QUANTITY) from PETSALE where ANIMAL = 'Dog';
```

__Scalar and String functions__

Scalar perform operations on every input value, for example ROUND(), LENGTH(), UCASE(), LCASE()

```sql
-- Round up or down every value in SALEPRICE
select round(SALEPRICE) from PETSALE;

-- Retrieve the length of each value in ANIMAL
select length(ANIMAL) from PETSALE;

-- Retrieve ANIMAL values in UPPERCASE;
select ucase(ANIMAL) from PETSALE;

-- Use the function in a where clause
select * from PETSALE where lcase(ANIMAL) = 'cat';

-- Use the DISTINCT() function to get unique values;
select distinct(ucase(ANIMAL)) from PETSALE;
```

<h3>Date and Time Built-in Functions</h3>

<img src='../5. Databases and SQL for Data Science/images/date_datatypes.png'>

```sql
-- Extract the DAY portion from a SALEDATE
select day(SALEDATE) from PETSALE where ANIMAL='Cat';

-- Get the number of sales during the month of May
select count(*) from PETSALE where month(SALEDATE) = '05';

-- What date is it 3 days after each sale date
select (SALEDATE + 3 days) from PETSALE;

-- Special Registers:
-- CURRENT_DATE, CURRENT_TIME

-- Find how many days have passed since each SALEDATE till now
select (current_date - SALEDATE) from PETSALE;
```

<h3>Sub-Queries and Nested Selects</h3>

Sub-queries or sub selects are like regular queries but placed within parentheses and nested inside another query. This allows you to form more powerful queries than would have been otherwise possible.

```sql
select COLUMN1 from TABLE
    where COLUMN2 = (select max(COLUMN2) from TABLE));
```

_Why use sub queries?_

For example, if we want to retrieve the list of employees who earn more than the average salary:

```sql
select * from employees where salary > avg(salary);
```

The above query will result in an error, indicating an invalid use of the aggregate function. One of the limitations of built in aggregate functions like the average function, is that they cannot always be evaluated in the WHERE clause. So to evaluate a function like average in the WHERE clause:

```sql
select * from employees where salary > (select avg(salary) from employees);
```

The sub-select doesn't just have to go in the WHERE clause. It can also go in other parts of the query such as in the list of columns to be selected.

```sql
select emp_id, salary, avg(salary) as avg_salary from employees;
```

Running this query will result in an error indicating that no group by clause is specified. We can circumvent this error by using the average function in a sub-query placed in the list of the columns.

```sql
select emp_id, salary,
    (select avg(salary) as avg_salary from employees) from employees;
```

Another option is to make the sub-query be part of the FROM clause. Sub-queries like these are sometimes called derived tables or table expressions. Because the outer query uses the results of the sub-query as a data source.

```sql
select * from
    (select emp_id, f_name, l_name, dep_id from employees) as emp4all;
```

<h3>Working with Multiple Tables</h3>

There are several ways to access multiple tables in the same query. Namely:
- using Sub-queries,
- Implicit JOIN, and
- JOIN operators, such as INNER JOIN and OUTER JOIN.

__Accessing multiple tables with sub-queries:__

To retrieve only the employee records that correspond to departments in the departments table:

```sql
select * from employees
    where dep_id in
    (select dept_id_dep from department);
```

To retrieve only the list of employees from a specific location:
- Employees table doesn't contain location information
- Need to get location info from departments table

```sql
select * from employees
    where dep_id in
    (select dept_id_dep from departments
        where loc_id='L0002');
```

To retrieve the department id and name for employees who earn more than $70,000:

```sql
select dept_id_dep, dep_name from departments
    where dept_id_dep in
    (select dep_id from employees where salary > 70000);
```

__Accessing multiple tables with Implicit Join__

```sql
select * from employees, departments;
```

The above code results in a full join or Cartesian join, because every row in the first table is joined with every row in the second table. If you examine the results set, you will see more rows than in both tables individually. We can use additional operands to limit the result set.

```sql
select * from employees E, departments D
    where E.dep_id = D.dept_id_dep;
```

To see the department name for each employee:

```sql
select employees.emp_id, departments.dept_name
    from employees E, departments D
    where E.dep_id = D.dept_id_dep;
```


<h2>Relational Model Constraints</h2>


<img src='../5. Databases and SQL for Data Science/images/referencing.png'>

In the figure above, at least one author writes one book. This is a one to one relationship. To look up the author information, the book entity refers to the author entity. In a relational data model, this is called _referencing_. In relational databases, this establishes the data integrity between two relations.

A __primary key__ of a relational table uniquely identifies each row in a table. A __foreign key__ is a set of columns referring to a primary key of another table.

A table containing a primary key that is related to at least one foreign key is called a __parent table__. A table containing one or more foreign keys is called a __dependent table__. It might also be referred to as a __child table__.


<h3>Relational Model Constraints - Advanced</h3>

Within any business, data must often adhere to certain restrictions or rules. Constraints help implement the business rules. In a relational data model, data integrity can be achieved using integrity rules or constraints. The following six constraints are defined in a relational database model:

- _Entity Integrity Constraint_: This constraint prevents duplicate values in a table. To implement these constraints, indexes are used. The entity integrity constraint states that no attribute participating in the primary key of a relation is allowed to accept null values.

- _Referential Integrity Constraint_: defines relationships between tables and ensures that these relationships remain valid. The validity of the data is enforced using a combination of primary keys and foreign keys. As mentioned previously, for a book to exist, it has to be written by at least one author.

- _Semantic Integrity Constraint_: refers to the correctness of the meaning of the data. For example, in the relation author, if the attribute or column city contains a garbage value instead of Toronto, the garbage value does not have any meaning. The semantic integrity constraint is related to the correctness of the data.

- _Domain Constraint_: specifies the permissible values for a given attribute. For example, in the relation author, the attribute country must contain a two letter country code.

- _Null Constraint_: specifies that attribute values cannot be null.

- _Check Constraint_: enforces domain integrity by limiting the values that are accepted by an attribute.

<h3>Additional Information</h3>

__Primary Keys:__

If a relation schema has more than one key, then each key is called a candidate key. One of the candidate keys is designated as the primary key, and the others are called secondary keys.

__Semantic Constraints:__

Semantic Constraints are constraints that cannot be directly expressed in the schemas of the data model. Semantic constraints are also called application-based rules or business rules. They are additional rules specified by users or database administrators. For example, a class can have a maximum of 30 students; salary of an employee cannot exceed the salary of the employee’s manager.



<h1>Week 3 - Accessing Databases using Python</h1>



<h2>Accessing databases using Python</h2>


<h3>How to access databases using Python?</h3>

A notebook interface is a virtual notebook environment used for programming. Examples of notebook interfaces include the mathematical notebook, maple worksheet, matlab notebook, IPython Jupyter, R Markdown, Apache Zeppelin, Apache Spark notebook and the Databricks cloud.

__SQL API__

The SQL API consists of library function calls as an application programming interface, API, for the DBMS. To pass SQL statements to the DBMS, an application program calls functions in the API, and it calls other functions to retrieve query results and status information from the DBMS.

<img src="../5. Databases and SQL for Data Science/images/sql_api.png">

Each database system has its own library. The table below shows a list of a few applications and corresponding SQL APIs.

<img src="../5. Databases and SQL for Data Science/images/sql_api_usage.png">

<h3>Writing code using DB-API</h3>

DB-API is Python's standard API for accessing relational databases. It is a standard that allows you to write a single program that works with multiple kinds of relational databases instead of writing a separate program for each one. So, if you learn the DB-API functions, then you can apply that knowledge to use any database with Python.

The two main concepts in the Python DB-API are:

- __Connection objects__: You use connection objects to connect to a database and manage your transactions.
    - Database connections
    - Manage transactions

    _Connection Methods:_
    - cursor() - returns a new cursor object using the connection.
    - commit() - is used to commit any pending transaction to the database.
    - rollback() - causes the database to roll back to the start of any pending transaction.
    - close() - is used to close a database connection.

- __Cursor objects__: Cursor objects are used to run queries. The cursor works similar to a cursor in a text processing system where you scroll down in your result set and get your data into the application. Cursors are used to scan through the results of a database.
    - Database queries

    _Cursor Methods:_
    - callproc()
    - execute()
    - executemany()
    - fetchone()
    - fetchmany()
    - fetchall()
    - nextset()
    - Arraysize()
    - close()

    Cursors created from the same connection are not isolated i.e. any changes done to the database by a cursor are immediately visible by the other cursors. Cursors created from different connections can or cannot be isolated depending on how the transaction support is implemented.

    A database cursor is a control structure that enables traversal over the records in a database. It behaves like a file name or file handle in a programming language.

    <img src="../5. Databases and SQL for Data Science/images/db_cursor.png">

__Writing code using DB-API__

```python
from dbmodule import connect

# Create connection object
Connection = connect(
    'databasename', 'username', 'pswd'
)

# Create cursor object
Cursor = connection.cursor()

# Run Queries
Cursor.execute('select * from mytable')
Results = Cursor.fetchall()

# Free resources
Cursor.close()
Connection.close()
```

<h3>Connecting to a database using ibm_db API</h3>

The ibm_db API provides a variety of useful Python functions for accessing and manipulating data in an IBM data server database, including functions for connecting to a database, repairing and issuing sequel statements, fetching rows from result sets, calling stored procedures, committing and rolling back transactions, handling errors and retrieving metadata.

The ibm_db API uses the IBM Data Server Driver for ODBC, and CLI APIs to connect to IBM, DB2, and Informix.

__Importing ibm_db API__

```python
import ibm_db
```

Connecting to the DB2 warehouse requires the following information:

<img src="../5. Databases and SQL for Data Science/images/ibm_db_connection.png">

Below is an example of creating a DB2 warehouse database connection in python:

<img src="../5. Databases and SQL for Data Science/images/ibm_db_example.png">

You can then close the database by closing all the connections:

```python
ibm_db.close(conn)
```

<h3>Creating tables, loading data and querying data</h3>

There are different ways of creating tables in DB2 Warehouse. One is using the Web console provided by DB2 Warehouse, and the other option is to create tables from any SQL, R, or Python environments.

__Creating Tables__

To create a table, we use the `ibm_db.exec_immediate` function. The parameters for the function are:

- Connection: is a valid database connection resource that is returned from the `ibm_dbconnect` or `ibm_dbpconnect` function.

- Statement: is a string that contains the sequel statement.

- Options: is an optional parameter that includes a dictionary that specifies the type of cursor to return for results sets.

Below is the code to create a table called trucks in Python:

<img src="../5. Databases and SQL for Data Science/images/create_table.png">

Python code to insert data into the table:

<img src="../5. Databases and SQL for Data Science/images/insert_data.png">

Python code to query data:

<img src="../5. Databases and SQL for Data Science/images/query_data.png">

Using pandas to retrieve data from the database tables:

<img src="../5. Databases and SQL for Data Science/images/read_sql.png">


<h2>Using JOIN operations to work with multiple tables</h2>


<h3>Join Overview</h3>

To combine data from two tables, we use the JOIN operator. A JOIN combines the rows from two or more tables based on a relationship between certain columns in these tables.

<h3>Inner Join Overview</h3>

There are two types of table joins: _inner join_ and _outer join_. The most common type of join is the inner join. An inner join matches the results from two tables and displays only the result set that matches the criteria specified in the query. An inner join returns only the rows that match.

For example,

```sql
select b.borrower_id, b.lastname, b.country, l.borrower_id, l.loan_date
from borrower b inner join loan l
on b.borrower_id = l.borrower_id;
```

If you want to join multiple tables:

```sql
select b.lastname, l.copy_id, c.status
from borrower b
    inner join loan lo on b.borrower_id = l.borrower_id
    inner join copy c on l.copy_id = c.copy_id;
```

<h3>Left Outer Join Overview</h3>

An Outer Join is a specialized form of joint and there are three types of Outer Joins: _Left Outer Join_, _Right Outer Join_ and _Full Outer Join_.

A left outer join or _left join_ matches the results from two tables and displays all the rows from the left table, and combines the information with rows from the right table that match the criteria specified in the query.

<img src="../5. Databases and SQL for Data Science/images/left_join.png">

<h3>Right Outer Join Overview</h3>

A right join matches the results from two tables and displays all the rows from the right table and combines the information with rows from the left table that matched the criteria specified in the query.

<img src="../5. Databases and SQL for Data Science/images/right_join.png">

<h3>Full Outer Join Overview</h3>

The full join keyword returns all rows from both tables. That is all rows from the left table and all rows from the right table. So, the full join could return a very large result set.

<img src="../5. Databases and SQL for Data Science/images/full_join.png">



<h1>Week 4: Course Assignment</h1>
