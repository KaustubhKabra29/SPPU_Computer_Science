#! /bin/bash

echo SQL username:
read USER

echo SQL password:
read PASS

mysql --user=$USER --password=$PASS moviedb << END_SQL

/*Sample Datasets*/

/*sample dataset for person*/
INSERT INTO Person
(Gender, First_Name, Middle_Name, Last_Name, DOB)
VALUES
('F' , 'Meryl', null, 'Streep', '1990-08-15'),
('M', 'Robert', null, 'Downey', '1965-4-4'),
('M', 'John', null, 'Krasinski', '1979-10-20'),
('M', 'Anthony', null, 'Russo', '1970-02-03'),
('F', 'Emma', null, 'Stone', '1988-11-06'),
('F', 'Gal', null, 'Gadot', '1985-04-30'),
('F', 'Patty', null, 'Jenkins', '1971-07-24'),
('M', 'Peter', null, 'Dinklage', '1971-07-24'),
('F', 'Milly', 'Bobby', 'Brown', '1971-07-24'),
('M', 'Kumail', null, 'Nanjiani', '1971-07-24'),
('F', 'Emilia', null, 'Clarke', '1971-07-24'),
('M', 'Damien', null, 'Chazelle', '1985-01-19'),
('M', 'Ramin', null, 'Djawadi', '1974-07-19'),
('M', 'Matt', null, 'Duffer', '1984-02-15'),
('M', 'Ross', null, 'Duffer', '1984-02-15'),
('M', 'David', null, 'Russell', '1958-08-20'),
('M', 'Matthew', null, 'Jensen', null),
('F', 'Charlotte', 'Bruss', 'Christensen', '1978-03-20'),
('M', 'User', null, '1', null),
('F', 'User', null, '2', '1999-03-20'),
('F', 'Emily', null, 'Blunt', '1983-02-23'),
('M', 'Chris', null, 'Evans', '1981-06-13'),
('M', 'Chris', null, 'Pine', '1980-08-26'),
('M', 'Ryan', null, 'Gosling', '1980-11-12'),
('M', 'Steve', null, 'Carell', '1962-08-16'),
('F', 'Mandy', null, 'Moore', '1984-04-10'),
('M', 'Tom', null, 'Cross', null),
('M', 'Joe', null, 'Russo', '1971-07-08');

/*sample dataset for Shows*/
INSERT INTO Shows
(Title, Language, Rating, Certification, Budget)
VALUES
('The Devil Wears Prada ', 'English', 6.9, 'PG-13', 35000000 ),
('Captain America: Civil War', 'English', 7.8, 'PG-13', 250000000),
('A Quiet Place', 'English', 7.6, 'PG-13', 17000000),
('Wonder Woman', 'English', 7.5, 'PG-13', 149000000),
('La La Land', 'English', 8.1, 'PG-13', 30000000),
('Stranger Things', 'English', 8.9, 'TV-14', null),
('Game of Thrones', 'English', 9.5, 'TV-MA', null),
('Silicon Valley', 'English', 8.6, 'TV-MA', null),
('Despicable Me', 'English', 7.7, 'PG', 69000000),
('Coco', 'English', 8.4, 'PG', 175000000),
('The Office', 'English', 8.8, 'TV-PG', null),
('Avengers: Infinity War', 'English', 8.5, 'PG-13', 321000000),
('Birdman', 'English', 7.7, 'R', 18000000),
('Before We Go', 'English', 6.8, 'PG-13', null),
('This is Us', 'English', 8.8, 'TV-14', null),
('A Walk to Remember', 'English', 7.4, 'PG', 11000000),
('The Notebook', 'English', 7.9, 'PG-13', 29000000);

/*sample dataset for Genre*/
INSERT INTO Genres
 (Genre_Id, Name)
VALUES
  (1, 'Action'),
  (2, 'Comedy'),
  (3, 'Drama'),
  (4, 'Romance'),
  (5, 'Sci-Fi'),
  (6, 'Adventure'),
  (7, 'Horror'),
  (8, 'Mystery'),
  (9, 'Music'),
  (10, 'Fantasy'),
  (11, 'Animation'),
  (12, 'Family');

/*sample dataset for In_Genre*/
INSERT INTO In_Genre
(Show_Id, Genre_Id)
VALUES
  (1,2),
  (1,3),
  (2,1),
  (2,5),
  (2,6),
  (3,3),
  (3,7),
  (3,8),
  (4,1),
  (4,6),
  (4,2),
  (5,2),
  (5,3),
  (5,8),
  (6,3),
  (6,7),
  (6,1),
  (7,1),
  (7,3),
  (7,6),
  (8,2),
  (9,11),
  (9,2),
  (9,12),
  (10,11),
  (10,6),
  (10,10),
  (11,2),
  (12,1),
  (12,6),
  (12,10),
  (13,2),
  (13,3),
  (14,2),
  (14,3),
  (14,4),
  (15,2),
  (15,3),
  (15,4),
  (16,3),
  (16,4),
  (17,3),
  (17,4);

/*sample dataset for Award*/
INSERT INTO Award
(Name, Title, Year)
VALUES
  ('Golden Globe', 'Best Actress in Supporting Role', 2015),
  ('Oscar', 'Best Actress in Supporting Role', 2015),
  ('Oscar', 'Best Picture', 2015),
  ('Oscar', 'Best Animated Film', 2018),
  ('Oscar', 'Best Actress', 2007),
  ('Golden Globe', 'Best Actress in Supporting Role', 2017),
  ('Oscar', 'Best Actress', 2017),
  ('Oscar', 'Best Director', 2017),
  ('Oscar', 'Best Picture', 2017),
 ('Critics Choice', 'Best Picture', 2016),
  ('Critics Choice', 'Best Editing', 2016),
  ('Critics Choice', 'Best Actor', 2016),
  ('Critics Choice', 'Best Movie', 2018),
  ('Golden Globe', 'Best TV Series - Drama', 2018),
  ('Critics Choice', 'Best Drama Series', 2018),
  ('Critics Choice', 'Best Supporting Actor', 2018),
  ('Critics Choice', 'Best Supporting Actress', 2018);

/*sample dataset for PersonsNominated*/
INSERT INTO PersonsNominated
(Person_Id, Award_Id)
VALUES
  (5,1),
  (5,2),
  (1,5),
  (26,6),
  (5,7),
  (12,8),
  (24,12),
  (8,16),
  (11,17),
  (27,11);

/*sample dataset for ShowsNominated*/
INSERT INTO ShowsNominated
(Show_Id, Award_Id)
VALUES
  (13,3),
  (10,4),
  (5,9),
  (5,10),
  (4,13),
  (7,14),
  (6,15);

/*sample dataset for Organization*/
INSERT INTO Organization
(Organization_Id, Name)
VALUES
  (1, 'HPFA'),
  (2, 'AMPAS'),
  (3, 'BFCA');

/*sample dataset for Presented_By*/
INSERT INTO Presented_By
(Award_Id, Organization_Id)
VALUES
  (1,1),
  (2,2),
  (3,2),
  (4,2),
  (5,2),
  (6,1),
  (7,2),
  (8,2),
  (9, 2),
  (10,2),
  (11,2),
  (12,2),
  (13,2),
  (14,1),
  (15,3),
  (16,3),
  (17,3);

/*sample dataset for Actor*/
INSERT INTO Actor
(Person_Id, Net_Worth, Since_Year)
VALUES
  (1, 90, 1969),
  (2, 300, 1970),
  (3, 30, 2000),
  (5, 28, 2004),
  (6, 10, 2004),
  (8, 15, 1995),
  (9, 3, 2013),
  (10, 6, 2008),
  (11, 13, 2009),
  (21, 16, 2004),
  (22, 50, 1995),
  (23, 20, 2013),
  (24, 60, 2008),
  (25, 50, 2009),
  (26, 10, 2009);

/*sample dataset for Acting*/
INSERT INTO Acting
(Actor_Id, Show_Id, Role_First_Name, Role_Last_Name)
VALUES
  (1,1, 'Miranda', 'Priestly'),
  (21,1, 'Emily', null),
  (2,2, 'Tony', 'Stark'),
  (22,2, 'Steve', 'Rogers'),
  (3,3, 'Lee', 'Abbott'),
  (21,3, 'Evelyn', 'Abbott'),
  (6,4, 'Diana', null),
  (23,4, 'Steve', 'Trevor'),
  (5,5, 'Mia', null),
  (24,5, 'Sebastian', null),
  (9,6, 'Eleven', null),
  (8,7, 'Tyrion', 'Lannister'),
  (11,7, 'Daenerys', 'Targaryen'),
  (10,8, 'Dinesh', 'Chugtai'),
  (25,9, 'Gru', null),
  (25,11, 'Michael', 'Scott'),
  (3,11, 'Jim', 'Halpert'),
  (2,12, 'Tony', 'Stark'),
  (22,12, 'Steve', 'Rogers'),
  (5,13, 'Sam', null),
  (22,14, 'Nick', null),
  (26,15, 'Rebecca', 'Pearson'),
  (26,16, 'Jamie', 'Sullivan'),
  (24,17, 'Noah', null);

/*sample dataset for Director*/
INSERT INTO Director
(Person_Id, Direction_Type,Since_Year)
VALUES
  (3, 'Movie', 2010),
  (4, 'Movie', 1994),
  (28, 'Movie', 1994),
  (7, 'Movie', 1995),
  (13, 'Music', 1998),
  (12, 'Movie', 2009),
  (14, 'Movie', 2005),
  (15, 'Movie', 2005),
  (22, 'Movie', 2014);

/*sample dataset for Direction*/
INSERT INTO Direction
(Director_Id, Show_Id)
VALUES
  (3,3),
  (4,2),
  (7,4),
  (12,5),
  (13,7),
  (14, 6),
  (15, 6),
  (22,14);

/*sample dataset for Producer*/
INSERT INTO Producer
(Person_Id)
VALUES
  (3),
  (4),
  (7);

/*sample dataset for Production_Company*/
INSERT INTO Production_Company
(Production_Company_Id, Name, Location, Address)
VALUES
  (1, 'Marvel Studios ', 'California', '500 S. Buena Vista Street, Burbank, California United States'),
  (2, 'DC Entertainment ', null, null),
  (3, 'Summit Entertainment ', 'California', null);

/*sample dataset for Produces*/
INSERT INTO Produces
(Production_company_Id, Show_Id)
VALUES
  (3,3),
  (1,6);

/*sample dataset for Owns*/
INSERT INTO Owns
(Producer_Id, Production_company_Id)
VALUES
  (3,3),
  (7,1);

/*sample dataset for Writer*/
INSERT INTO Writer
(Person_Id)
VALUES
  (12),
  (14),
  (15),
  (16);

/*sample dataset for Written*/
INSERT INTO Written
(Writer_Id, Show_Id)
VALUES
  (12,5),
  (14,6),
  (15,6),
  (16,1);

/*sample dataset for Cinematographer*/
INSERT INTO Cinematographer
(Person_Id)
VALUES
  (17),
  (18);

/*sample dataset for Shooting*/
INSERT INTO Shooting
(Cinematographer_Id, Show_Id)
VALUES
  (17,4),
  (18,3);

/*sample dataset for Editor*/
INSERT INTO Editor
(Person_Id)
VALUES
  (27);

/*sample dataset for Editing*/
INSERT INTO Editing
(Editor_Id, Show_Id, Software_used)
VALUES
  (27,5,'Adobe');

/*sample dataset for Distributor*/
INSERT INTO Distributor
(Person_Id)
VALUES
  (3),
  (4),
  (7);

/*sample dataset for Distributing*/
INSERT INTO Distributing
(Distributor_Id, Show_Id)
VALUES
  (3,3),
  (4,2),
  (7,4);

/*sample dataset for User*/
INSERT INTO User
(Person_Id, User_Id)
VALUES
  (19, 'janu@123'),
  (20, 'vamsee@123');


/*sample dataset for Critic*/
INSERT INTO Critic
(Person_Id, User_Id)
VALUES
 (19, 'janu@123');


/*sample dataset for Regular_User*/
INSERT INTO Regular_User
(Person_Id, User_Id)
VALUES
  (20, 'vamsee@123');


/*sample dataset for Reviews*/
INSERT INTO Reviews
  (Review_Id, User_Id, Show_Id, UP_Votes, Down_Votes, Rating, Review_Description, Reviwed_Date)
VALUES
  (1,'vamsee@123', 1, 5, 0, 5, 'very good movie, mush watch',  '2016-07-15'),
  (2, 'janu@123', 4, 5, 0, 5, 'the best female superhero movie of all timer',  '2017-07-15'),
  (3, 'janu@123', 6, 5, 0, 5, 'the show keeps you insanely captivated throughout',  '2017-07-15'),
  (4, 'vamsee@123', 2, 5, 0, 5, 'the best marvel movie so far',  '2017-07-15');

/*sample dataset for Movies*/
INSERT INTO Movies
(Show_Id, Duration, Release_Date, Year)
VALUES
(1, 109, '2006-06-30', 2006),
(2, 147, '2016-05-06', 2016),
(3, 90, '2018-04-06', 2018),
(4, 141, '2017-06-02', 2017),
(5, 128, '2016-12-25', 2016),
(9, 95, '2010-07-09', 2010),
(10, 105, '2017-11-22', 2017),
(12, 149, '2018-04-27', 2018),
(13, 119, '2014-11-14', 2014),
(14, 95, '2015-07-21', 2015),
(16, 102, '2002-01-25', 2002),
(17, 124, '2004-06-25', 2004);

/*sample dataset for Box_Office_Collections*/
INSERT INTO Box_Office_Collections
(Movie_Id, First_Week_Collections, Overall_USA_Collections, Overall_Worldwide_Collections, Currency)
VALUES
(1, 27537244, 124740460, 326551094, 'Dollars'),
(2, 179139142, 408084349,1153304495, 'Dollars'),
(3, 50203562, 188024361,332583447, 'Dollars'),
(4, 103251471, 412563408, 821763408, 'Dollars'),
(5, 881104, 151101803, 44609357, 'Dollars'),
(9, 56397125, 251513985, 543113985, 'Dollars'),
(10, 50802605, 209726015, 807082196, 'Dollars'),
(12, 257698183, 678815482, 2046900111, 'Dollars'),
(13, 424397, 42340598, 103215094, 'Dollars'),
(14, 3225, 37047, null, 'Dollars'),
(16, 12177488, 41227069, null, 'Dollars'),
(17, 13464745, 81001787, 116072707, 'Dollars');

/*sample dataset for TVSeries*/
INSERT INTO TVSeries
(Show_Id, Start_Date, End_Date, Air_Channel, Air_Day, Air_Time)
VALUES
(6, '2016-07-15', null, 'Netflix', null, null),
(7, '2011-04-11', null, 'HBO', 'Sunday', '21:00:00'),
(8, '2014-04-06', null, 'HBO', 'Sunday', null),
(11, '2016-09-20', null, 'NBC', 'Tuesday', '21:00:00'),
(15, '2005-03-24', '2013-05-16', 'NBC', 'Thursday', null);

/*sample dataset for Seasons*/
INSERT INTO Seasons
(Season_Id, Season_Name, Start_Date, End_Date, Season_number, Show_Id)
VALUES
(1, null,  '2016-07-15', null, 1, 6),
(2, null,  '2017-10-27', null, 2, 6),
(3, null,  '2011-04-17',  '2011-06-19', 1, 7),
(4, null,  '2012-04-01',  '2012-06-03', 2, 7),
(5, null,  '2013-03-31',  '2013-06-09', 3, 7),
(6, null,  '2014-04-06',  '2014-06-15', 4, 7),
(7, null,  '2015-04-12',  '2015-06-14', 5, 7),
(8, null,  '2016-04-24',  '2016-06-26', 6, 7),
(9, null,  '2017-07-16',  '2017-08-27', 7, 7),
(10, null,  '2014-06-16',  '2014-06-01', 1, 8),
(11, null,  '2015-04-16',  '2015-06-14', 2, 8),
(12, null,  '2016-24-16',  '2016-06-26', 3, 8),
(13, null,  '2017-23-16',  '2017-06-25', 4, 8),
(14, null,  '2018-25-15',  '2018-05-13', 5, 8);

/*sample dataset for Episodes*/
INSERT INTO Episodes
(Episode_Id, Episode_Title, Air_Date, Duration, Season_ID)
VALUES
(1, null,  '2016-07-15', null, 6),
(2, null,  '2017-10-27', null, 6),
(3, null,  '2011-04-17',  20,  7),
(4, null,  '2012-04-01',  20,  7),
(5, null,  '2013-03-31',  20,  7),
(6, null,  '2014-04-06',  22,  7),
(7, null,  '2015-04-12',  31,  7),
(8, null,  '2016-04-24',  55,  7),
(9, null,  '2017-07-16',  10,  7),
(10, null,  '2014-06-16',  44, 8),
(11, null,  '2015-04-16',  16, 8),
(12, null,  '2016-24-16',  33, 8),
(13, null,  '2017-23-16',  23, 8),
(14, null,  '2018-25-15',  45, 8);

END_SQL
