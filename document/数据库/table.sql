drop index taxi_id_index on taxi_info;

drop table if exists taxi_info;

/*==============================================================*/
/* Table: taxi_info                                             */
/*==============================================================*/
create table taxi_info
(
   id                   int not null auto_increment,
   taxi_id              varchar(10) not null,
   full_load            int not null,
   actual_load          int not null,
   info_date            datetime not null,
   lon                  float not null,
   lat                  float not null,
   attr1                int not null,
   attr2                int not null,
   attr3                int not null,
   primary key (id),
   unique key AK_UNQ_taxi_info_taxi_id_date (taxi_id, info_date)
);

/*==============================================================*/
/* Index: taxi_id_index                                         */
/*==============================================================*/
create index taxi_id_index on taxi_info
(
   taxi_id
);

create table taxi
(
	id                   int not null auto_increment,
	taxi_id              varchar(10) not null,
	primary key(id)
);

insert into taxi (taxi_id) select taxi_id from taxi_info group by(taxi_id);

create table poi_info
(
	id 					int not null auto_increment,
	poi_name 			varchar(50) not null,
	poi_addr 			text not null,
	phone 				varchar(20) not null,
	tel 				varchar(20) not null,
	lon 				float not null,
	lat 				float not null,
	primary key(id)
);

create table poi_type_code
(
	id 					int not null auto_increment,
	poi_type			varchar(50) not null,
	primary key(id)
);
create table poi_type
(
	id 					int not null auto_increment,
	poi_id				int not null,
	poi_type_id			int not null,
	primary key(id)
);
