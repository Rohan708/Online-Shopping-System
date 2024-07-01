CREATE DATABASE SLR;
use SLR;
 CREATE TABLE SELL(
 S_id INT NOT NULL,
 S_First_Name varchar(100) NOT NULL,
 S_Middle_Name varchar(100) ,
 S_Last_Name varchar(100) ,
 S_Email varchar(100) NOT NULL,
 S_Ph_No varchar(100) NOT NULL,
 S_Adrs varchar(100) NOT NULL,
 S_GST_No varchar(100) NOT NULL,
 S_license varchar(100) NOT NULL,
 S_password varchar(100) NOT NULL,
 
 PRIMARY KEY (S_id)
 );
 Select * from SELL;