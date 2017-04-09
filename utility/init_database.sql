use bless;
drop table if exists users;
drop table if exists events;
drop table if exists event_user;
drop table if exists login_token;
drop table if exists event_blessings;

create table users (
    EMAIL varchar(50) not null,
    FULLNAME varchar(20) not null,
    BIRTHDAY date,
    primary key (EMAIL)
) DEFAULT CHARSET='utf8';

create table events (
    ID int not null auto_increment,
    DESCRIPTION varchar(100) not null,
    HAPPEN_DATE date not null,
    primary key (ID)
) DEFAULT CHARSET='utf8';

create table event_user (
    EVENT_ID int not null,
    EMAIL varchar(50) not null,
    EDIT_TIME timestamp not null default current_timestamp,
    primary key (EVENT_ID, EMAIL)
) DEFAULT CHARSET='utf8';

create table login_token (
    TOKEN int not null,
    primary key (TOKEN)
) DEFAULT CHARSET='utf8';

create table event_blessings (
    EVENT_ID int not null,
    EMAIL varchar(50) not null,
    MESSAGE varchar(300) not null,
    EDIT_TIME timestamp not null default current_timestamp,
    primary key (EVENT_ID, EMAIL)
) DEFAULT CHARSET='utf8';

insert into users(EMAIL, FULLNAME) values('admin@bless', '超级管理员');
insert into login_token(TOKEN) values('2013');