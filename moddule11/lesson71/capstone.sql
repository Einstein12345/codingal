-- Create a table
CREATE TABLE Students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(5),
    marks INT
);

-- Insert data
INSERT INTO Students (student_id, name, age, grade, marks) VALUES
(1, 'Alice', 20, 'A', 85),
(2, 'Bob', 22, 'B', 70),
(3, 'Charlie', 21, 'A', 90),
(4, 'David', 23, 'C', 60),
(5, 'Eva', 20, 'B', 75);

-- View all data
SELECT * FROM Students;

-- Filtering (students with marks above 75)
SELECT * FROM Students
WHERE marks > 75;

-- Sorting (highest marks first)
SELECT * FROM Students
ORDER BY marks DESC;

-- Sorting + Filtering (Grade A students sorted by marks)
SELECT * FROM Students
WHERE grade = 'A'
ORDER BY marks DESC;

-- Update data (increase marks for a student)
UPDATE Students
SET marks = marks + 5
WHERE name = 'Bob';

-- Delete a record
DELETE FROM Students
WHERE student_id = 4;

-- Aggregate analysis (average marks)
SELECT AVG(marks) AS average_marks
FROM Students;

-- Count students by grade
SELECT grade, COUNT(*) AS total_students
FROM Students
GROUP BY grade;