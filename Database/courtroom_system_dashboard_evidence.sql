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
-- Table structure for table `dashboard_evidence`
--

DROP TABLE IF EXISTS `dashboard_evidence`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dashboard_evidence` (
  `CaseID_id` int NOT NULL,
  `EvidenceInfo` varchar(100) NOT NULL,
  `LawyerEmail_id` varchar(254) NOT NULL,
  PRIMARY KEY (`CaseID_id`),
  UNIQUE KEY `evidence_lawyer_case` (`CaseID_id`,`LawyerEmail_id`),
  KEY `dashboard_evidence_LawyerEmail_id_03f4ef33_fk_dashboard` (`LawyerEmail_id`),
  CONSTRAINT `dashboard_evidence_CaseID_id_6123a5f2_fk_dashboard_case_CaseID` FOREIGN KEY (`CaseID_id`) REFERENCES `dashboard_case` (`CaseID`),
  CONSTRAINT `dashboard_evidence_LawyerEmail_id_03f4ef33_fk_dashboard` FOREIGN KEY (`LawyerEmail_id`) REFERENCES `dashboard_lawyer` (`Email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dashboard_evidence`
--

LOCK TABLES `dashboard_evidence` WRITE;
/*!40000 ALTER TABLE `dashboard_evidence` DISABLE KEYS */;
INSERT INTO `dashboard_evidence` VALUES (9,'No reason for termination','lali12@gmail.com'),(11,'birth certificate proving child is under age','starm4@yahoo.com');
/*!40000 ALTER TABLE `dashboard_evidence` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26 22:32:08
