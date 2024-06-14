DROP TABLE Registration;
DROP TABLE Viewing;
DROP TABLE PropertyForRent;
DROP TABLE Client;
DROP TABLE PrivateOwner;
DROP TABLE Staff;
DROP TABLE Branch;


CREATE TABLE Branch (
branchNo CHAR(4) NOT NULL,
street   VARCHAR(50),
city     VARCHAR(50),
postcode VARCHAR(10),
PRIMARY KEY (branchNo)
);

CREATE TABLE Staff (
staffNo CHAR(4) NOT NULL,
fName   VARCHAR(50),
lName     VARCHAR(50),
position VARCHAR(50),
sex      CHAR(1),
DOB      DATE,
salary   INT,
branchNo CHAR(4),
PRIMARY KEY (staffNo),
FOREIGN KEY (branchNo) REFERENCES Branch (branchNo) 
);

CREATE TABLE PrivateOwner (
ownerNo CHAR(4) NOT NULL,
fName   VARCHAR(50),
lName     VARCHAR(50),
address VARCHAR(50),
telNo      CHAR(20),
email      VARCHAR(50),
password   VARCHAR(50),
PRIMARY KEY (ownerNo)
);

CREATE TABLE Client (
clientNo CHAR(4) NOT NULL,
fName   VARCHAR(50),
lName     VARCHAR(50),
telNo      CHAR(20),
prefType   VARCHAR(50),
maxRent    INT,
email      VARCHAR(50),
PRIMARY KEY (clientNo)
);


CREATE TABLE PropertyForRent (
propertyNo CHAR(4) NOT NULL,
street   VARCHAR(50),
city     VARCHAR(50),
postcode VARCHAR(10),
type      CHAR(10),
rooms      SMALLINT,
rent   INT,
ownerNo  CHAR(4),
staffNo  CHAR(4),
branchNo CHAR(4),
PRIMARY KEY (propertyNo),
FOREIGN KEY (branchNo) REFERENCES Branch (branchNo),
FOREIGN KEY (staffNo) REFERENCES Staff (staffNo),
FOREIGN KEY (ownerNo) REFERENCES PrivateOwner (ownerNo) 
);

CREATE TABLE Viewing (
clientNo CHAR(4) NOT NULL,
propertyNo CHAR(4) NOT NULL,
viewDate   DATE,
comment VARCHAR(100),
PRIMARY KEY (clientNo,propertyNo),
FOREIGN KEY (clientNo) REFERENCES Client (clientNo),
FOREIGN KEY (propertyNo) REFERENCES PropertyForRent (propertyNo)
);

CREATE TABLE Registration (
clientNo CHAR(4) NOT NULL,
branchNo CHAR(4) NOT NULL,
staffNo CHAR(4),
dateJoined   DATE,
PRIMARY KEY (clientNo,branchNo),
FOREIGN KEY (clientNo) REFERENCES Client (clientNo),
FOREIGN KEY (branchNo) REFERENCES Branch (branchNo),
FOREIGN KEY (staffNo) REFERENCES Staff (staffNo)
);
