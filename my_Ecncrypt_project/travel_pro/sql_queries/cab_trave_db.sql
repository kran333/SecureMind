-- Author: Kranthi Kumar K
-- Date: 23/09/2019


create DATABASE `travel_cab_db`;
show tables;

create table cab_details(cab_id varchar(45) primary key,cab_name varchar(45));
insert into cab_details values("cab-1","xoylo-cab-white");
insert into cab_details values("cab-2","xoylo-cab-black");
insert into cab_details values("cab-3","xoylo-cab-red");
insert into cab_details values("cab-4","xoylo-cab-blue");
select cab_id from cab_details;

create table cab_status(
cab_id varchar(45) ,
c_status varchar(45),
create_timestamp DATETIME,
update_timestamp DATETIME,
FOREIGN KEY (cab_id) references cab_details(cab_id)
);


insert into cab_status values("cab-1","F",now(),now());
insert into cab_status values("cab-2","F",now(),now());
insert into cab_status values("cab-3","F",now(),now());
insert into cab_status values("cab-4","F",now(),now());

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
INSERT INTO `customer_details` (`customer_name`,`address`,`phone`) VALUES ("Carson Fields","Redruth","3235188324"),("Nathan England","Kasur","3948616088"),("Deacon Ward","Saint-Médard-en-Jalles","4961610540"),("Hamilton Hines","Markham","2257256295"),("Cairo Nelson","Latronico","8393135874"),("Quinn Golden","Roccabruna","0093223279"),("Aquila Ruiz","Montese","8737878136"),("Gabriel Gould","Colmar","2603967457"),("Reese Strickland","Coatbridge","0985155131"),("Chandler Charles","Glenrothes","7670673309");
INSERT INTO `customer_details` (`customer_name`,`address`,`phone`) VALUES ("Sawyer Casey","Koekelberg","9264641325"),("Duncan Love","Yellowhead County","9709483508"),("Cullen Holmes","Basildon","5188157897"),("Hop Richard","Bavikhove","1972287566"),("Dorian Hardy","Selkirk","5350697523"),("Vincent Riggs","Rocca San Felice","2883492918"),("Colorado Marquez","Columbus","1204276312"),("Trevor Burks","Colico","4144154320"),("Ryder Owens","Warminster","3805647153"),("Tyler Hampton","Minneapolis","5794807246");
INSERT INTO `customer_details` (`customer_name`,`address`,`phone`) VALUES ("Scott Bird","Grand Falls","9690040913"),("Derek Buckner","Motueka","0357366484"),("Merritt Ferguson","Telfs","7989513956"),("Gabriel Owens","Bègles","8941094566"),("Jackson Vargas","Baie-D'Urfé","5298985930"),("Ian Carson","Saint Andr�","8509396177"),("Seth Estes","Mauá","4479454983"),("Keith Johns","Autelbas","6114517027"),("Craig Mccoy","Rio nell'Elba","6263841491"),("Elmo Randall","Saint-Malo","9169442266");
INSERT INTO `customer_details` (`customer_name`,`address`,`phone`) VALUES ("Brendan Williamson","Vilcún","3819472614"),("Aladdin Douglas","Vanier","9838711676"),("Cadman Bauer","Ofena","5021018270"),("Steven Galloway","Boo","5970408584"),("Dexter Bowen","Driekapellen","3109517026"),("Carlos Harris","Bilbo","7784039081"),("Preston Short","Buzenol","0699317803"),("Zane Wilkins","Surrey","2857145418"),("Dennis Carver","Stamford","1918450821"),("Owen Allison","PiŽtrebais","1808439174");
INSERT INTO `customer_details` (`customer_name`,`address`,`phone`) VALUES ("Demetrius Baird","Sunshine Coast Regional District","6289912405"),("Hoyt Bolton","Allumiere","6015905916"),("Drew Johnson","Baltasound","0541436999"),("Seth Keller","Rimouski","0476445255"),("Rahim Cruz","La Reina","1039416037"),("Xenos Turner","Moffat","4042142892"),("Bevis Franco","Beersel","0929039938"),("Guy Landry","New Maryland","4852974062"),("Bruce Duran","Sete Lagoas","1211477357"),("Maxwell Callahan","Gary","7458687897");
INSERT INTO `customer_details` (`customer_name`,`address`,`phone`) VALUES ("Nicholas Donaldson","Forge-Philippe","9274718191"),("Beau Russell","Gudivada","1462869498"),("Barrett Wallace","Brodick","1187496775"),("Branden Irwin","Stornaway","9279958343"),("Allen Franco","Neudörfl","1367076172"),("Ciaran Boyd","San Chirico Nuovo","1806044848"),("Warren Reid","Sant'Arsenio","2339970276"),("Stephen Leach","Tavier","6496580597"),("Abel Mendez","Houffalize","6019623489"),("Odysseus Blake","Bridgeport","5568231703");
INSERT INTO `customer_details` (`customer_name`,`address`,`phone`) VALUES ("Malachi Hamilton","Bionaz","0506959660"),("Brennan Norris","Lauro de Freitas","4958503440"),("Barclay Stanton","Pace del Mela","5650778012"),("Stone Cardenas","Schulen","4451791254"),("Lane Bennett","Glendon","3919124273"),("Jerry Goodwin","Orai","9386477272"),("Ross Walsh","Paulatuk","2267557114"),("Abbot Mathis","Mission","3099793190"),("Gray Curry","St. David's","7325881223"),("Neville Larson","Dehradun","9926204372");
INSERT INTO `customer_details` (`customer_name`,`address`,`phone`) VALUES ("Devin Roth","Tiruvarur","8000591799"),("Simon Brady","Melle","7057423658"),("Phillip Howell","Kaneohe","9261773773"),("Clarke Sargent","Piovene Rocchette","8052726837"),("Garth Anthony","Rocca Massima","3836394211"),("Davis Figueroa","Ongole","8506745841"),("Coby Gilmore","Purnea","5500068127"),("Thor Cherry","Launceston","6451819121"),("Axel Guerrero","Newton Stewart","6105174507"),("Rooney Lopez","Piringen","1216587452");
INSERT INTO `customer_details` (`customer_name`,`address`,`phone`) VALUES ("Brock Mitchell","Latronico","5454767364"),("Flynn Reilly","Palanzano","5436247572"),("Gage Beard","Orai","9097596860"),("Tad Hancock","Paradise","4830759117"),("Leonard Barry","Koersel","6261504725"),("Burton Joyce","Gosselies","6548330382"),("Mufutau Bryant","Pointe-du-Lac","8886781290"),("Ahmed Warren","Hafizabad","2949290362"),("Adrian Booker","Bournemouth","0227408371"),("Jeremy Rice","Wieze","9418970989");
INSERT INTO `customer_details` (`customer_name`,`address`,`phone`) VALUES ("Finn Waller","New Orleans","6094906141"),("Warren Jarvis","Emines","0883853085"),("Oliver Hutchinson","Gibsons","8234058579"),("Ira Bender","Alajuelita","9222166529"),("Brandon Salazar","North Dum Dum","7947221875"),("Finn Lynch","Henstedt-Ulzburg","0990560345"),("Fuller Carr","Hertford","6751549386"),("Ian Haley","Meeuwen-Gruitrode","7644764185"),("Warren Mathews","Viña del Mar","5807642849"),("Chadwick Kennedy","Varna/Vahrn","1859550875");
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


select (case when cab_id = "" then 'NA' else cab_id end) as cab_id from cab_status where c_status = 'R' ORDER BY update_timestamp limit 1;



select  coalesce(cab_id,"NA") as cab_id from cab_status where c_status = 'R' ORDER BY update_timestamp limit 1;

insert into travel_cab_db.cab_status values("cab-4","R",
(select update_timestamp from travel_cab_db.cab_status where cab_id = "cab-4" order by update_timestamp desc limit 1),
now());




 
 update travel_cab_db.cab_status set c_status = "F" ,
 update_timestamp = now() where cab_id = "cab-2";

insert into cab_status(cab_id,c_status,create_timestamp,update_timestamp) values();


create table cabs_fair(
cab_id varchar(45) not null,
customer_id INT not NULL,
pickup_loc varchar(45) not NULL,
drop_loc varchar(45) not null,
date_of_booking DATETIME not NULL,
no_of_km float not NULL,
price float not null,
foreign key(cab_id) references cab_details(cab_id),
foreign key(customer_id) references customer_details(customer_id)
);


insert into cabs_fair(cab_id,customer_id,pickup_loc,drop_loc,date_of_booking,no_of_km,price) VALUES('%s','%s','%s','%s',now(),'%s','%s');




desc cabs_fair;

SELECT * from customer_details;




select cab_id,customer_id,price from cabs_fair where cab_id = "cab-2" GROUP BY cab_id,customer_id,price ORDER BY cab_id ;





alter table cab_status
add COLUMN current_location VARCHAR(45) not null DEFAULT "A";

alter TABLE cab_status
drop COLUMN create_timestamp;
alter TABLE cab_status
drop COLUMN update_timestamp;

alter table cab_status
add COLUMN create_timestamp DATETIME not null DEFAULT NOW(),
add COLUMN update_timestamp DATETIME not null DEFAULT NOW();


select cab_id from travel_cab_db.cab_status where c_status = "F" and current_location = "A" ORDER BY update_timestamp desc limit 1;

show tables;

CREATE table customer_details(
customer_id INT PRIMARY key AUTO_INCREMENT,
customer_name VARCHAR(45) not null,
address VARCHAR(45) not null,
phone BIGINT not null UNIQUE
);

alter TABLE customer_details
AUTO_INCREMENT = 101;

desc customer_details;



select cd.customer_id,cd.customer_name,cf.cab_id,cf.pickup_loc,cf.drop_loc,cf.date_of_booking,cf.price from
customer_details cd inner JOIN cabs_fair cf on cd.customer_id = cf.customer_id;



select customer_id,customer_name from customer_details WHERE customer_id = 155;

select * from cab_status; 

alter table cab_status
ADD COLUMN booking_status VARCHAR(20) DEFAULT "FREE" not null check(booking_status in ('FREE', "BLOCK"));

create table locations(
location_code VARCHAR(10) PRIMARY key,
location_name VARCHAR(50) not null
);

SELECT count(*) from locations ORDER BY location_code;

SELECT location_code from locations ORDER BY location_code;

select cab_id,current_location from cab_status where c_status = "F";

update travel_cab_db.cab_status set c_status = "F" ,current_location = "J",booking_status = "FREE",
 update_timestamp = now() where cab_id = "cab-4";
 
 desc cab_status;

SELECT cab_id,current_location from cab_status where c_status = 'F' and booking_status = 'FREE';



----------------------------------------------------------------------------------------------------------------------------
select * from cab_status ;
select * from customer_details;
select * from cabs_fair;
SELECT * from locations ORDER BY location_code;
----------------------------------------------------------------------------------------------------------------------------

SELECT cf.cab_id as CAB_ID,cf.customer_id as CUSTOMER_ID,cd.customer_name as CUSTOMER_NAME,loc1.location_name as PICK_UP_LOC,loc2.location_name as DROP_LOC, 
cf.date_of_booking as DATE_OF_BOOKING,cf.no_of_km as TOTAL_DISTANCE,cf.price as TOTAL_FAIR
from cabs_fair cf inner join customer_details cd on cf.customer_id = cd.customer_id inner join locations loc1 on cf.pickup_loc = loc1.location_code
inner join locations loc2 on cf.drop_loc = loc2.location_code ORDER BY cf.cab_id;



SELECT cf.cab_id as CAB_ID,cf.customer_id as CUSTOMER_ID,cd.customer_name as CUSTOMER_NAME,loc1.location_name as PICK_UP_LOC,loc2.location_name as DROP_LOC, 
cf.date_of_booking as DATE_OF_BOOKING,cf.no_of_km as TOTAL_DISTANCE,cf.price as TOTAL_FAIR
from cabs_fair cf inner join customer_details cd on cf.customer_id = cd.customer_id inner join locations loc1 on cf.pickup_loc = loc1.location_code
inner join locations loc2 on cf.drop_loc = loc2.location_code where cf.cab_id = "cab-1" ORDER BY cf.customer_id;






