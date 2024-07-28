-- Use CASE statement when you need to categorize or conditionally alter the data within a result set 
-- The CASE statement in MySQL is a way to perform conditional logic in SQL queries.
--   It allows you to evaluate conditions and return a value based on the result of those conditions.
-- CASE Syntax
-- (CASE
--     WHEN condition1 THEN result1
--     WHEN condition2 THEN result2
--     WHEN conditionN THEN resultN
--     ELSE result
-- END;)
-- Classify Students Based on GPA
SELECT student_id,first_name,last_name,gpa,
       CASE 
           WHEN gpa>=3.5 THEN 'Honors'
           WHEN gpa>=3.2 THEN 'Merit'
           Else 'Pass'
		END AS classification 
FROM students;

-- CASE Statement to Determine Scholarship Eligibility
SELECT student_id,first_name,last_name,gpa,
       CASE
           WHEN gpa >= 3.8 THEN 'Full Scholarship'
           WHEN gpa >= 3.5 THEN 'Partial Scholarship'
           ELSE 'No Scholarship'
       END AS scholarship_status
FROM students;
-- Using CASE in WHERE Clause to Filter Students by Major and GPA
SELECT student_id,first_name,last_name,gpa,major
FROM students
WHERE 
    CASE
        WHEN major = 'Computer Science' THEN gpa >= 3.5
        WHEN major = 'Mathematics' THEN gpa >= 3.0
        ELSE gpa >= 2.5
    END;
-- Using CASE in ORDER BY Clause to Sort Students by Major and GPA
-- SELECT student_id,first_name,last_name,major,gpa
-- FROM students
-- ORDER BY 
--     CASE
--         WHEN major = 'Computer Science' THEN gpa
--         WHEN major = 'Mathematics' THEN gpa DESC
--         ELSE major
--     END;
    
-- Categorize Students Based on Age Group
SELECT student_id,first_name,last_name,age,
       CASE
           WHEN age < 20 THEN 'Teenager'
           WHEN age BETWEEN 20 AND 24 THEN 'Young Adult'
           ELSE 'Adult'
       END AS age_group
FROM students;

-- CASE with Aggregate Functions to Count Students by GPA Range
-- SELECT major,
--        COUNT(CASE WHEN gpa >= 3.5 THEN 1 END) AS honors_count,
--        COUNT(CASE WHEN gpa BETWEEN 3.0 AND 3.49 THEN 1 END) AS merit_count,
--        COUNT(CASE WHEN gpa < 3.0 THEN 1 END) AS pass_count
-- FROM students
-- GROUP BY major;

