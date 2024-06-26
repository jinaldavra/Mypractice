1] Create table :

CREATE DATABASE STUDENT;

CREATE TABLE `STUDENT`.`INFO`
(
	STUDENT_ID INT,
    FIRSTNAME VARCHAR(255),
    LASTNAME VARCHAR(255),
    ADDRESS VARCHAR(255)
)

2] Insert data into the table :

CREATE DATABASE STUDENT;

CREATE TABLE `STUDENT`.`INFO`
(
	STUDENT_ID INT,
    FIRSTNAME VARCHAR(255),
    LASTNAME VARCHAR(255),
    ADDRESS VARCHAR(255)
)

INSERT INTO STUDENT.INFO(STUDENT_ID,FIRSTNAME,LASTNAME,ADDRESS) VALUES(1,'JOHN','DOE','XYZ');
INSERT INTO STUDENT.INFO(STUDENT_ID,FIRSTNAME,LASTNAME,ADDRESS) VALUES(2,'ZAIN','MALIK','ABC');
INSERT INTO STUDENT.INFO(STUDENT_ID,FIRSTNAME,LASTNAME,ADDRESS) VALUES(3,'LUIS','BIBER','LMN');

3] Create table with constraints :

CREATE DATABASE JINAL;

CREATE TABLE JINAL.INFO
(
	STUDENT_ID INT AUTO_INCREMENT PRIMARY KEY,
    FIRST_NAME VARCHAR(255) NOT NULL,
    LAST_NAME VARCHAR(255) NOT NULL,
    EMAIL VARCHAR(255) UNIQUE,
    MONILE VARCHAR(255) UNIQUE,
    PASSWORD VARCHAR(255)
)

// TO MODIFY COLUMN
ALTER TABLE JINAL.INFO MODIFY MONILE INT UNIQUE;

// ADD NEW COLUMN
ALTER TABLE JINAL.INFO ADD MOBILE INT UNIQUE;

// DELETE COLUMN
ALTER TABLE JINAL.INFO DROP MONILE;

// DELETE TABLE
DROP TABLE JINAL.INFO;

// SHOW TABLE STRUCTURE
DESCRIBE JINAL.INFO;

4] Select data from the table :

// SELECT ALL DATA FROM THE TABLE
SELECT * FROM student.info;

// GET ALL RECORDS WITH SPECIFIC COLUMNS
SELECT FIRSTNAME,LASTNAME FROM STUDENT.INFO;

// GET DATA USING FILTER
SELECT * FROM STUDENT.INFO WHERE STUDENT_ID = 1;

// GET FIRST N RECORDS
SELECT * FROM STUDENT.INFO LIMIT 2;

// GET DATA BY ORDERS
SELECT * FROM STUDENT.INFO ORDER BY ADDRESS;

SELECT * FROM STUDENT.INFO ORDER BY FIRSTNAME;

SELECT * FROM STUDENT.INFO ORDER BY STUDENT_ID DESC LIMIT 3;

5] Update single records in the table :

UPDATE JINAL.INFO
SET EMAIL = 'new_email@example.com',
	MOBILE = '8200524421'
WHERE 'FIRST_NAME' = 'JOHN';

6] Update multiple records in the table :

UPDATE JINAL.INFO SET PASSWORD = 'test@123' WHERE STUDENT_ID < 6;

7] Delete single record :

DELETE FROM JINAL.INFO WHERE STUDENT_ID = 5;

8] Delete multi records based on condition :

DELETE FROM JINAL.INFO WHERE STUDENT_ID > 3;





