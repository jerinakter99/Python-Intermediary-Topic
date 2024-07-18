-- Alter Table ( ADD COLUMN, MODIFY COLUMN)
-- 1. ADD COLUMN
ALTER TABLE student
ADD COLUMN EMAIL VARCHAR(50),
ADD COLUMN Phone_No VARCHAR(15),
ADD COLUMN Address VARCHAR(255);

-- 2. MODIFY COLUMN	
-- modify the Fname and Lname columns to increase their length
ALTER TABLE student 
MODIFY COLUMN Fname VARCHAR(255),
MODIFY COLUMN Lname VARCHAR (255),
-- MODIFY the EMAIL column uniqe
MODIFY COLUMN EMAIL VARCHAR (50) UNIQUE;

-- 3. Renaming a Column
-- rename Phone_No column To Contract_no using the CHANGE COLUMN clause
ALTER TABLE student 
CHANGE COLUMN Phone_No Contract_no VARCHAR(15);

-- 4. Drop column
ALTER TABLE Student 
DROP COLUMN Address;




