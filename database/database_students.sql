# SHOW DATABASES;
USE flask_project;

CREATE TABLE students(
    StudentID int not null AUTO_INCREMENT,
    FirstName varchar(100) NOT NULL,
    SurName varchar(100) NOT NULL,
    PRIMARY KEY (StudentID)
);

INSERT INTO students(FirstName, SurName)
VALUES("John", "Andersen"), ("Emma", "Smith");

SELECT * FROM students;