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
-- Table structure for table `dashboard_case`
--

DROP TABLE IF EXISTS `dashboard_case`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dashboard_case` (
  `CaseID` int NOT NULL,
  `CaseType` varchar(45) NOT NULL,
  `CaseInfo` varchar(45) NOT NULL,
  `Verdict` varchar(45) DEFAULT NULL,
  `DefenseLawyerEmail_id` varchar(254) NOT NULL,
  `ProsecutorLawyerEmail_id` varchar(254) NOT NULL,
  `JudgeEmail_id` varchar(254) DEFAULT NULL,
  `DefenseClientEmail_id` varchar(254) NOT NULL,
  `ProsecutorClientEmail_id` varchar(254) NOT NULL,
  PRIMARY KEY (`CaseID`),
  KEY `dashboard_case_ProsecutorLawyerEmai_24548438_fk_dashboard` (`ProsecutorLawyerEmail_id`),
  KEY `dashboard_case_JudgeEmail_id_16f97604` (`JudgeEmail_id`),
  KEY `dashboard_case_DefenseClientEmail_id_c56882cc` (`DefenseClientEmail_id`),
  KEY `dashboard_case_ProsecutorClientEmail_id_0566a39f` (`ProsecutorClientEmail_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboard_case`
--

LOCK TABLES `dashboard_case` WRITE;
/*!40000 ALTER TABLE `dashboard_case` DISABLE KEYS */;
INSERT INTO `dashboard_case` VALUES (1,'Murder','Found stabbed on RNT','GUILTY','kavs@hotmail.com','khooshrin2@gmail.com','khushii@gmail.com','luc@gmail.com','hemb@gmail.com'),(2,'Theft','Purse was stolen on public transport','FINED','pepper@hotmail.com','peterp@hotmail.com','veedee@hotmail.com','samwilson@gmail.com','maryjane@gmail.com'),(3,'Construction','Building fell due to poor foundation','Compensation granted','stephen@gmail.com','tomh5@gmail.com','jams@gmail.com','christinep@yahoo.com','taylor5@hotmail.com'),(4,'Kidnap','Taken away in a van by masked men','GUILTY','lali12@gmail.com','kavs@hotmail.com','veedee@hotmail.com','bruceb8@yahoo.com','luc@gmail.com'),(5,'Break-in','Broke into house when away','Scott free','khooshrin2@gmail.com','tony@hotmail.com','jams@hotmail.com','hemb@gmail.com','scarjo@hotmail.com'),(6,'Substance Abuse','Drugs were possessed','2 years imprisonment','tomh5@gmail.com','peterp@hotmail.com','khushii@gmail.com','taylor5@hotmail.com','maryjane@gmail.com'),(7,'Murder','Found suffocated in apartment','Not Guilty','lali12@gmail.com','pepper@hotmail.com','khushii@gmail.com','bruceb8@yahoo.com','samwilson@gmail.com'),(8,'Domestic Abuse','Wife was found beaten','GUILTY','tony@hotmail.com','kavs@hotmail.com','veedee@hotmail.com','steverog@gmail.com','luc@gmail.com'),(9,'Wrongful Termination','Fired from job without valid reason','','lali12@gmail.com','starm4@yahoo.com','veedee@hotmail.com','bruceb8@yahoo.com','chloe22@gmail.com'),(11,'Child marriage','Forceful marriage of child below legal age','Lifetime prison','starm4@yahoo.com','tomh5@gmail.com','jams@gmail.com','chloe22@yahoo.com','taylor5@hotmail.com');
/*!40000 ALTER TABLE `dashboard_case` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26 22:33:21
