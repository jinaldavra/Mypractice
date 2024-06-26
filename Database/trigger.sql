1] Example of INSERT:

CREATE DATABASE SHOPPING;

CREATE TABLE SHOPPING.ORDERS(
		ORDER_ID INT AUTO_INCREMENT PRIMARY KEY,
        ORDER_DATE DATE,
        CUSTOMER_NAME VARCHAR(255),
        TOTAL_AMOUNT DECIMAL(10,2)
);

CREATE TABLE SHOPPING.ORDER_LOG(
	LOG_ID INT AUTO_INCREMENT PRIMARY KEY,
    LOG_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ORDER_ID INT,
    ORDER_DATE DATE,
    CUSTOMER_NAME VARCHAR(255),
    TOTAL_AMOUNT DECIMAL(10,2)
);

DELIMITER //
CREATE TRIGGER LOG_NEW_ORDER
AFTER INSERT ON ORDERS
FOR EACH ROW
BEGIN
	INSERT INTO ORDER_LOG(ORDER_ID,ORDER_DATE,CUSTOMER_NAME,TOTAL_AMOUNT)
    VALUES(NEW.ORDER_ID,NEW.ORDER_DATE,NEW.CUSTOMER_NAME,NEW.TOTAL_AMOUNT);
END //
DELIMITER ;

INSERT INTO SHOPPING.ORDERS(ORDER_DATE,CUSTOMER_NAME,TOTAL_AMOUNT)
VALUES('2023-09-08','JOHN DOE',100.00);

2] Example of UPDATE:

USE SHOPPING;

CREATE TABLE SHOPPING.employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100),
    salary DECIMAL(10, 2)
);

CREATE TABLE SHOPPING.employees_audit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employee_id INT,
    old_name VARCHAR(100),
    old_position VARCHAR(100),
    old_salary DECIMAL(10, 2),
    new_name VARCHAR(100),
    new_position VARCHAR(100),
    new_salary DECIMAL(10, 2),
    changed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

DELIMITER //

CREATE TRIGGER before_employee_update
BEFORE UPDATE ON employees
FOR EACH ROW
BEGIN
    INSERT INTO employees_audit (employee_id, old_name, old_position, old_salary, new_name, new_position, new_salary)
    VALUES (OLD.id, OLD.name, OLD.position, OLD.salary, NEW.name, NEW.position, NEW.salary);
END //

DELIMITER ;

INSERT INTO SHOPPING.employees (name, position, salary) VALUES ('John Doe', 'Software Engineer', 60000);

UPDATE SHOPPING.employees SET name = 'John Smith', position = 'Senior Software Engineer', salary = 75000 WHERE id = 1;




