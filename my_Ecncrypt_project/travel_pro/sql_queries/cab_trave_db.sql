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


select cab_id from travel_cab_db.cab_status where c_status = "F" ORDER BY update_timestamp desc limit 1;



insert into travel_cab_db.cab_status values("cab-4","R",
(select update_timestamp from travel_cab_db.cab_status where cab_id = "cab-4" order by update_timestamp desc limit 1),
now());



update travel_cab_db.cab_status set c_status = "F" ,
 update_timestamp = now() where cab_id = "cab-4";
 
 update travel_cab_db.cab_status set c_status = "F" ,
 update_timestamp = now() where cab_id = "cab-2";

insert into cab_status(cab_id,c_status,create_timestamp,update_timestamp) values();


create table cabs_fair(
cab_id varchar(45),
customer_id varchar(45),
pickup_loc varchar(45),
drop_loc varchar(45),
date_of_booking DATETIME,
no_of_km float,
price float,
foreign key(cab_id) references cab_details(cab_id)
);


insert into cabs_fair(cab_id,customer_id,pickup_loc,drop_loc,date_of_booking,no_of_km,price) VALUES('%s','%s','%s','%s',now(),'%s','%s');




desc cabs_fair;

select * from cabs_fair;

select * from cab_status; 





