CREATE DATABASE BANK;

USE BANK;

CREATE TABLE ACCOUNTS(
	ACCOUNT_ID INT AUTO_INCREMENT PRIMARY KEY,
    ACCOUNT_HOLDER VARCHAR(255),
    BALANCE DECIMAL(10,2)
);

CREATE TABLE TRANSACTIONS(
	TRANSACTION_ID INT AUTO_INCREMENT PRIMARY KEY,
    ACCOUNT_ID INT,
    AMOUNT DECIMAL(10,2),
    TRANSACTION_TYPE ENUM('DEPOSIT','WITHDRAWL'),
    TRANSACTION_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (ACCOUNT_ID) REFERENCES ACCOUNTS(ACCOUNT_ID)
);

START TRANSACTION;

SELECT BALANCE FROM ACCOUNTS WHERE ACCOUNT_ID = 1;

SAVEPOINT BEFORE_WITHDRAWL;

UPDATE ACCOUNTS
SET BALANCE = BALANCE - 200
WHERE ACCOUNT_ID = 1;

INSERT INTO ACCOUNTS (ACCOUNT_HOLDER, BALANCE) VALUES ('John Doe', 1000.00);

SAVEPOINT AFTER_WITHDRAWL;

UPDATE ACCOUNTS
SET BALANCE = BALANCE + 200
WHERE ACCOUNT_ID = 2;

INSERT INTO ACCOUNTS(ACCOUNT_HOLDER,BALANCE) VALUES('JOSEPH DOE',2000.00);

SAVEPOINT AFTER_DEPOSIT;

SELECT * FROM ACCOUNTS;

SELECT * FROM TRANSACTIONS;

COMMIT;


