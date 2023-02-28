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
---

## Conditions and Nulls
---

## Correlating table Names
---

## Create Statement with Data Types 
---

## Picking Correct Data Types
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
---

## Qualified Column Statements
---

## Pattern Matching and wildcard characters
---

## Joins (5 questions)
---

## Primary Key
---

## Deleting Table
---

## Select Statement
---

## Union
---

## Where Statements
---



 