-- Aggregate functions are powerful tools for summarizing data in SQL. They can be used to find minimum and maximum values,
--     count rows, calculate averages, and sum values. When combined with the GROUP BY clause, 
--     they can provide insights into different subsets of your data.
-- commonly used with the GROUP BY clause to group the results by one or more columns. 
-- MIN(): Returns the smallest value.
-- MAX(): Returns the largest value.
-- COUNT(): Returns the number of rows.
-- AVG(): Returns the average value.
-- SUM(): Returns the sum of values.
-- GROUP BY: Used to group rows sharing a property so that an aggregate function can be applied to each group.
-- HAVING: Used to filter records after the GROUP BY clause

-- 1.MIN(): Finding the Minimum GPA
SELECT MIN(gpa) AS Min_gpa FROM students;

-- 2.MAX(): Finding the Maximum GPA
SELECT MAX(gpa) AS Max_gpa FROM students;

-- 3. COUNT(): Counting the Number of Students
SELECT COUNT(*) AS total_students FROM students;

-- 4. AVG(): Calculating the Average GPA
SELECT AVG(gpa) AS average_gpa FROM students;

-- 5. SUM(): Summing the Ages of All Students
SELECT SUM(age) AS total_age FROM students;

-- Grouping with Aggregate Functions

-- Counting Students by Major
SELECT major, COUNT(*) AS num_students
FROM students
GROUP BY major;

-- Average GPA by Major
SELECT major, AVG(gpa) AS average_gpa
FROM students
GROUP BY major;

-- Maximum GPA by Gender
SELECT gender, MAX(gpa) AS max_gpa
FROM students
GROUP BY gender;











