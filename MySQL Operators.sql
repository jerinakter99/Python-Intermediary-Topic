-- MySQL AND, OR ,NOT, IN, LIKE, BETWEEN Operators
-- AND, OR ,NOT
SELECT * FROM student
WHERE Grade='A' AND Department= 'CSE';

SELECT * FROM student
WHERE Department='CSE' OR Department='ENG';

SELECT * FROM student
WHERE NOT Grade='F';

-- IN LIKE BETWEEN 
-- filter query results based on specific conditions.

SELECT * FROM student
WHERE Grade IN('A','F');

SELECT * FROM student
WHERE Grade NOT IN ('A','F');

-- LIKE 
SELECT* FROM student
WHERE Fname LIKE '%a' ;

-- BETWEEN
SELECT *FROM student
WHERE Student_Id BETWEEN 1 AND 3;
SELECT* FROM student