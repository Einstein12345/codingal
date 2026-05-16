-- CREATE TABLE WITH CONSTRAINTS
CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT CHECK (age >= 18),
    email VARCHAR(100) UNIQUE,
    phone_number VARCHAR(15),
    course VARCHAR(50)
);

-- INSERT DATA
INSERT INTO students (student_id, name, age, email, phone_number, course)
VALUES
(1, 'Alice', 20, 'alice@gmail.com', '9876543210', 'Computer Science'),
(2, 'Bob', 22, NULL, NULL, 'Mathematics'),
(3, 'Charlie', 19, 'charlie@gmail.com', NULL, 'Physics'),
(4, 'David', 21, NULL, '9123456780', 'Chemistry'),
(5, 'Eva', 23, 'eva@gmail.com', '9988776655', 'Biology');

-- FIND STUDENTS WHERE EMAIL IS NULL
SELECT *
FROM students
WHERE email IS NULL;

-- FIND STUDENTS WHERE PHONE NUMBER IS NULL
SELECT *
FROM students
WHERE phone_number IS NULL;

-- FIND STUDENTS WHERE EMAIL IS NOT NULL
SELECT *
FROM students
WHERE email IS NOT NULL;

-- COUNT NULL PHONE NUMBERS
SELECT COUNT(*) AS missing_phone_numbers
FROM students
WHERE phone_number IS NULL;