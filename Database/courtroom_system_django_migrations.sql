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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-04-20 18:38:21.976120'),(2,'auth','0001_initial','2022-04-20 18:38:22.747843'),(3,'admin','0001_initial','2022-04-20 18:38:22.928433'),(4,'admin','0002_logentry_remove_auto_add','2022-04-20 18:38:22.938375'),(5,'admin','0003_logentry_add_action_flag_choices','2022-04-20 18:38:22.947660'),(6,'contenttypes','0002_remove_content_type_name','2022-04-20 18:38:23.073969'),(7,'auth','0002_alter_permission_name_max_length','2022-04-20 18:38:23.153808'),(8,'auth','0003_alter_user_email_max_length','2022-04-20 18:38:23.177828'),(9,'auth','0004_alter_user_username_opts','2022-04-20 18:38:23.193818'),(10,'auth','0005_alter_user_last_login_null','2022-04-20 18:38:23.393472'),(11,'auth','0006_require_contenttypes_0002','2022-04-20 18:38:23.401467'),(12,'auth','0007_alter_validators_add_error_messages','2022-04-20 18:38:23.409464'),(13,'auth','0008_alter_user_username_max_length','2022-04-20 18:38:23.528259'),(14,'auth','0009_alter_user_last_name_max_length','2022-04-20 18:38:23.603604'),(15,'auth','0010_alter_group_name_max_length','2022-04-20 18:38:23.628496'),(16,'auth','0011_update_proxy_permissions','2022-04-20 18:38:23.637666'),(17,'auth','0012_alter_user_first_name_max_length','2022-04-20 18:38:23.701472'),(18,'dashboard','0001_initial','2022-04-20 18:38:24.755966'),(19,'sessions','0001_initial','2022-04-20 18:38:24.795946'),(20,'dashboard','0002_remove_client_dependent_id_remove_lawyer_domain_id_and_more','2022-04-20 19:04:19.718872'),(21,'dashboard','0003_alter_case_defenselawyeremail_and_more','2022-04-20 20:18:08.462779'),(22,'dashboard','0004_remove_case_judgeid_case_judgeemail','2022-04-23 22:59:03.384617'),(23,'dashboard','0005_alter_case_judgeemail_alter_case_verdict','2022-04-25 09:29:15.747544'),(24,'dashboard','0006_case_defenseclientemail_case_prosecutorclientemail','2022-04-25 11:18:19.336540'),(25,'dashboard','0007_remove_evidence_judgeemail','2022-04-26 16:18:04.783740');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-04-26 22:32:09
