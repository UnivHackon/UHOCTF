USE ctf;

CREATE TABLE Student
(
  Student_ID SERIAL NOT NULL,
  Email VARCHAR(128) NOT NULL,
  Username VARCHAR(128) NOT NULL,
  Password VARCHAR(128) NOT NULL,
  Blocked INT NOT NULL,
  Izly_Wallet VARCHAR(256) NOT NULL,
  PRIMARY KEY (Student_ID),
  UNIQUE (Email),
  UNIQUE (Username)
);

CREATE TABLE Interface
(
  Interface_ID SERIAL NOT NULL,
  Student_ID BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (Interface_ID),
  FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID)
);

CREATE TABLE Support_Tickets
(
  Ticket_ID SERIAL NOT NULL,
  Description VARCHAR(2048) NOT NULL,
  Messages VARCHAR(2048) NOT NULL,
  Time_stamp VARCHAR(256) NOT NULL,
  Student_ID BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (Ticket_ID),
  FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID)
);

CREATE TABLE Support_Prof
(
  Staff_ID SERIAL NOT NULL,
  Developer INT,
  Student_ID BIGINT UNSIGNED NOT NULL,
  PRIMARY KEY (Staff_ID),
  FOREIGN KEY (Student_ID) REFERENCES Student(Student_ID)
);



CREATE TABLE Vps
(
  Vps_ID SERIAL NOT NULL,
  OS VARCHAR(32) NOT NULL,
  IP_Address VARCHAR(256) NOT NULL,
  Interface_ID BIGINT UNSIGNED,
  PRIMARY KEY (Vps_ID),
  FOREIGN KEY (Interface_ID) REFERENCES Interface(Interface_ID),
  UNIQUE (IP_Address)
);

