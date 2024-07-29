-- combine rows from two or more tables based on a related column between them. 
-- INNER JOIN: Returns records that have matching values in both tables
-- LEFT JOIN: Returns all records from the left table, and the matched records from the right table
-- RIGHT JOIN: Returns all records from the right table, and the matched records from the left table
-- CROSS JOIN: Returns all records from both tables
-- Self Join : the table is joined with itself.

-- 1.INNER JOIN keyword selects records that have matching values in both tables 
-- INNER JOIN Syntax

-- SELECT column_name(s)
-- FROM table1
-- INNER JOIN table2
-- ON table1.column_name = table2.column_name;

-- Inner Join Query: two tables: students and enrollments.
SELECT students.student_id, students.first_name, students.last_name, enrollments.course_id
FROM students
INNER JOIN enrollments 
ON students.student_id = enrollments.student_id;


-- 2.LEFT JOIN Syntax
-- SELECT column_name(s)
-- FROM table1
-- LEFT JOIN table2
-- ON table1.column_name = table2.column_name;

-- LEFT JOIN returns all rows from the left table (students), and the matched rows from the right table (enrollments).
SELECT students.student_id, students.first_name, students.last_name, enrollments.course_id
FROM students
LEFT JOIN enrollments ON students.student_id = enrollments.student_id;

-- A RIGHT JOIN returns all rows from the right table (enrollments), and the matched rows from the left table (students)
SELECT students.student_id, students.first_name, students.last_name, enrollments.course_id
FROM students
RIGHT JOIN enrollments ON students.student_id = enrollments.student_id;

-- 4.CROSS JOIN returns the Cartesian product of the two tables. This means it returns all possible combinations of rows from the left table and the right table.
SELECT students.student_id, students.first_name, students.last_name, enrollments.course_id
FROM students
CROSS JOIN enrollments;

