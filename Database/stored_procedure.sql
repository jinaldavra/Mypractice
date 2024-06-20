USE MATHS;

CREATE TABLE EMPLOYEES(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    salary DECIMAL(10,2) NOT NULL,
    department_id INT NOT NULL,   
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
)

DELIMITER //

CREATE PROCEDURE AddEmployee (
IN empName VARCHAR(50),
IN empSalary DECIMAL(10,2),
IN empDeptId INT
)
BEGIN
INSERT INTO employees (name, salary, department_id)
VALUES (empName, empSalary, empDeptId);
END //

DELIMITER ;

CALL AddEmployee('John Doe', 75000.00, 1);