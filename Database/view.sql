USE COMPANY;

CREATE TABLE EMPLOYEES(
	EMPLOYEE_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIRST_NAME VARCHAR(255),
    LAST_NAME VARCHAR(255),
    DEPARTMENT VARCHAR(255),
    SALARY DECIMAL(10,2),
    HIRE_DATE DATE
);

INSERT INTO employees (first_name, last_name, department, salary, hire_date) VALUES
('John', 'Doe', 'HR', 60000.00, '2021-03-15'),
('Jane', 'Smith', 'Finance', 75000.00, '2020-06-01'),
('Michael', 'Johnson', 'IT', 90000.00, '2019-09-23'),
('Patricia', 'Brown', 'Marketing', 65000.00, '2022-01-10'),
('Robert', 'Jones', 'IT', 85000.00, '2023-05-19'),
('Linda', 'Davis', 'Finance', 71000.00, '2021-04-22'),
('William', 'Garcia', 'HR', 63000.00, '2020-12-11'),
('Elizabeth', 'Miller', 'Marketing', 69000.00, '2019-11-30'),
('James', 'Wilson', 'IT', 92000.00, '2022-03-01'),
('Mary', 'Moore', 'Finance', 72000.00, '2018-07-14'),
('David', 'Taylor', 'Marketing', 68000.00, '2021-08-29'),
('Jennifer', 'Anderson', 'HR', 64000.00, '2023-02-17'),
('Richard', 'Thomas', 'IT', 91000.00, '2019-06-25'),
('Susan', 'Jackson', 'Finance', 76000.00, '2022-05-07'),
('Charles', 'White', 'Marketing', 67000.00, '2020-09-13'),
('Joseph', 'Harris', 'HR', 60000.00, '2018-11-21'),
('Karen', 'Martin', 'IT', 95000.00, '2021-10-05'),
('Thomas', 'Thompson', 'Finance', 70000.00, '2020-02-14'),
('Sarah', 'Martinez', 'Marketing', 67500.00, '2023-03-25'),
('Christopher', 'Robinson', 'IT', 87000.00, '2019-12-15'),
('Nancy', 'Clark', 'HR', 62000.00, '2022-08-18'),
('Daniel', 'Rodriguez', 'Finance', 74000.00, '2018-05-20'),
('Matthew', 'Lewis', 'IT', 93000.00, '2020-11-12'),
('Betty', 'Lee', 'Marketing', 68000.00, '2021-06-04'),
('Anthony', 'Walker', 'HR', 61000.00, '2019-03-08'),
('Sandra', 'Hall', 'Finance', 71500.00, '2022-07-30'),
('Mark', 'Allen', 'IT', 90500.00, '2023-01-22'),
('Donna', 'Young', 'Marketing', 65500.00, '2018-10-11'),
('Steven', 'Hernandez', 'HR', 62500.00, '2021-11-27'),
('Emily', 'King', 'Finance', 73500.00, '2020-04-09');

CREATE VIEW IT_EMPLOYEES AS 
SELECT 
	EMPLOYEE_ID,
    CONCAT(FIRST_NAME,' ',LAST_NAME) AS
    FULL_NAME,
    SALARY
FROM EMPLOYEES
WHERE DEPARTMENT = 'IT';

SELECT * FROM IT_EMPLOYEES;

UPDATE IT_EMPLOYEES
SET SALARY = SALARY * 1.10
WHERE EMPLOYEE_ID = 1;

CREATE VIEW AVG_SALARY_BY_DEPT AS 
SELECT 
	DEPARTMENT,
    AVG(SALARY) AS AVG_SALARY
FROM EMPLOYEES
GROUP BY DEPARTMENT;

SELECT * FROM AVG_SALARY_BY_DEPT;
