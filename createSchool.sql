--
-- Create a very simplified university database 
--
--
-- Drop tables for house-keeping if necessary
--

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL';

DROP SCHEMA IF EXISTS school;
CREATE SCHEMA school;
USE school;

DROP TABLE IF EXISTS Enroll;
DROP TABLE IF EXISTS Student;
DROP TABLE IF EXISTS Class;
DROP TABLE IF EXISTS Course;
DROP TABLE IF EXISTS Faculty;
DROP TABLE IF EXISTS Department;

--
CREATE TABLE IF NOT EXISTS Department (
    deptCode    VARCHAR(4),
	deptName	VARCHAR(30),
	schoolCode	VARCHAR(3),
	numFaculty	TINYINT,
	CONSTRAINT Department_deptCode_pk PRIMARY KEY (deptCode),
	CONSTRAINT Department_name_ck UNIQUE (deptName)
);

CREATE TABLE IF NOT EXISTS Faculty (
	facId		INT NOT NULL,
	fname	 	VARCHAR(20) NOT NULL,
	lname	 	VARCHAR(20) NOT NULL,
	deptCode	VARCHAR(4) NOT NULL,
	`rank` 		VARCHAR(25),
	passwd    VARCHAR(25) NOT NULL,
	CONSTRAINT Faculty_facId_pk PRIMARY KEY (facId),
	CONSTRAINT Faculty_deptCode_fk FOREIGN KEY (deptCode) 
		REFERENCES Department(deptCode));

CREATE TABLE IF NOT EXISTS Course (
	courseId 	INT NOT NULL,
	rubric		char(4) NOT NULL,
	number	 	char(4) NOT NULL,
	name		VARCHAR(80) NOT NULL,
	CONSTRAINT Course_courseId_pk PRIMARY KEY (courseId));
	
CREATE TABLE IF NOT EXISTS Class (
	classId		INT NOT NULL AUTO_INCREMENT,
	courseId 	INT NOT NULL,
	semester	VARCHAR(10) NOT NULL,
	year		DECIMAL(4,0) NOT NULL,
	facId	 	INT NOT NULL,
	room		VARCHAR(6),
	CONSTRAINT Class_classId_pk PRIMARY KEY (classId),
	CONSTRAINT Class_courseId_fk FOREIGN KEY (courseId) 
		REFERENCES Course(courseId) ON DELETE CASCADE,
	CONSTRAINT Class_facId_fk FOREIGN KEY (facId) 
		REFERENCES Faculty (facId) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS Student	(
	stuId		INT NOT NULL,
	fname	 	VARCHAR(20) NOT NULL,
	lname	 	VARCHAR(20) NOT NULL,
	major		VARCHAR(4) NULL,
	minor		VARCHAR(4) NULL,
	credits  	integer(3) DEFAULT 0,
	advisor		INT NULL,
	CONSTRAINT Student_stuId_pk PRIMARY KEY(stuId),
	CONSTRAINT Student_credits_cc CHECK ((credits>=0) AND (credits < 250)),
	CONSTRAINT Student_major_fk FOREIGN KEY (major) 
		REFERENCES Department(deptCode) ON DELETE CASCADE,
	CONSTRAINT Student_minor_fk FOREIGN KEY (minor) 
		REFERENCES Department(deptCode) ON DELETE CASCADE,
	CONSTRAINT Student_advisor_fk FOREIGN KEY (advisor) 
		REFERENCES Faculty(facId)
); 
	

CREATE TABLE IF NOT EXISTS Enroll(
	stuId		INT NOT NULL,
	classId		INT NOT NULL,
	grade		VARCHAR(2),
	CONSTRAINT Enroll_classId_stuId_pk PRIMARY KEY (classId, stuId),
	CONSTRAINT Enroll_classNumber_fk FOREIGN KEY (classId) 
		REFERENCES Class(classId) ON DELETE CASCADE,	
	CONSTRAINT Enroll_stuId_fk FOREIGN KEY (stuId) 
		REFERENCES Student (stuId) ON DELETE CASCADE
);

INSERT INTO DEPARTMENT VALUES 
	('CSCI','Computer Science','CSE',12),
	('CINF','Computer Information Systems','CSE',5),
	('ITEC','Information Technology','CSE',4),
	('ARTS','Arts','HSH',5),
	('ENGL','English','HSH',12),
	('ACCT','Accounting','BUS',10);

INSERT INTO FACULTY VALUES('1011','Rick','Herzog','CSCI','Professor', 'password'),
	('1012','admin','admin','CSCI','Associate Professor', 'secret');

	
SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;