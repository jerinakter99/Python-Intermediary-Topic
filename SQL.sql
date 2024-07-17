/* CREATE database
 CREATE DATABASE Mydata ; */
/* CREATE table

CREATE TABLE Student (
Student_Id int , 
Fname varchar(50) ,
Lname varchar(50),
Department varchar(40),
Grade varchar(10)

);*/
/* INSERT value into table
INSERT INTO student(Student_Id,Fname,Lname,Department,Grade)
VALUES(1,"Jerin","Akter","CSE","A"),
	  (2,"Oris","Khan","BBA","F"),
      (3,"Arif","Islam","CSE","B"),
      (4,"Rita","","ENG","A")
;
*/
/* SELECT statements
SELECT * FROM student
WHERE Student_Id=3;
SELECT Student_id,Fname,Grade
FROM Student;
SELECT distinct Student_id, Fname,Department
FROM student
 */
/* WHERE Clause
SELECT Student_Id,Fname
FROM student
WHERE Student_Id = 1;

SELECT Grade FROM student
WHERE Student_Id= 4 */
/* UPDATE table values
UPDATE student
SET Fname ='orin', Grade = 'C'
WHERE Student_Id=3;
SELECT * FROM student ; */
/* DELETE 
DELETE FROM student WHERE Fname='Oris';
SELECT * FROM student;
-- for delete all data from table
-- DELETE FROM student */
/* ORDER BY used for sort
SELECT Grade 
FROM student
ORDER BY Grade ASC;

SELECT Fname ,Lname
FROM student
ORDER BY Fname,Lname DESC*/
/* ALTER TABLE for add, delete, modify columns in an existing table
ALTER TABLE student
ADD Email VARCHAR (40);

ALTER TABLE student
DROP COLUMN Email ;

ALTER TABLE student
MODIFY COLUMN Student_Id INT;      //MODIFY The datatype
SELECT * FROM student ;*/
/* Aliases for temporary name
-- provide temporary names for tables or columns
-- Column Aliases
-- SELECT Fname AS "First Name" , Lname AS 'Last Name'
-- FROM student;
-- SELECT * FROM student;
-- -- Table Aliases
SELECT Student_Id, Fname
FROM student AS Stu; */
/* AND, OR ,NOT
SELECT * FROM student
WHERE Grade='A' AND Department= 'CSE';

SELECT * FROM student
WHERE Department='CSE' OR Department='ENG';

SELECT * FROM student
WHERE NOT Grade='F'*/
/* IN LIKE BETWEEN
SELECT * FROM student
WHERE Grade IN('A','F');
SELECT * FROM student
WHERE Grade NOT IN ('A','F');
SELECT* FROM student
WHERE Fname LIKE '%a' ;*/
/* GROUP BY, LIMIT*/
SELECT * FROM student
LIMIT 3;

SELECT * FROM student
LIMIT 2 OFFSET 2;






