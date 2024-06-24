1] Create function : 

CREATE DATABASE MATHS;

USE MATHS;

DELIMITER //
CREATE FUNCTION calculate_area(radius FLOAT)
RETURNS FLOAT
DETERMINISTIC
BEGIN 
	DECLARE area FLOAT;
    SET area = P1() * radius * radius;
    RETURN area;
END //
DELIMITER //

2] Using select statement :

SELECT calculate_area(5.0);
DELIMITER //
CREATE FUNCTION square(x INT)
	RETURNS int
    DETERMINISTIC
BEGIN
	DECLARE RESULT INT;
    SET RESULT = X * X;
    RETURN RESSULT;
END;
//
DELIMITER //

3] Integrating into an INSERT or UPDATE statement :

INSERT INTO CIRCLE_AREAS(RADIUS,AREA)
VALUES(5.0,CALCULATE_AREA(5.0));

SELECT * FROM CIRCLES WHERE CALCULATE_AREA(RADIUS) > 50.0;

4] Deterministic function example :

DELIMITER //
CREATE FUNCTION calculate_area(radius FLOAT)
RETURNS float
DETERMINISTIC
BEGIN 
	DECLARE area FLOAT;
    SET area = PI() * radius * radius;
    RETURN area;
END //

5] Non- deterministic function example :

DELIMITER //
CREATE FUNCTION current_datetime()
RETURNS DATETIME
NOT DETERMINISTIC
BEGIN
	DECLARE current_time DATETIME;
    SET current_time = NOW();
    RETURN current_time;
END;

6] EXAMPLE OF FUNCTION :

CREATE DATABASE FUN;

USE FUN;

CREATE TABLE CUSTOMER(
	CUST_ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL,
    OCCUPATION VARCHAR(255) NOT NULL,
    AGE INT NOT NULL
);

INSERT INTO CUSTOMER(CUST_ID,NAME,OCCUPATION,AGE)
VALUES
(101,'PETER','ENGINEER',32),
(102,'JOSEPH','DEVELOPER',30),
(103,'JOHN','LEADER',28),
(104,'STEPHEN','SCIENTIST',45),
(105,'SUZI','CARPENTER',26),
(106,'BOB','ACTOR','25');

DELIMITER //
CREATE FUNCTION CUSTOMER_OCCUPATION(AGE INT)
RETURNS INT
DETERMINISTIC
BEGIN 
	DECLARE CUSTOMER_OCCUPATION VARCHAR(255);
    IF AGE > 35 THEN
		SET CUSTOMER_OCCUPATION = 'SCIENTIST';
	ELSEIF (AGE <= 35 AND AGE >= 30) THEN
		SET CUSTOMER_OCCUPATION = 'ENGINEER';
	ELSEIF AGE < 30 THEN
		SET CUSTOMER_OCCUPATION = 'ACTOR';
	END IF;
    RETURN (CUSTOMER_OCCUPATION);
    END //
    DELIMITER ;
    
    SELECT NAME, AGE, CUSTOMER_OCCUPATION(AGE)
    FROM CUSTOMER ORDER BY AGE;