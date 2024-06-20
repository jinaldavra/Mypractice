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