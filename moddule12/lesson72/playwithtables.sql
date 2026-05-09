CREATE TABLE Employee (
    EmpID INT,
    Name VARCHAR(50),
    Department VARCHAR(50),
    Salary INT,
    Age INT
);
INSERT INTO Employee VALUES
(1, 'Alice', 'HR', 50000, 25),
(2, 'Bob', 'IT', 70000, 30),
(3, 'Charlie', 'IT', 65000, 28),
(4, 'Diana', 'Sales', 45000, 24),
(5, 'Ethan', 'HR', 55000, 32);
SELECT * FROM Employee;
SELECT Name, Salary
FROM Employee
WHERE Department = 'IT';
SELECT MAX(Salary) AS Highest_Salary
FROM Employee;
SELECT MIN(Age) AS Youngest
FROM Employee;
SELECT Name, Salary
FROM Employee
WHERE Salary > 50000;
SELECT Name, Age
FROM Employee
WHERE Department = 'HR'
AND Age > 30;
SELECT AVG(Salary) AS Avg_Salary
FROM Employee;
SELECT COUNT(*) AS Total_Employees
FROM Employee;