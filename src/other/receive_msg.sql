create table delivermsg(
id int primary key auto_increment,
delivertime timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP,
phone varchar(255),
content varchar(255),
subcode varchar(255)
) DEFAULT CHARSET=utf8;

create table sendrmsg(
id int primary key auto_increment,
sendtime timestamp NOT NULL ON UPDATE CURRENT_TIMESTAMP,
phone varchar(255),
content varchar(255),
operator varchar(255)
) DEFAULT CHARSET=utf8;