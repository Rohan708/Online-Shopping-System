CREATE DATABASE BYR;
use BYR;
 CREATE TABLE BUY(
 B_id INT NOT NULL,
 B_First_Name varchar(100) NOT NULL,
 B_Middle_Name varchar(100) ,
 B_Last_Name varchar(100) , 
 B_Email varchar(100) NOT NULL, 
 B_Ph_No varchar(100) NOT NULL,
 B_Adrs varchar(100) NOT NULL,
 B_password varchar(100) NOT NULL,
 
 PRIMARY KEY (B_id)
 );
 Select * from BUY ;
/*SELECT * FROM BUY WHERE B_id = %s AND B_password = %s;

 

 

 