-- INSERT INTO, UPDATE, DELETE
-- TRUNCATE TABLE student;
-- 1. INSERT INTO
-- INSERT value into table
INSERT INTO student(Student_Id,Fname,Lname,Department,Grade,EMAIL,Contract_no)
VALUES(1,"Jerin","Akter","CSE","A","jerin@gmail.com",'01334558'),
	  (2,"Oris","Khan","BBA","F","oris@gmail.com",'9847346374'),
      (3,"Arif","Islam","CSE","B",'arif@gmail.com','87685487547'),
      (4,"Rita","Khan","ENG","A",'','29823764'),
      (5,'anika','tuba',"BNG",'B','tuba@gmail.com',""),
      (6,'aria',"",'BBA',"C","aria@gmail.com",'738473874');
SELECT * FROM student ;

-- 2.UPDATE table data
UPDATE student
SET EMAIL="rita@gmail.com",
    Contract_no ="01738483448"
WHERE Student_Id = 4 ;
SELECT*FROM student;

UPDATE student
SET Contract_no="0193487474"
WHERE Student_Id='5';
SELECT * FROM student;

-- 3.Delete rows
 DELETE FROM student
 WHERE Fname='RITA';
 SELECT*FROM student;
 
-- Delete Multiple Rows
-- Delete all students who are in the 'BBA' Department
 DELETE FROM student
 WHERE Department='BBA';
 SELECT *FROM student



