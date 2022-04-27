CREATE DATABASE  IF NOT EXISTS `courtroom_system` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `courtroom_system`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: courtroom_system
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dashboard_client`
--

DROP TABLE IF EXISTS `dashboard_client`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dashboard_client` (
  `Name` varchar(45) NOT NULL,
  `Email` varchar(254) NOT NULL,
  `ContactNo` int NOT NULL,
  `City` varchar(45) NOT NULL,
  `Street` varchar(45) NOT NULL,
  `Pincode` int NOT NULL,
  `Password` varchar(20) NOT NULL,
  `LawyerEmail_id` varchar(254) NOT NULL,
  PRIMARY KEY (`Email`),
  KEY `dashboard_client_LawyerEmail_id_553a6808_fk_dashboard` (`LawyerEmail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboard_client`
--

LOCK TABLES `dashboard_client` WRITE;
/*!40000 ALTER TABLE `dashboard_client` DISABLE KEYS */;
INSERT INTO `dashboard_client` VALUES ('Bruce Banner','bruceb8@yahoo.com',985475867,'London','SQ Road',110001,'brucebanner','lali12@gmail.com'),('Chloe','chloe22@yahoo.com',734736574,'Florida','Heaven Road',924990,'chloe22','starm4@yahoo.com'),('Christine Palmer','christinep@yahoo.com',384283378,'Vegas','Mark Harbour',120005,'palmerchris','stephen@gmail.com'),('Hemangi','hemb@gmail.com',878703232,'Bangalore','JP Street',870021,'hemangidb','khooshrin2@gmail.com'),('Lucas','luc@gmail.com',891357392,'California','Cal Road',900123,'lucas99','kavs@hotmail.com'),('Madhumita','madz@yahoo.com',743841893,'Pune','Laal Chowk',600012,'madhup0','lali12@gmail.com'),('Mary Jane','maryjane@gmail.com',493895965,'New York','Bridgeton Road',122089,'mj1029','peterp@hotmail.com'),('Sam Wilson','samwilson@gmail.com',234657688,'Washington','WC Avenue',233001,'samwilson3','pepper@hotmail.com'),('Scarlett Johan','scarjo@hotmail.com',146788997,'New York','Fight Street',900022,'scarjo66','tony@hotmail.com'),('Steve Rogers','steverog@gmail.com',298385868,'Britain','KL Road',270012,'steverog2','tony@hotmail.com'),('Taylor Swift','taylor5@hotmail.com',845855486,'Texas','Right Avenue',900101,'swift5','tomh5@gmail.com');
/*!40000 ALTER TABLE `dashboard_client` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26 22:33:23
