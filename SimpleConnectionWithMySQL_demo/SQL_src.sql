-- CREATE DATABASE test CHARSET=utf8;

use test;

CREATE TABLE if not exists goods(
	id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
    name VARCHAR(150) NOT NULL,
    cate_id	 VARCHAR(40) NOT NULL,
    brand_name VARCHAR(40) NOT NULL,
    price DECIMAL(10,3) NOT NULL DEFAULT 0,
    is_show BIT NOT NULL DEFAULT 1,
    is_saleoff BIT NOT NULL DEFAULT 0
);

create table if not exists orders(
	id int unsigned not null primary key auto_increment,
    order_date_time varchar(19) not null,
    customer_id int unsigned not null
);

create table if not exists customers(
	id int unsigned not null primary key auto_increment,
    name varchar(20) not null,
    address varchar(60) not null,
    tel varchar(20) not null,
    password varchar(20) not null
);

create table if not exists order_detail(
	id int unsigned not null primary key auto_increment,
    order_id int unsigned not null,
    good_id int unsigned not null,
    quantity int unsigned not null
);

INSERT goods VALUES
	(0, 'r510vc 15.6英寸', '笔记本', '华硕', '3399', default, default),
    (0, 'y400n 14.0英寸', '笔记本', '联想', '4999', default, default),
    (0, 'g15th 15.6英寸', '游戏本', '雷神', '8499', default, default),
    (0, 'x550cc 15.6英寸', '笔记本', '华硕', '2799', default, default),
    (0, 'lx240 超极本', '超极本', '联想', '4880', default, default),
    (0, 'lu330p 15.6超极本', '超极本', '联想', '4299', default, default),
    (0, 'svp360 15.6英寸触控超极本', '超极本', '联想', '7999', default, default),
    (0, 'iPadmini 7.9英寸平板电脑', '平板电脑', '苹果', '1998', default, default),
    (0, 'ideacenter 20英寸一体式电脑', '台式', '华硕', '3380', default, default);
insert goods values (0,'老王牌电脑','笔记本', 'laowang', '4999', default, default);

create table if not exists goods_cates(
	id int unsigned not null primary key auto_increment,
    name varchar(40) not null) select cate_id as name from goods group by cate_id;

create table if not exists goods_brands(
	id int unsigned not null primary key auto_increment,
    name varchar(40) not null) select brand_name as name from goods group by brand_name;
    

select * from goods;
select * from goods_brands;
select * from goods_cates;