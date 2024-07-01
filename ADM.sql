CREATE DATABASE ADM;
use ADM;
CREATE TABLE ADMN(
 A_id INT NOT NULL,
 A_password varchar(100) NOT NULL,
 
 PRIMARY KEY (A_id)
 );
 INSERT INTO ADMN (A_id, A_password)
VALUES (131, 'rohan');

  Select * from ADMN;