# Exam 2 study guide
Using Sally's Pet Store as the database (2023)

##  Find Incorrect Usage of Alter Table
---

## "Between" Numbers
A command that will show you all values between a start and an end point.

```
Select * FROM SaleAnimal
WHERE SalePrice BETWEEN 0 AND 10;
```
SalePrice is our column
BETWEEN is the boolean operator
0 is the start point. 10 is the end point.

*Results*
|SaleID|AnimalID|SalePrice|
|-|-|-|
|10|9|1.80|
|112|118|3.60|

You can also use `value >= param AND value <= param`

---

## Column Alias
A functional rename of the column to make querying easier to decipher.
```
Select TOP 3 Name, Category, Breed FROM Animal anim
WHERE anim.Name IS NOT NULL AND anim.Category LIKE 'Cat'
;
```

Animal ⬅️ Object

anim ⬅️ Object Alias 

*Results*
|Name	|Category|	Breed|
|-|-|-|
|Rosie	|Cat	|Oriental Shorthair|
|Eugene	|Cat	|Bombay|
|Tina	|Cat	|Sphynx|
---

## Column Creation Statement
There are two ways of creating a column that we discussed in class.
Both ways may require extra parameters, but it depends on your needs.

1. To create a brand new column on a new table
`CREATE <column name> <datatype>`

2. To create a brand new column on an existing table
```
ALTER TABLE SaleAnimal
ADD AnimalBought VARCHAR(50)
;
```
*results*
|SaleID|AnimalID|SalePrice|AnimalBought|
|-|-|-|-|
|4|8|183.38|NULL|
|5|183|114.30|NULL|
|6|58|132.19|NULL|

---

## Concatenating Columns

Combine two or more columns to make a single column.

```
SELECT TOP 3
    FirstName, LastName, FirstName + ' ' + LastName AS  FullName
FROM INFO2410_SPS_Brayden_C.dbo.Customer
;
```



|FirstName	|LastName	|Concatenated|
|-|-|-|
|Walkin	|Walkin	|Walkin Walkin|
|Brent	|Cummings|	Brent Cummings|
|Dwight	|Logan	|Dwight Logan|

---

## Conditions and Nulls

Conditions: Logical statements that help filter your query.

`WHERE` and `HAVING` are conditions

Nulls: cells that have no value.

When creating a database, you need to define if your table will need nulls or not based on your clients needs. Primary keys are not allowed to have null values because they are the address to foreign keys on other tables.

`WHERE <value> <boolean logic>`

`HAVING <value> <boolean logic>`

---

## Correlating table Names
---

## Create Statement with Data Types
---

## Picking Correct Data Types

Correct data typing is necessary for your database. [You can find more about types here.](https://www.w3schools.com/sql/sql_datatypes.asp)

Types that *might* be on the test

Numeric Data Types:
* BIT(*size*)
* BOOL/BOOLEAN
* INT/INTEGER
* BIGINT(*size*)
* FLOAT(*size, digits*)
* FLOAT(*p*)
* DOUBLE(*size, digits*)
* DECIMAL(*size, digits*)
* MONEY ⬅️ Like a float, but money.

String Data Types:
* CHAR(n) ⬅️ Max size 8,000 characters
* VARCHAR(n) ⬅️ Max size 8,000 characters
* VARCHAR(max) ⬅️ Max size 1,073,741,824 characters
* NVARCHAR() ⬅️ Max size 4,000 characters
* NVARCHAR(max) ⬅️ Max size 536,870,912 characters

Date and Time Data Types:
* DATE
* DATETIME
* TIMESTAMP
* TIME
* YEAR

---

## Data Definition Language (DDL) Statements

### CREATE
Create an object inside a database server.

    `CREATE DATABASE DB_A;`
    or
    `CREATE TABLE Table_A (<contents of Table_A>)`

### DROP
Drop an object from the database

*Drop command may not work for SQLite*

    DROP COLUMN <column>
    DROP TABLE <table>

### ALTER
Alters an existing database object

    ALTER TABLE <table> ADD <new object> <object type>
    ALTER TABLE <table> DROP COLUMN <object>

---

## Use of Distinct

Distinct is a condition that filters out duplicate values for 


---

## Qualified Column Statements

Statements that allow the addition, modification, or removal of specific columns on a table.

Conditions:
* INSERT :arrow_left: *might be on test*
* UPDATE :arrow_left: *might be on test*
* MERGE
* COMMENT
* LABEL

---

## Pattern Matching and wildcard characters

Logical conditions that match a cell based on what your query will be.

Wildcards:

* % ⬅️ Represents zero or more characters
* _ ⬅️ Represents single characters
* [] :arrow_left: Represents any single character within brackets.
* [^] :arrow_left: Represents any character that is not in brackets. 
* \- ⬅️ Represents any single character within a range.

```
SELECT TOP 3
    Name, Breed
FROM INFO2410_SPS_Brayden_C.dbo.Animal
WHERE 
    Name LIKE '%e'
        AND
    Breed LIKE '%[ie]%'
;
```

|Name	|Breed|
|-|-|
|Rosie	|Oriental Shorthair|
|Jackie	|Doberman|
|Gene	|Wire Fox Terrier|

---

## Joins (5 questions)

[Joins are located in another note files](https://github.com/Autoclitic/UVU_IT_Notes/Test2Notes.md)

---

## Primary Key

Primary keys are what connects a table to other tables in a database. They cannot be null, and will autoincrement when an INT type is used.

Example ➡️ `[ID] INT PRIMARY KEY`

---

## Deleting Table

Deleting a table involves the `DROP` condition.

```
DROP <TableName> FROM <Database>; 
```

---

## Select Statement

Selects the columns to display from one or more tables.

```
SELECT
    *
FROM <table>
;
```

---

## Union

Combine two ore more select statements into one query. The query must have a similar number of rows to return.

```


```

---

## Where Statements

Logical conditioning to filter your queries. You can use logical operators with the where statement.

`WHERE <logic>`

`WHERE Date != '20000101'`

`WHERE Name LIKE 'Bo Jack'`

`WHERE Price >= 40.00 AND Price <= 100.00`

---



 