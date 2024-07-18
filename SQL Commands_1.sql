-- SELECT,  WHERE, ALIAS

-- 1. SELECT statements
SELECT Student_Id , Grade 
FROM student;

-- 2. DISTINCT statement is used to return only distinct (different) values.
SELECT DISTINCT Grade, Student_Id
FROM student;
-- 3. INSERT value into table
INSERT INTO student(Student_Id,Fname,Lname,Department,Grade)
VALUES(1,"Jerin","Akter","CSE","A"),
	  (2,"Oris","Khan","BBA","F"),
      (3,"Arif","Islam","CSE","B"),
      (4,"Rita","","ENG","A")
;
SELECT * FROM student
WHERE Student_Id=3;
SELECT Student_id,Fname,Grade
FROM Student;
SELECT distinct Student_id, Fname,Department
FROM student;

-- 4. WHERE Clause
SELECT Student_Id,Fname
FROM student
WHERE Student_Id = 1;

SELECT Grade FROM student
WHERE Student_Id= 4 ;

-- 5. Aliases for temporary name
-- provide temporary names for tables or columns
-- Column Aliases

SELECT Fname AS "First Name" , Lname AS 'Last Name'
FROM student;
SELECT * FROM student;

