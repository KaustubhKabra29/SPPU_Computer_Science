#! /bin/bash

echo SQL username:
read USER

echo SQL password:
read PASS

mysql --user=$USER --password=$PASS moviedb << END_SQL


/*person table schema*/
CREATE TABLE Person(
    Person_Id INTEGER NOT NULL AUTO_INCREMENT,
    Gender char(1) NOT NULL,
    First_Name VARCHAR(30) NOT NULL,
    Middle_Name VARCHAR(30),
    Last_Name VARCHAR(30) NOT NULL,
    DOB DATE NOT NULL,
    PRIMARY KEY(Person_Id),
    UNIQUE(First_Name,Last_Name,DOB,Gender),
    CHECK (Gender IN('M','F','O'))
);


/*Award Table Schema*/
CREATE TABLE Award(
    Award_Id INTEGER NOT NULL AUTO_INCREMENT,
    Name VARCHAR(50),
    Title VARCHAR(30),
    Year INTEGER,
PRIMARY KEY(Award_Id)
);


/* Shows Table */

CREATE TABLE Shows(
    Show_Id INTEGER NOT NULL AUTO_INCREMENT,
    Title VARCHAR(30),
    Language VARCHAR(30),
    Ranking INTEGER,
    Rating FLOAT,
    Certification VARCHAR (10),
    Budget INTEGER,
    Release_Countries VARCHAR(30),
    Locations_Made_In VARCHAR(30),
    PRIMARY KEY(Show_Id),
    CHECK (VALUE IN ('U','U/A','A','PG-13'))
);

/*Persons Nominated table Schema*/
CREATE TABLE PersonsNominated(
    Person_Id INTEGER NOT NULL,
    Award_Id INTEGER NOT NULL,
    PRIMARY KEY(Person_Id, Award_Id),
    FOREIGN KEY(Person_Id) REFERENCES Person(Person_Id),
    FOREIGN KEY(Award_Id) REFERENCES Award(Award_Id)
);

/*Shows Nominated */
CREATE TABLE ShowsNominated(
    Show_Id INTEGER NOT NULL,
    Award_Id INTEGER NOT NULL,
    PRIMARY KEY(Show_Id, Award_Id),
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id),
    FOREIGN KEY(Award_Id) REFERENCES Award(Award_Id)
);


/* Table organization */

CREATE TABLE Organization(
    Organization_Id INTEGER NOT NULL,
    Name VARCHAR(100),
    PRIMARY KEY(Organization_Id)
);

/*Table presented by*/
CREATE TABLE Presented_By(
    Award_Id INTEGER NOT NULL,
    Organization_Id INTEGER NOT NULL,
    PRIMARY KEY(Award_Id),
    FOREIGN KEY(Award_Id) REFERENCES Award(Award_Id),
    FOREIGN KEY(Organization_Id) REFERENCES Organization(Organization_Id)
);

/*Won by Table 

CREATE TABLE Won_by(
    Award_Id INTEGER NOT NULL,
    Person_Id INTEGER,
    Show_Id INTEGER,
    PRIMARY KEY(Award_Id),
    FOREIGN KEY(Award_Id) REFERENCES Awards(Award_Id),
    FOREIGN KEY(Person_Id) REFERENCES Person(Person_Id),
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id)
);

*/


/* Actor Table */

CREATE TABLE Actor(
    Person_Id INTEGER NOT NULL,
    Screen_Name VARCHAR(30),
    Stage_Name VARCHAR(30),
    Net_Worth INTEGER,
    Since_Year INTEGER,
    PRIMARY KEY(Person_Id),
    FOREIGN KEY(Person_Id) REFERENCES Person(Person_Id) ON DELETE CASCADE
);


/* Acting Table */


CREATE TABLE Acting(
    Actor_Id INTEGER NOT NULL,
    Show_Id INTEGER NOT NULL,
    Role_First_Name VARCHAR(50),
    Role_Last_Name VARCHAR(50),
    PRIMARY KEY(Actor_Id,Show_Id),
    FOREIGN KEY(Actor_Id) REFERENCES Actor(Person_Id) ON DELETE CASCADE,
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id) ON DELETE CASCADE
);

/* Director Table */

CREATE TABLE Director(
    Person_Id INTEGER NOT NULL,
    Direction_Type VARCHAR(10),
    Since_Year INTEGER,
    PRIMARY KEY(Person_Id),
    CHECK (Direction_Type IN(‘Music’,’Movie’,’Dance’,’Art’)),
    FOREIGN KEY(Person_Id) REFERENCES Person(Person_Id) ON DELETE CASCADE
);

/* Direction Table */

CREATE TABLE Direction(
    Director_Id INTEGER NOT NULL,
    Show_Id INTEGER NOT NULL,
    PRIMARY KEY(Director_Id,Show_Id),
    FOREIGN KEY(Director_Id) REFERENCES Director(Person_Id) ON DELETE CASCADE,
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id) ON DELETE CASCADE
);

/* Producer Table */

CREATE TABLE Producer(
    Person_Id INTEGER NOT NULL,
    PRIMARY KEY(Person_Id),
    FOREIGN KEY(Person_Id) REFERENCES Person(Person_Id) ON DELETE CASCADE
);


/* Production Company Table */

CREATE TABLE Production_Company(
    Production_company_Id INTEGER NOT NULL,
    Name VARCHAR(30),
    Location VARCHAR(30),
    Address VARCHAR(200),
    PRIMARY KEY(Production_company_Id)
);

/* Produces Table */

CREATE TABLE Produces(
    Production_company_Id INTEGER NOT NULL,
    Show_Id INTEGER NOT NULL,
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id) ON DELETE CASCADE,
    FOREIGN KEY(Production_company_Id) REFERENCES Production_Company(Production_company_Id) ON DELETE CASCADE,
    PRIMARY KEY(Production_company_Id,Show_Id)  
);

/* Owns Table */

CREATE TABLE Owns(
    Producer_Id INTEGER NOT NULL,
    Production_company_Id INTEGER NOT NULL,
    FOREIGN KEY(Producer_Id) REFERENCES Producer(Person_Id) ON DELETE CASCADE,
    FOREIGN KEY(Production_company_Id) REFERENCES Production_Company(Production_company_Id) ON DELETE CASCADE,
    PRIMARY KEY(Producer_Id,Production_company_Id)
);    

/* Writer Table */

CREATE TABLE Writer(
    Person_Id INTEGER NOT NULL,
    PRIMARY KEY(Person_Id),
    FOREIGN KEY(Person_Id) REFERENCES Person(Person_Id) ON DELETE CASCADE
);

/* Written Table */

CREATE TABLE Written(
    Writer_Id INTEGER NOT NULL,
    Show_Id INTEGER NOT NULL,
    PRIMARY KEY(Writer_Id,Show_Id),
    FOREIGN KEY(Writer_Id) REFERENCES Writer(Person_Id) ON DELETE CASCADE,
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id) ON DELETE CASCADE
);

/* Cinematographer Table */

CREATE TABLE Cinematographer(
    Person_Id INTEGER NOT NULL,
    PRIMARY KEY(Person_Id),
    FOREIGN KEY(Person_Id) REFERENCES Person(Person_Id) ON DELETE CASCADE
);

/* Shooting Table */

CREATE TABLE Shooting(
    Cinematographer_Id INTEGER NOT NULL,
    Show_Id INTEGER NOT NULL,
    PRIMARY KEY(Cinematographer_Id ,Show_Id),
    FOREIGN KEY(Cinematographer_Id) REFERENCES Cinematographer(Person_Id) ON DELETE CASCADE,
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id) ON DELETE CASCADE
);

/* Editor Table */

CREATE TABLE Editor(
    Person_Id INTEGER NOT NULL,
    PRIMARY KEY(Person_Id),
    FOREIGN KEY(Person_Id) REFERENCES Person(Person_Id) ON DELETE CASCADE
);

/* Editing Table */

CREATE TABLE Editing(
    Editor_Id INTEGER NOT NULL,
    Show_Id INTEGER NOT NULL,
    Software_used VARCHAR(100),
    PRIMARY KEY(Editor_Id ,Show_Id),
    FOREIGN KEY(Editor_Id) REFERENCES Editor(Person_Id) ON DELETE CASCADE,
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id) ON DELETE CASCADE
);

/* Distributor Table */

CREATE TABLE Distributor(
    Person_Id INTEGER NOT NULL,
    PRIMARY KEY(Person_Id),
    FOREIGN KEY(Person_Id) REFERENCES Person(Person_Id) ON DELETE CASCADE
);

/* Distributing Table*/

CREATE TABLE Distributing(
    Distributor_Id Integer NOT NULL,
    Show_Id Integer NOT NULL,
    PRIMARY KEY(Distributor_Id ,Show_Id),
    FOREIGN KEY(Distributor_Id ) REFERENCES Distributor(Person_Id) ON DELETE CASCADE,
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id) ON DELETE CASCADE
);

/* User Table */

CREATE TABLE User(
    Person_Id INTEGER NOT NULL,
    User_Id VARCHAR(30),
    PRIMARY KEY(Person_Id),
    UNIQUE(User_Id),
    FOREIGN KEY(Person_Id) REFERENCES Person(Person_Id) ON DELETE CASCADE
);

/* Critic Table */

CREATE TABLE Critic(
    Person_Id INTEGER NOT NULL,
    User_Id VARCHAR(30),
    PRIMARY KEY(Person_Id),
    FOREIGN KEY(Person_Id) REFERENCES User(Person_Id) ON DELETE CASCADE
);


/* Regular table */


CREATE TABLE Regular_User(
    Person_Id INTEGER NOT NULL,
    User_Id VARCHAR(30) NOT NULL,
    PRIMARY KEY(User_Id),
    FOREIGN KEY(Person_Id) REFERENCES User(Person_Id) ON DELETE CASCADE
);

/* Reviews table */

CREATE TABLE Reviews(
    Review_Id INTEGER NOT NULL,
    User_Id VARCHAR(30) NOT NULL,
    Show_Id Integer NOT NULL,
    UP_Votes INTEGER,
    Down_Votes INTEGER,
    Rating FLOAT,
    Review_Description VARCHAR(20000),
    Reviwed_Date DATE,
    PRIMARY KEY(Review_Id),
    FOREIGN KEY(User_Id) REFERENCES User(User_Id) ON DELETE CASCADE
);





/* Movie Table */

CREATE TABLE Movies(
    Show_Id INTEGER NOT NULL,
    Duration FLOAT,
    Release_Date DATE,
    Year INTEGER,
    PRIMARY KEY(Show_Id),
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id) ON DELETE CASCADE
);

/* Box ofc collections Table */

CREATE TABLE Box_Office_Collections(
    Movie_Id INTEGER NOT NULL,
    First_Week_Collections FLOAT,
    Overall_USA_Collections FLOAT,
    Overall_Worldwide_Collections FLOAT,
    Currency VARCHAR(10),
    PRIMARY KEY(Movie_Id),
    FOREIGN KEY(Movie_Id) REFERENCES Movies(Show_Id) ON DELETE CASCADE
);

/* TV Series Table */

CREATE TABLE TVSeries(
    Show_Id INTEGER NOT NULL,
    Start_date DATE,
    End_date DATE,
    Air_Channel VARCHAR(50),
    Air_Day VARCHAR(30),
    Air_time TIME,
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id) ON DELETE CASCADE,
    PRIMARY KEY(Show_Id)
);

/* Seasons Table */

CREATE TABLE Seasons(
    Season_Id INTEGER NOT NULL,
    Season_Name VARCHAR(30),
    Start_date DATE,
    End_date DATE,
    Season_number INTEGER,
    Show_Id Integer NOT NULL,
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id) ON DELETE CASCADE,
    PRIMARY KEY(Season_Id)
);

/* Episodes Table */

CREATE TABLE Episodes(
    Episode_Id Int NOT NULL,
    Episode_Title VARCHAR(50),
    Air_date DATE,
    Duration FLOAT,
    Season_Id INTEGER NOT NULL,
    FOREIGN KEY(Season_Id) REFERENCES Seasons(Season_Id) ON DELETE CASCADE,
    PRIMARY KEY(Episode_Id)
);



/*Genre table Schema*/
CREATE TABLE Genres(
    Genre_Id INTEGER NOT NULL,
    Name VARCHAR(30),
    PRIMARY KEY(Genre_Id)
    );

/*In_Genre table Schema*/
CREATE TABLE In_Genre(
    Genre_Id INTEGER NOT NULL,
    Show_Id INTEGER NOT NULL,
    PRIMARY KEY(Genre_Id, Show_Id),
    FOREIGN KEY(Genre_Id) REFERENCES Genres(Genre_Id),
    FOREIGN KEY(Show_Id) REFERENCES Shows(Show_Id)
 );

END_SQL

