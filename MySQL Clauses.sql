-- ORDER BY, GROUP BY, LIMIT
-- 1. ORDER BY used for sort
sELECT Grade 
FROM student
ORDER BY Grade ASC;

SELECT Fname ,Lname
FROM student
ORDER BY Fname,Lname DESC ;

-- 2.GROUP BY _to show the same type data together ,group rows 

SELECT Grade
FROM student
GROUP BY Grade;

SELECT Grade,Department
FROM student
GROUP BY Grade,Department;

-- LIMIT clause is used to specify the number of records to return.

SELECT * FROM student
LIMIT 3;

SELECT * FROM student
LIMIT 3 OFFSET 1;

SELECT * FROM student
WHERE Grade='Eng'
LIMIT 2;











