-- DISTINCT
SELECT DISTINCT department
FROM employees;

-- ORDER BY
SELECT employee_id, employee_name, salary
FROM employees
ORDER BY salary DESC;

-- GROUP BY with COUNT
SELECT department, COUNT(*) AS total_employees
FROM employees
GROUP BY department;

-- Aggregate Functions
SELECT 
    COUNT(*) AS total_employees,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary,
    MAX(salary) AS highest_salary,
    MIN(salary) AS lowest_salary
FROM employees;

-- GROUP BY with Aggregate Function
SELECT department, AVG(salary) AS average_salary
FROM employees
GROUP BY department
ORDER BY average_salary DESC;