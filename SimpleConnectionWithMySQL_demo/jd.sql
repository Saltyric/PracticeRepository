-- MySQL dump 10.17  Distrib 10.3.14-MariaDB, for CYGWIN (x86_64)
--
-- Host: localhost    Database: jing_dong
-- ------------------------------------------------------
-- Server version	8.0.16

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customers` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `address` varchar(60) NOT NULL,
  `tel` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,'老王','山东','13411111111','123'),(3,'老张','广州','13455555555','321'),(4,'老李','深圳','13366666666','456'),(5,'小罗','上海','15645646546','654'),(6,'小宇','北京','1375464654','789'),(7,'小雪','辽宁','61546564654','741'),(8,'小明','福建','1864564645','852'),(9,'小刘','新疆','846464644','621');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  `cate_id` int(10) unsigned NOT NULL,
  `brand_id` int(10) unsigned NOT NULL,
  `price` decimal(10,3) NOT NULL DEFAULT '0.000',
  `is_show` bit(1) NOT NULL DEFAULT b'1',
  `is_saleoff` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`id`),
  KEY `cate_id` (`cate_id`),
  KEY `brand_id` (`brand_id`),
  CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`cate_id`) REFERENCES `goods_cates` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (1,'r510vc 15.6英寸',1,1,3399.000,'','\0'),(2,'y400n 14.0英寸',1,2,4999.000,'','\0'),(3,'g15th 15.6英寸',2,3,8499.000,'','\0'),(4,'x550cc 15.6英寸',1,1,2799.000,'','\0'),(5,'lx240 超极本',3,2,4880.000,'','\0'),(6,'lu330p 15.6超极本',3,2,4299.000,'','\0'),(7,'svp360 15.6英寸触控超极本',3,2,7999.000,'','\0'),(8,'iPadmini 7.9英寸平板电脑',4,4,1998.000,'','\0'),(9,'ideacenter 20英寸一体式电脑',5,1,3380.000,'','\0'),(10,'老王牌电脑',1,5,4999.000,'','\0');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_brands`
--

DROP TABLE IF EXISTS `goods_brands`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_brands` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_brands`
--

LOCK TABLES `goods_brands` WRITE;
/*!40000 ALTER TABLE `goods_brands` DISABLE KEYS */;
INSERT INTO `goods_brands` VALUES (1,'华硕'),(2,'联想'),(3,'雷神'),(4,'苹果'),(5,'laowang'),(8,'外星人'),(9,'惠普'),(10,'微星MSI'),(11,'小米'),(12,'戴尔');
/*!40000 ALTER TABLE `goods_brands` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods_cates`
--

DROP TABLE IF EXISTS `goods_cates`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods_cates` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(40) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods_cates`
--

LOCK TABLES `goods_cates` WRITE;
/*!40000 ALTER TABLE `goods_cates` DISABLE KEYS */;
INSERT INTO `goods_cates` VALUES (1,'笔记本'),(2,'游戏本'),(3,'超极本'),(4,'平板电脑'),(5,'台式'),(8,'路由器'),(9,'交换机'),(10,'网卡');
/*!40000 ALTER TABLE `goods_cates` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `order_detail`
--

DROP TABLE IF EXISTS `order_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `order_detail` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_id` int(10) unsigned NOT NULL,
  `good_id` int(10) unsigned NOT NULL,
  `quantity` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order_detail`
--

LOCK TABLES `order_detail` WRITE;
/*!40000 ALTER TABLE `order_detail` DISABLE KEYS */;
INSERT INTO `order_detail` VALUES (1,10,4,3),(2,11,1,3),(3,12,6,1);
/*!40000 ALTER TABLE `order_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orders`
--

DROP TABLE IF EXISTS `orders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `orders` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `order_date_time` varchar(19) NOT NULL,
  `customer_id` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orders`
--

LOCK TABLES `orders` WRITE;
/*!40000 ALTER TABLE `orders` DISABLE KEYS */;
INSERT INTO `orders` VALUES (6,'2020-07-18 14:22:50',3),(7,'2020-07-18 14:26:58',3),(8,'2020-07-18 14:33:00',3),(9,'2020-07-18 14:34:59',3),(10,'2020-07-18 14:35:24',3),(11,'2020-07-18 15:48:36',3),(12,'2020-07-18 15:49:10',3);
/*!40000 ALTER TABLE `orders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `v_goods_info`
--

DROP TABLE IF EXISTS `v_goods_info`;
/*!50001 DROP VIEW IF EXISTS `v_goods_info`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `v_goods_info` (
  `id` tinyint NOT NULL,
  `name` tinyint NOT NULL,
  `cate_id` tinyint NOT NULL,
  `brand_id` tinyint NOT NULL,
  `price` tinyint NOT NULL,
  `is_show` tinyint NOT NULL,
  `is_saleoff` tinyint NOT NULL,
  `cate_name` tinyint NOT NULL,
  `brand_name` tinyint NOT NULL
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `v_goods_info`
--

/*!50001 DROP TABLE IF EXISTS `v_goods_info`*/;
/*!50001 DROP VIEW IF EXISTS `v_goods_info`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `v_goods_info` AS select `g`.`id` AS `id`,`g`.`name` AS `name`,`g`.`cate_id` AS `cate_id`,`g`.`brand_id` AS `brand_id`,`g`.`price` AS `price`,`g`.`is_show` AS `is_show`,`g`.`is_saleoff` AS `is_saleoff`,`c`.`name` AS `cate_name`,`b`.`name` AS `brand_name` from ((`goods` `g` left join `goods_cates` `c` on((`g`.`cate_id` = `c`.`id`))) left join `goods_brands` `b` on((`g`.`brand_id` = `b`.`id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-07-20 17:52:08
