create table if not exists users (
    EMAIL varchar(50) not null,
    FULLNAME varchar(20) not null,
    BIRTHDAY date not null,
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
    primary key (EVENT_ID, EMAIL)
) DEFAULT CHARSET='utf8';

create table token (
    TOKEN int not null,
    primary key (TOKEN)
) DEFAULT CHARSET='utf8';

create table event_blessings (
    EVENT_ID int not null,
    EMAIL varchar(50) not null,
    MESSAGE varchar(300) not null,
    EDIT_TIME timestamp not null,
    primary key (EVENT_ID, EMAIL)
) DEFAULT CHARSET='utf8';