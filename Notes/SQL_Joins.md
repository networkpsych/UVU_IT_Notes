<i><span style="color:#FFBF00"><font size="+2"> These notes are for the 2/21/23 and 2/23/23 class. </font></span></i>

source: *[Visual Representation of SQL Joins by C.L. Moffatt](https://www.codeproject.com/Articles/33052/Visual-Representation-of-SQL-Joins)*

## Take two tables, Table_A and Table_B

<table>
<tr><th>Table_A</th><th>Table_B</th></tr>
<tr><td>

|PK|Value|
|-|-|
|1|Fox|
|2|Cop|
|3|Taxi|
|6|Washington|
|7|Dell|
|5|Arizona|
|4|Lincoln|
|10|Lucent|

</td><td>

|PK|Value|
|-|-|
|1|Trot|
|2|Car|
|3|Cab|
|6|Monument|
|7|PC|
|5|Microsoft|
|4|Apple|
|10|Scotch|

</td></tr> </table>

---

## **Inner Join**
* Returns all records that have matching records between two tables.

```
    SELECT <column_list>
    FROM Table_A A
    INNER JOIN Table_B B
    ON B.Key = A.Key
```

|A_PK|A_Value   | B_Value   | B_PK|
|----|----------| ----------| ----|
|   1|FOX       | TROT      |    1|
|   2|COP       | CAR       |    2|
|   3|TAXI      | CAB       |    3|
|   6|WASHINGTON| MONUMENT  |    6|
|   7|DELL      | PC        |    7|
---

## **Left Join**
* Returns all records from selected table, even if they do not match the other  tables.

```
    SELECT <column_list>
    FROM Table_A A
    LEFT JOIN Table_B B
    ON A.Key = B.Key
```

|A_PK| A_Value  |  B_Value  | B_PK|
|----|----------| ----------| ----|
|   1|FOX       | TROT      |    1|
|   2|COP       | CAR       |    2|
|   3|TAXI      | CAB       |    3|
|   4|LINCOLN   | NULL      | NULL|
|   5|ARIZONA   | NULL      | NULL|
|   6|WASHINGTON| MONUMENT  |    6|
|   7|DELL      | PC        |    7|
|  10|LUCENT    | NULL      | NULL|

---

## **Right Join**
<span style="color:red"> Right Joins </span> 
> It is suggested that you don't use Right Joins. If you reverse the logic, you can just run a LEFT JOIN.
* Returns all records from comparison table, even if they do not match the selected table.

```
    SELECT <column_list>
    FROM Table_A A
    RIGHT JOIN Table_B B
    ON A.Key = B.Key
```

|A_PK |A_Value    |B_Value    |B_PK|
|---- |---------- |---------- |----|
|   1 |FOX        |TROT       |   1|
|   2 |COP        |CAR        |   2|
|   3 |TAXI       |CAB        |   3|
|   6 |WASHINGTON |MONUMENT   |   6|
|   7 |DELL       |PC         |   7|
|NULL |NULL       |MICROSOFT  |   8|
|NULL |NULL       |APPLE      |   9|
|NULL |NULL       |SCOTCH     |  11|

---

## **Outer Join**
* Return all records from both tables.
  * Also known as `FULL OUTER JOIN` or a `FULL JOIN`

```
    SELECT <column_list>
    FROM Table_A A
    FULL OUTER JOIN Table_B B
    ON A.Key = B.Key
```

|A_PK| A_Value   | B_Value   | B_PK|
|----| ----------| ----------| ----|
|   1| FOX       | TROT      |    1|
|   2| COP       | CAR       |    2|
|   3| TAXI      | CAB       |    3|
|   6| WASHINGTON| MONUMENT  |    6|
|   7| DELL      | PC        |    7|
|NULL| NULL      | MICROSOFT |    8|
|NULL| NULL      | APPLE     |    9|
|NULL| NULL      | SCOTCH    |   11|
|   5| ARIZONA   | NULL      | NULL|
|   4| LINCOLN   | NULL      | NULL|
|  10| LUCENT    | NULL      | NULL|

---

## **Right Join Excluding Inner Join**
* Returns all records in the selected table that do not match the comparison table.

```
    SELECT <column_list>
    FROM Table_A A
    LEFT JOIN Table_B B
    ON A.Key = B.Key
    WHERE B.Key IS NULL
```
|A_PK|A_Value   |B_Value   |B_PK|
|----|----------|----------|----|
|   4|LINCOLN   |NULL      |NULL|
|   5|ARIZONA   |NULL      |NULL|
|  10|LUCENT    |NULL      |NULL|

---

## **Outer Join Excluding Inner Join**
* Returns all records in the compaison table that do not match the selected table.

```
    SELECT <column_list>
    FROM Table_A A
    LEFT JOIN Table_B B
    ON A.Key = B.Key
    WHERE A.Key IS NULL
```

|A_PK|A_Value   |B_Value   |B_PK|
|----|----------|----------|----|
|NULL|NULL      |MICROSOFT |   8|
|NULL|NULL      |APPLE     |   9|
|NULL|NULL      |SCOTCH    |  11|

---

## **Outer Excluding Join**
* Returns all records that do not match in both tables.

```
    SELECT <column_list>
    FROM Table_A A
    LEFT JOIN Table_B B
    ON A.Key = B.Key
    WHERE A.Key IS NULL OR B.Key IS NULL
```
|A_PK|A_Value   |B_Value   |B_PK|
|----|----------|----------|----|
|NULL|NULL      |MICROSOFT |   8|
|NULL|NULL      |APPLE     |   9|
|NULL|NULL      |SCOTCH    |  11|
|   5|ARIZONA   |NULL      |NULL|
|   4|LINCOLN   |NULL      |NULL|
|  10|LUCENT    |NULL      |NULL|

---
<br></br>

## Image from source website

![Image from source](https://www.codeproject.com/KB/database/Visual_SQL_Joins/Visual_SQL_JOINS_V2.png)