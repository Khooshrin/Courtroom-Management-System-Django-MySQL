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
-- Table structure for table `dashboard_lawyer`
--

DROP TABLE IF EXISTS `dashboard_lawyer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dashboard_lawyer` (
  `Name` varchar(45) NOT NULL,
  `Email` varchar(254) NOT NULL,
  `ContactNo` int NOT NULL,
  `WorkExperience` int NOT NULL,
  `SuccessRate` int NOT NULL,
  `Password` varchar(20) NOT NULL,
  PRIMARY KEY (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboard_lawyer`
--

LOCK TABLES `dashboard_lawyer` WRITE;
/*!40000 ALTER TABLE `dashboard_lawyer` DISABLE KEYS */;
INSERT INTO `dashboard_lawyer` VALUES ('Kavya','kavs@hotmail.com',478792435,10,87,'ilovekhoo'),('Khooshrin','khooshrin2@gmail.com',787889894,13,92,'ilovekav'),('Lahari','lali12@gmail.com',343546547,15,89,'ilovek'),('Pepper Stark','pepper@hotmail.com',987865657,23,87,'starkpepper'),('Peter Parker','peterp@hotmail.com',686787987,8,83,'parkerp'),('Morningstar','starm4@yahoo.com',999955552,17,71,'starmorning'),('Stephen Strange','stephen@gmail.com',252343566,11,90,'strangesteph'),('Tom Holland','tomh5@gmail.com',575643545,12,91,'tomhol6'),('Tony Stark','tony@hotmail.com',645756456,16,95,'starktony');
/*!40000 ALTER TABLE `dashboard_lawyer` ENABLE KEYS */;
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
