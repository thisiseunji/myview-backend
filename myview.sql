-- MySQL dump 10.13  Distrib 8.0.29, for macos12.2 (arm64)
--
-- Host: localhost    Database: myview
-- ------------------------------------------------------
-- Server version	8.0.29

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `actor_jobs`
--

DROP TABLE IF EXISTS `actor_jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actor_jobs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `actor_id` bigint NOT NULL,
  `job_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `actor_jobs_actor_id_17c27854_fk_actors_id` (`actor_id`),
  KEY `actor_jobs_job_id_80982833_fk_jobs_id` (`job_id`),
  CONSTRAINT `actor_jobs_actor_id_17c27854_fk_actors_id` FOREIGN KEY (`actor_id`) REFERENCES `actors` (`id`),
  CONSTRAINT `actor_jobs_job_id_80982833_fk_jobs_id` FOREIGN KEY (`job_id`) REFERENCES `jobs` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actor_jobs`
--

LOCK TABLES `actor_jobs` WRITE;
/*!40000 ALTER TABLE `actor_jobs` DISABLE KEYS */;
INSERT INTO `actor_jobs` VALUES (1,1,1),(2,1,2),(3,2,1),(4,3,1),(5,4,1),(6,5,1),(7,6,1),(8,7,1),(9,8,1),(10,8,2),(11,9,1),(12,9,2),(13,10,1),(14,11,1),(15,12,1);
/*!40000 ALTER TABLE `actor_jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `actors`
--

DROP TABLE IF EXISTS `actors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `actors` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `country_id` bigint NOT NULL,
  `image_id` bigint NOT NULL,
  `birth` date DEFAULT NULL,
  `debut` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `debut_year` int DEFAULT NULL,
  `height` int DEFAULT NULL,
  `weight` int DEFAULT NULL,
  `agency` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `actors_country_id_55fde9d9_fk_countries_id` (`country_id`),
  KEY `actors_image_id_d320d816_fk_images_id` (`image_id`),
  CONSTRAINT `actors_country_id_55fde9d9_fk_countries_id` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`),
  CONSTRAINT `actors_image_id_d320d816_fk_images_id` FOREIGN KEY (`image_id`) REFERENCES `images` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `actors`
--

LOCK TABLES `actors` WRITE;
/*!40000 ALTER TABLE `actors` DISABLE KEYS */;
INSERT INTO `actors` VALUES (1,'마동석',2,13,'1971-03-01','바람의 전설',2004,178,100,'빅펀치이엔티'),(2,'최귀화',2,14,'1978-03-03','피고지고 피고지고',1997,181,72,'미스터초이'),(3,'박지환',2,15,'1980-09-05','짝패',2006,178,72,'저스트엔터테인먼트'),(4,'손석구',2,16,'1983-02-07','블랙스톤',2016,179,80,'샛별당'),(5,'허동원',2,17,'1980-06-09','유쾌한 거래',2007,183,0,'에이스팩토리'),(6,'크리스 에반스',1,18,'1981-06-13','풋내기',2000,183,79,''),(7,'타이카 와이티티',1,19,'1975-08-16','',0,184,0,''),(8,'피터 손',1,20,'1977-01-23','',0,0,0,''),(9,'김무열',2,21,'1982-05-22','사이간',1999,183,71,'프레인TPC'),(10,'김성규',2,22,'1986-01-06','12인',2011,173,0,'사람엔터테인먼트'),(11,'유승목',2,23,'1969-09-14','연극배우',1993,175,69,'SM C&C'),(12,'최민철',2,24,'1976-11-09','팔만대장경',2000,182,0,'빅보스 엔터테인먼트');
/*!40000 ALTER TABLE `actors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=149 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can view permission',1,'view_permission'),(5,'Can add group',2,'add_group'),(6,'Can change group',2,'change_group'),(7,'Can delete group',2,'delete_group'),(8,'Can view group',2,'view_group'),(9,'Can add user',3,'add_user'),(10,'Can change user',3,'change_user'),(11,'Can delete user',3,'delete_user'),(12,'Can view user',3,'view_user'),(13,'Can add content type',4,'add_contenttype'),(14,'Can change content type',4,'change_contenttype'),(15,'Can delete content type',4,'delete_contenttype'),(16,'Can view content type',4,'view_contenttype'),(17,'Can add session',5,'add_session'),(18,'Can change session',5,'change_session'),(19,'Can delete session',5,'delete_session'),(20,'Can view session',5,'view_session'),(21,'Can add collection',6,'add_collection'),(22,'Can change collection',6,'change_collection'),(23,'Can delete collection',6,'delete_collection'),(24,'Can view collection',6,'view_collection'),(25,'Can add group',7,'add_group'),(26,'Can change group',7,'change_group'),(27,'Can delete group',7,'delete_group'),(28,'Can view group',7,'view_group'),(29,'Can add social platform',8,'add_socialplatform'),(30,'Can change social platform',8,'change_socialplatform'),(31,'Can delete social platform',8,'delete_socialplatform'),(32,'Can view social platform',8,'view_socialplatform'),(33,'Can add social token',9,'add_socialtoken'),(34,'Can change social token',9,'change_socialtoken'),(35,'Can delete social token',9,'delete_socialtoken'),(36,'Can view social token',9,'view_socialtoken'),(37,'Can add user',10,'add_user'),(38,'Can change user',10,'change_user'),(39,'Can delete user',10,'delete_user'),(40,'Can view user',10,'view_user'),(41,'Can add profile image',11,'add_profileimage'),(42,'Can change profile image',11,'change_profileimage'),(43,'Can delete profile image',11,'delete_profileimage'),(44,'Can view profile image',11,'view_profileimage'),(45,'Can add collection movie',12,'add_collectionmovie'),(46,'Can change collection movie',12,'change_collectionmovie'),(47,'Can delete collection movie',12,'delete_collectionmovie'),(48,'Can view collection movie',12,'view_collectionmovie'),(49,'Can add actor',13,'add_actor'),(50,'Can change actor',13,'change_actor'),(51,'Can delete actor',13,'delete_actor'),(52,'Can view actor',13,'view_actor'),(53,'Can add category',14,'add_category'),(54,'Can change category',14,'change_category'),(55,'Can delete category',14,'delete_category'),(56,'Can view category',14,'view_category'),(57,'Can add country',15,'add_country'),(58,'Can change country',15,'change_country'),(59,'Can delete country',15,'delete_country'),(60,'Can view country',15,'view_country'),(61,'Can add genre',16,'add_genre'),(62,'Can change genre',16,'change_genre'),(63,'Can delete genre',16,'delete_genre'),(64,'Can view genre',16,'view_genre'),(65,'Can add image',17,'add_image'),(66,'Can change image',17,'change_image'),(67,'Can delete image',17,'delete_image'),(68,'Can view image',17,'view_image'),(69,'Can add movie',18,'add_movie'),(70,'Can change movie',18,'change_movie'),(71,'Can delete movie',18,'delete_movie'),(72,'Can view movie',18,'view_movie'),(73,'Can add platform',19,'add_platform'),(74,'Can change platform',19,'change_platform'),(75,'Can delete platform',19,'delete_platform'),(76,'Can view platform',19,'view_platform'),(77,'Can add role',20,'add_role'),(78,'Can change role',20,'change_role'),(79,'Can delete role',20,'delete_role'),(80,'Can view role',20,'view_role'),(81,'Can add video',21,'add_video'),(82,'Can change video',21,'change_video'),(83,'Can delete video',21,'delete_video'),(84,'Can view video',21,'view_video'),(85,'Can add thumbnail image',22,'add_thumbnailimage'),(86,'Can change thumbnail image',22,'change_thumbnailimage'),(87,'Can delete thumbnail image',22,'delete_thumbnailimage'),(88,'Can view thumbnail image',22,'view_thumbnailimage'),(89,'Can add movie video',23,'add_movievideo'),(90,'Can change movie video',23,'change_movievideo'),(91,'Can delete movie video',23,'delete_movievideo'),(92,'Can view movie video',23,'view_movievideo'),(93,'Can add movie platform',24,'add_movieplatform'),(94,'Can change movie platform',24,'change_movieplatform'),(95,'Can delete movie platform',24,'delete_movieplatform'),(96,'Can view movie platform',24,'view_movieplatform'),(97,'Can add movie image',25,'add_movieimage'),(98,'Can change movie image',25,'change_movieimage'),(99,'Can delete movie image',25,'delete_movieimage'),(100,'Can view movie image',25,'view_movieimage'),(101,'Can add movie genre',26,'add_moviegenre'),(102,'Can change movie genre',26,'change_moviegenre'),(103,'Can delete movie genre',26,'delete_moviegenre'),(104,'Can view movie genre',26,'view_moviegenre'),(105,'Can add movie actor',27,'add_movieactor'),(106,'Can change movie actor',27,'change_movieactor'),(107,'Can delete movie actor',27,'delete_movieactor'),(108,'Can view movie actor',27,'view_movieactor'),(109,'Can add job',28,'add_job'),(110,'Can change job',28,'change_job'),(111,'Can delete job',28,'delete_job'),(112,'Can view job',28,'view_job'),(113,'Can add actor job',29,'add_actorjob'),(114,'Can change actor job',29,'change_actorjob'),(115,'Can delete actor job',29,'delete_actorjob'),(116,'Can view actor job',29,'view_actorjob'),(117,'Can add color code',30,'add_colorcode'),(118,'Can change color code',30,'change_colorcode'),(119,'Can delete color code',30,'delete_colorcode'),(120,'Can view color code',30,'view_colorcode'),(121,'Can add place',31,'add_place'),(122,'Can change place',31,'change_place'),(123,'Can delete place',31,'delete_place'),(124,'Can view place',31,'view_place'),(125,'Can add review',32,'add_review'),(126,'Can change review',32,'change_review'),(127,'Can delete review',32,'delete_review'),(128,'Can view review',32,'view_review'),(129,'Can add tag',33,'add_tag'),(130,'Can change tag',33,'change_tag'),(131,'Can delete tag',33,'delete_tag'),(132,'Can view tag',33,'view_tag'),(133,'Can add review user',34,'add_reviewuser'),(134,'Can change review user',34,'change_reviewuser'),(135,'Can delete review user',34,'delete_reviewuser'),(136,'Can view review user',34,'view_reviewuser'),(137,'Can add review place',35,'add_reviewplace'),(138,'Can change review place',35,'change_reviewplace'),(139,'Can delete review place',35,'delete_reviewplace'),(140,'Can view review place',35,'view_reviewplace'),(141,'Can add review tag',36,'add_reviewtag'),(142,'Can change review tag',36,'change_reviewtag'),(143,'Can delete review tag',36,'delete_reviewtag'),(144,'Can view review tag',36,'view_reviewtag'),(145,'Can add review image',37,'add_reviewimage'),(146,'Can change review image',37,'change_reviewimage'),(147,'Can delete review image',37,'delete_reviewimage'),(148,'Can view review image',37,'view_reviewimage');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) COLLATE utf8mb4_general_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `first_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(254) COLLATE utf8mb4_general_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES (1,'movie'),(2,'drama');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collection_movies`
--

DROP TABLE IF EXISTS `collection_movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collection_movies` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `collection_id` bigint NOT NULL,
  `movie_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `collection_movies_collection_id_e62f909e_fk_collections_id` (`collection_id`),
  KEY `collection_movies_movie_id_1bd1ed0d_fk_movies_id` (`movie_id`),
  CONSTRAINT `collection_movies_collection_id_e62f909e_fk_collections_id` FOREIGN KEY (`collection_id`) REFERENCES `collections` (`id`),
  CONSTRAINT `collection_movies_movie_id_1bd1ed0d_fk_movies_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collection_movies`
--

LOCK TABLES `collection_movies` WRITE;
/*!40000 ALTER TABLE `collection_movies` DISABLE KEYS */;
INSERT INTO `collection_movies` VALUES (1,1,1),(2,1,2),(3,2,1);
/*!40000 ALTER TABLE `collection_movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `collections`
--

DROP TABLE IF EXISTS `collections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `collections` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `name` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `collections_user_id_155c6d5e_fk_users_id` (`user_id`),
  CONSTRAINT `collections_user_id_155c6d5e_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `collections`
--

LOCK TABLES `collections` WRITE;
/*!40000 ALTER TABLE `collections` DISABLE KEYS */;
INSERT INTO `collections` VALUES (1,'2022-07-08 10:54:54.434860','2022-07-08 10:54:54.434873','나만의 콜렉션',1),(2,'2022-07-08 10:54:54.436645','2022-07-08 10:54:54.436657','연인과 보기',2),(3,'2022-07-08 10:54:54.439083','2022-07-08 10:54:54.439111','가족영화 콜렉션',2);
/*!40000 ALTER TABLE `collections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `color_codes`
--

DROP TABLE IF EXISTS `color_codes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `color_codes` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `color_code` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `color_codes`
--

LOCK TABLES `color_codes` WRITE;
/*!40000 ALTER TABLE `color_codes` DISABLE KEYS */;
INSERT INTO `color_codes` VALUES (1,'#ffffff'),(2,'#ff0000'),(3,'#800000'),(4,'#ffff00');
/*!40000 ALTER TABLE `color_codes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `countries`
--

DROP TABLE IF EXISTS `countries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `countries` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `countries`
--

LOCK TABLES `countries` WRITE;
/*!40000 ALTER TABLE `countries` DISABLE KEYS */;
INSERT INTO `countries` VALUES (1,'미국'),(2,'한국'),(3,'일본'),(4,'중국');
/*!40000 ALTER TABLE `countries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `model` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (2,'auth','group'),(1,'auth','permission'),(3,'auth','user'),(4,'contenttypes','contenttype'),(13,'movies','actor'),(29,'movies','actorjob'),(14,'movies','category'),(15,'movies','country'),(16,'movies','genre'),(17,'movies','image'),(28,'movies','job'),(18,'movies','movie'),(27,'movies','movieactor'),(26,'movies','moviegenre'),(25,'movies','movieimage'),(24,'movies','movieplatform'),(23,'movies','movievideo'),(19,'movies','platform'),(20,'movies','role'),(22,'movies','thumbnailimage'),(21,'movies','video'),(30,'reviews','colorcode'),(31,'reviews','place'),(32,'reviews','review'),(37,'reviews','reviewimage'),(35,'reviews','reviewplace'),(36,'reviews','reviewtag'),(34,'reviews','reviewuser'),(33,'reviews','tag'),(5,'sessions','session'),(6,'users','collection'),(12,'users','collectionmovie'),(7,'users','group'),(11,'users','profileimage'),(8,'users','socialplatform'),(9,'users','socialtoken'),(10,'users','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-07-08 10:53:23.723268'),(2,'contenttypes','0002_remove_content_type_name','2022-07-08 10:53:23.746557'),(3,'auth','0001_initial','2022-07-08 10:53:23.886492'),(4,'auth','0002_alter_permission_name_max_length','2022-07-08 10:53:23.915681'),(5,'auth','0003_alter_user_email_max_length','2022-07-08 10:53:23.927474'),(6,'auth','0004_alter_user_username_opts','2022-07-08 10:53:23.932652'),(7,'auth','0005_alter_user_last_login_null','2022-07-08 10:53:23.950786'),(8,'auth','0006_require_contenttypes_0002','2022-07-08 10:53:23.952586'),(9,'auth','0007_alter_validators_add_error_messages','2022-07-08 10:53:23.958719'),(10,'auth','0008_alter_user_username_max_length','2022-07-08 10:53:23.978230'),(11,'auth','0009_alter_user_last_name_max_length','2022-07-08 10:53:23.994318'),(12,'auth','0010_alter_group_name_max_length','2022-07-08 10:53:24.005427'),(13,'auth','0011_update_proxy_permissions','2022-07-08 10:53:24.010559'),(14,'auth','0012_alter_user_first_name_max_length','2022-07-08 10:53:24.027301'),(15,'movies','0001_initial','2022-07-08 10:53:24.270964'),(16,'movies','0002_alter_thumbnailimage_table','2022-07-08 10:53:24.275923'),(17,'movies','0003_alter_video_video_url','2022-07-08 10:53:24.285026'),(18,'movies','0004_movie_age_movie_en_title_movie_running_time','2022-07-08 10:53:24.321933'),(19,'movies','0005_job_actor_birth_actor_debut_actor_debut_year_and_more','2022-07-08 10:53:24.410460'),(20,'movies','0006_actor_agency','2022-07-08 10:53:24.448621'),(21,'users','0001_initial','2022-07-08 10:53:24.620975'),(22,'reviews','0001_initial','2022-07-08 10:53:24.829884'),(23,'reviews','0002_remove_review_tag_remove_tag_color_code_reviewtag','2022-07-08 10:53:24.938063'),(24,'reviews','0003_rename_imagereview_reviewimage_and_more','2022-07-08 10:53:25.035990'),(25,'reviews','0004_alter_reviewtag_table','2022-07-08 10:53:25.047232'),(26,'reviews','0005_review_with_user_alter_place_link_alter_place_mapx_and_more','2022-07-08 10:53:25.142513'),(27,'sessions','0001_initial','2022-07-08 10:53:25.154153');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8mb4_general_ci NOT NULL,
  `session_data` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `genres`
--

DROP TABLE IF EXISTS `genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `genres` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `genres`
--

LOCK TABLES `genres` WRITE;
/*!40000 ALTER TABLE `genres` DISABLE KEYS */;
INSERT INTO `genres` VALUES (1,'멜로'),(2,'코미디'),(3,'로맨틱 코미디'),(4,'액션'),(5,'서부극'),(6,'갱스터'),(7,'누와르'),(8,'스릴러'),(9,'미스터리'),(10,'모험'),(11,'공포'),(12,'전쟁'),(13,'탐정'),(14,'공상과학'),(15,'판타지');
/*!40000 ALTER TABLE `genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
INSERT INTO `groups` VALUES (1,'manager'),(2,'general');
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `images` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `image_url` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES (1,'2022-07-08 10:54:54.389837','2022-07-08 10:54:54.390012','image/thumbnail/%E1%84%87%E1%85%A5%E1%86%B7%E1%84%8C%E1%85%AC%E1%84%83%E1%85%A9%E1%84%89%E1%85%B52_thumbnail.jpeg'),(2,'2022-07-08 10:54:54.391860','2022-07-08 10:54:54.391874','image/thumbnail/%E1%84%87%E1%85%A5%E1%84%8C%E1%85%B3%E1%84%85%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%90%E1%85%B3%E1%84%8B%E1%85%B5%E1%84%8B%E1%85%A5_thumbnail.jpeg'),(3,'2022-07-08 10:54:54.392415','2022-07-08 10:54:54.392427','image/gallery/2t-e9p_pooN0OuqB5EjNmA.jpeg'),(4,'2022-07-08 10:54:54.392863','2022-07-08 10:54:54.392871','image/gallery/ajkHDQJ4jmU6T5QGUgK3Hw.jpeg'),(5,'2022-07-08 10:54:54.393344','2022-07-08 10:54:54.393352','image/gallery/UwEF-X2__wDZg2WHiFQ7Tg.jpeg'),(6,'2022-07-08 10:54:54.393787','2022-07-08 10:54:54.393795','image/gallery/XvOdKXuyw4ES5L83Y1qvtw.jpeg'),(7,'2022-07-08 10:54:54.394255','2022-07-08 10:54:54.394262','image/gallery/yymKC7-5asM_KEH8oxIdyg.jpeg'),(8,'2022-07-08 10:54:54.394720','2022-07-08 10:54:54.394729','image/gallery/Z8jafJT0TOkoU1C0Z5xo_Q.jpeg'),(9,'2022-07-08 10:54:54.395172','2022-07-08 10:54:54.395180','image/gallery/yymKC7-5asM_KEH8oxIdyg.jpeg'),(10,'2022-07-08 10:54:54.395649','2022-07-08 10:54:54.395656','image/gallery/XvOdKXuyw4ES5L83Y1qvtw.jpeg'),(11,'2022-07-08 10:54:54.396202','2022-07-08 10:54:54.396212','image/gallery/UwEF-X2__wDZg2WHiFQ7Tg.jpeg'),(12,'2022-07-08 10:54:54.396751','2022-07-08 10:54:54.396760','image/gallery/UOcFw-BDSh-yoR0gmc35tQ.jpeg'),(13,'2022-07-08 10:54:54.397313','2022-07-08 10:54:54.397322','image/actor/%E1%84%86%E1%85%A1%E1%84%83%E1%85%A9%E1%86%BC%E1%84%89%E1%85%A5%E1%86%A8.jpeg'),(14,'2022-07-08 10:54:54.397978','2022-07-08 10:54:54.397987','image/actor/%E1%84%87%E1%85%A1%E1%86%A8%E1%84%8C%E1%85%B5%E1%84%92%E1%85%AA%E1%86%AB.jpeg'),(15,'2022-07-08 10:54:54.398678','2022-07-08 10:54:54.398688','image/actor/%E1%84%89%E1%85%A9%E1%86%AB%E1%84%89%E1%85%A5%E1%86%A8%E1%84%80%E1%85%AE.jpeg'),(16,'2022-07-08 10:54:54.399355','2022-07-08 10:54:54.399364','image/actor/%E1%84%8E%E1%85%AC%E1%84%80%E1%85%B1%E1%84%92%E1%85%AA.jpeg'),(17,'2022-07-08 10:54:54.400050','2022-07-08 10:54:54.400059','image/actor/%E1%84%92%E1%85%A5%E1%84%83%E1%85%A9%E1%86%BC%E1%84%8B%E1%85%AF%E1%86%AB.jpeg'),(18,'2022-07-08 10:54:54.400707','2022-07-08 10:54:54.400717','image/actor/%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%84%89%E1%85%B3+%E1%84%8B%E1%85%A6%E1%84%87%E1%85%A1%E1%86%AB%E1%84%89%E1%85%B3.jpg'),(19,'2022-07-08 10:54:54.401535','2022-07-08 10:54:54.401544','image/actor/%E1%84%90%E1%85%A1%E1%84%8B%E1%85%B5%E1%84%8F%E1%85%A1+%E1%84%8B%E1%85%AA%E1%84%8B%E1%85%B5%E1%84%90%E1%85%B5%E1%84%90%E1%85%B5.jpg'),(20,'2022-07-08 10:54:54.402160','2022-07-08 10:54:54.402170','image/actor/%E1%84%91%E1%85%B5%E1%84%90%E1%85%A5+%E1%84%89%E1%85%A9%E1%86%AB.jpg'),(21,'2022-07-08 10:54:54.402867','2022-07-08 10:54:54.402884','image/actor/%E1%84%80%E1%85%B5%E1%86%B7%E1%84%89%E1%85%A5%E1%86%BC%E1%84%80%E1%85%B2.jpeg'),(22,'2022-07-08 10:54:54.403533','2022-07-08 10:54:54.403545','image/actor/%E1%84%8B%E1%85%B2%E1%84%89%E1%85%B3%E1%86%BC%E1%84%86%E1%85%A9%E1%86%A8.jpeg'),(23,'2022-07-08 10:54:54.404524','2022-07-08 10:54:54.404548','image/actor/%E1%84%8E%E1%85%AC%E1%84%86%E1%85%B5%E1%86%AB%E1%84%8E%E1%85%A5%E1%86%AF.jpeg'),(24,'2022-07-08 10:54:54.406579','2022-07-08 10:54:54.406603','image/thumbnail/%E1%84%8B%E1%85%A1%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB.jpeg'),(25,'2022-07-09 18:04:45.975324','2022-07-09 18:04:45.975427','http://k.kakaocdn.net/dn/dpk9l1/btqmGhA2lKL/Oz0wDuJn1YV2DIn92f6DVK/img_640x640.jpg'),(26,'2022-07-09 18:27:35.655790','2022-07-09 18:27:35.655859','http://k.kakaocdn.net/dn/chqBNG/btru7SlhkOG/E9IfM4Bo8mFTam2fqQHChk/img_640x640.jpg'),(27,'2022-07-09 18:51:39.968101','2022-07-09 18:51:39.968195','https://phinf.pstatic.net/contact/20201212_110/16077841546587Wdwu_JPEG/DSC03256.JPG'),(28,'2022-07-09 18:51:42.901040','2022-07-09 18:51:42.901108','https://ssl.pstatic.net/static/pwe/address/img_profile.png');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs`
--

DROP TABLE IF EXISTS `jobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `jobs` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs`
--

LOCK TABLES `jobs` WRITE;
/*!40000 ALTER TABLE `jobs` DISABLE KEYS */;
INSERT INTO `jobs` VALUES (1,'영화배우'),(2,'감독'),(3,'뮤지컬배우'),(4,'연극배우');
/*!40000 ALTER TABLE `jobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_actors`
--

DROP TABLE IF EXISTS `movie_actors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_actors` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `role_name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `actor_id` bigint NOT NULL,
  `movie_id` bigint NOT NULL,
  `role_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_actors_actor_id_19a7fa23_fk_actors_id` (`actor_id`),
  KEY `movie_actors_movie_id_4da92ed2_fk_movies_id` (`movie_id`),
  KEY `movie_actors_role_id_b50b4044_fk_roles_id` (`role_id`),
  CONSTRAINT `movie_actors_actor_id_19a7fa23_fk_actors_id` FOREIGN KEY (`actor_id`) REFERENCES `actors` (`id`),
  CONSTRAINT `movie_actors_movie_id_4da92ed2_fk_movies_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `movie_actors_role_id_b50b4044_fk_roles_id` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_actors`
--

LOCK TABLES `movie_actors` WRITE;
/*!40000 ALTER TABLE `movie_actors` DISABLE KEYS */;
INSERT INTO `movie_actors` VALUES (1,'2022-07-08 10:54:54.551789','2022-07-08 10:54:54.551814','마석도',1,1,1),(2,'2022-07-08 10:54:54.562030','2022-07-08 10:54:54.562063','강해상',2,1,1),(3,'2022-07-08 10:54:54.582392','2022-07-08 10:54:54.582437','전일만',3,1,1),(4,'2022-07-08 10:54:54.586359','2022-07-08 10:54:54.586393','장이수',4,1,2),(5,'2022-07-08 10:54:54.592228','2022-07-08 10:54:54.592260','오동균',5,1,2),(6,'2022-07-08 10:54:54.595150','2022-07-08 10:54:54.595174','버즈 라이트이어',6,2,1),(7,'2022-07-08 10:54:54.597486','2022-07-08 10:54:54.597498','타이카',7,2,1),(8,'2022-07-08 10:54:54.604891','2022-07-08 10:54:54.604908','피터',8,2,1),(9,'2022-07-08 10:54:54.607421','2022-07-08 10:54:54.607434','장동수',1,3,1),(10,'2022-07-08 10:54:54.609787','2022-07-08 10:54:54.609800','정태석',9,3,1),(11,'2022-07-08 10:54:54.612176','2022-07-08 10:54:54.612188','강경호',10,3,1),(12,'2022-07-08 10:54:54.614523','2022-07-08 10:54:54.614536','안호봉',11,3,2),(13,'2022-07-08 10:54:54.616925','2022-07-08 10:54:54.616937','권오성',12,3,2);
/*!40000 ALTER TABLE `movie_actors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_genres`
--

DROP TABLE IF EXISTS `movie_genres`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_genres` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `genre_id` bigint NOT NULL,
  `movie_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_genres_genre_id_3f892aeb_fk_genres_id` (`genre_id`),
  KEY `movie_genres_movie_id_cafd9509_fk_movies_id` (`movie_id`),
  CONSTRAINT `movie_genres_genre_id_3f892aeb_fk_genres_id` FOREIGN KEY (`genre_id`) REFERENCES `genres` (`id`),
  CONSTRAINT `movie_genres_movie_id_cafd9509_fk_movies_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_genres`
--

LOCK TABLES `movie_genres` WRITE;
/*!40000 ALTER TABLE `movie_genres` DISABLE KEYS */;
INSERT INTO `movie_genres` VALUES (1,2,1),(2,4,1),(3,10,2),(4,4,3);
/*!40000 ALTER TABLE `movie_genres` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_images`
--

DROP TABLE IF EXISTS `movie_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_images` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image_id` bigint NOT NULL,
  `movie_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_images_image_id_21f52f39_fk_images_id` (`image_id`),
  KEY `movie_images_movie_id_0a9ee73e_fk_movies_id` (`movie_id`),
  CONSTRAINT `movie_images_image_id_21f52f39_fk_images_id` FOREIGN KEY (`image_id`) REFERENCES `images` (`id`),
  CONSTRAINT `movie_images_movie_id_0a9ee73e_fk_movies_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_images`
--

LOCK TABLES `movie_images` WRITE;
/*!40000 ALTER TABLE `movie_images` DISABLE KEYS */;
INSERT INTO `movie_images` VALUES (1,3,1),(2,4,1),(3,5,1),(4,6,1),(5,7,1),(6,8,2),(7,9,2),(8,10,2),(9,11,2),(10,12,2);
/*!40000 ALTER TABLE `movie_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_platforms`
--

DROP TABLE IF EXISTS `movie_platforms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_platforms` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `movie_id` bigint NOT NULL,
  `platform_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_platforms_movie_id_ce8cb364_fk_movies_id` (`movie_id`),
  KEY `movie_platforms_platform_id_56e30b22_fk_platforms_id` (`platform_id`),
  CONSTRAINT `movie_platforms_movie_id_ce8cb364_fk_movies_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `movie_platforms_platform_id_56e30b22_fk_platforms_id` FOREIGN KEY (`platform_id`) REFERENCES `platforms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_platforms`
--

LOCK TABLES `movie_platforms` WRITE;
/*!40000 ALTER TABLE `movie_platforms` DISABLE KEYS */;
INSERT INTO `movie_platforms` VALUES (1,1,1),(2,2,2),(3,3,1);
/*!40000 ALTER TABLE `movie_platforms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie_videos`
--

DROP TABLE IF EXISTS `movie_videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movie_videos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `movie_id` bigint NOT NULL,
  `video_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_videos_movie_id_f3198014_fk_movies_id` (`movie_id`),
  KEY `movie_videos_video_id_e07c8349_fk_videos_id` (`video_id`),
  CONSTRAINT `movie_videos_movie_id_f3198014_fk_movies_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `movie_videos_video_id_e07c8349_fk_videos_id` FOREIGN KEY (`video_id`) REFERENCES `videos` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie_videos`
--

LOCK TABLES `movie_videos` WRITE;
/*!40000 ALTER TABLE `movie_videos` DISABLE KEYS */;
INSERT INTO `movie_videos` VALUES (1,1,1),(2,1,2),(3,1,3),(4,1,4),(5,1,5),(6,2,6),(7,2,7),(8,2,8),(9,3,1),(10,3,9),(11,3,10),(12,3,11),(13,3,12);
/*!40000 ALTER TABLE `movie_videos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `title` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `description` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `release_date` date NOT NULL,
  `category_id` bigint NOT NULL,
  `country_id` bigint NOT NULL,
  `age` int DEFAULT NULL,
  `en_title` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `running_time` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `movies_category_id_8672f94f_fk_categories_id` (`category_id`),
  KEY `movies_country_id_c840f0f3_fk_countries_id` (`country_id`),
  CONSTRAINT `movies_category_id_8672f94f_fk_categories_id` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `movies_country_id_c840f0f3_fk_countries_id` FOREIGN KEY (`country_id`) REFERENCES `countries` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'2022-07-08 10:54:54.457210','2022-07-08 10:54:54.457241','범죄도시2','“느낌 오지? 이 놈 잡아야 하는 거”\n\n가리봉동 소탕작전 후 4년 뒤, 금천서 강력반은 베트남으로 도주한 용의자를 인도받아 오라는 미션을 받는다. 괴물형사 ‘마석도’(마동석)와 ‘전일만’(최귀화) 반장은 현지 용의자에게서 수상함을 느끼고, 그의 뒤에 무자비한 악행을 벌이는 ‘강해상’(손석구)이 있음을 알게 된다. ‘마석도’와 금천서 강력반은 한국과 베트남을 오가며 역대급 범죄를 저지르는 ‘강해상’을 본격적으로 쫓기 시작하는데...\n\n나쁜 놈들 잡는 데 국경 없다!\n통쾌하고 화끈한 범죄 소탕 작전이 다시 펼쳐진다!','2022-05-30',1,2,15,'The Roundup',106),(2,'2022-07-08 10:54:54.459469','2022-07-08 10:54:54.459483','버즈 라이트이어','우주 저 너머 운명을 건 미션,\n무한한 모험이 시작된다!\n\n미션 #1 \n나, 버즈 라이트이어. 인류 구원에 필요한 자원을 감지하고 현재 수많은 과학자들과 미지의 행성으로 향하고 있다. 이번 미션은 인류의 역사를 새롭게 쓸 것이라 확신한다. \n\n미션 #2\n잘못된 신호였다. 이곳은 삭막하고 거대한 외계 생물만이 살고 있는 폐허의 땅이다. 나의 실수로 모두가 이곳에 고립되고 말았다. 모두를 구하기 위해서 모든 것을 제자리에 돌려 놔야 한다. \n\n미션 #3\n실수를 바로잡기 위한 탈출 미션을 위해 1년의 준비를 마쳤다. 어쩌다 한 팀이 된 정예 부대와 이 미션을 수행할 예정이다. 우주를 집어삼킬 ‘저그 황제’와 대규모 로봇 군사의 위협이 계속되지만 나는 절대 포기할 수 없다. 그런데… 여긴 또 어디지? 시간 속에 갇힌 건가?','2022-06-15',1,1,0,'Lightyear',100),(3,'2022-07-08 10:54:54.460951','2022-07-08 10:54:54.460963','악인전','우연히 연쇄살인마의 표적이 되었다 살아난 조직 보스 장동수와\n 범인잡기에 혈안이 된 강력반 미친개 정태석.\n 타협할 수 없는 두 사람이 연쇄살인마 K를 잡기 위해 손잡는다.\n \n 표적은 하나, 룰도 하나!\n 먼저 잡는 놈이 갖는다!','2019-05-15',1,2,19,'The Gangster, The Cop, The Devil',110);
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `places`
--

DROP TABLE IF EXISTS `places`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `places` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  `mapx` double DEFAULT NULL,
  `mapy` double DEFAULT NULL,
  `link` varchar(500) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `places`
--

LOCK TABLES `places` WRITE;
/*!40000 ALTER TABLE `places` DISABLE KEYS */;
INSERT INTO `places` VALUES (1,'cgv 성신여대점',1,1,'https://www.naver.com'),(2,'롯데시네마 수락점',1,1,'https://www.naver.com'),(3,'메가박스 군자점',1,1,'https://www.naver.com'),(4,'ㅁㄴㅇㄹㄴㅇㄹ',0,0,'url');
/*!40000 ALTER TABLE `places` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `platforms`
--

DROP TABLE IF EXISTS `platforms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `platforms` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `image_url` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `platforms`
--

LOCK TABLES `platforms` WRITE;
/*!40000 ALTER TABLE `platforms` DISABLE KEYS */;
INSERT INTO `platforms` VALUES (1,'넷플릭스','image/platform/Netfilx.png'),(2,'디즈니플러스','image/platform/Disney.png'),(3,'왓챠','image/platform/Whatcha.png'),(4,'티빙','platform/Tving.png');
/*!40000 ALTER TABLE `platforms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `profile_images`
--

DROP TABLE IF EXISTS `profile_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `profile_images` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `image_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `profile_images_image_id_f0fbd11d_fk_images_id` (`image_id`),
  KEY `profile_images_user_id_f5702e2b_fk_users_id` (`user_id`),
  CONSTRAINT `profile_images_image_id_f0fbd11d_fk_images_id` FOREIGN KEY (`image_id`) REFERENCES `images` (`id`),
  CONSTRAINT `profile_images_user_id_f5702e2b_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `profile_images`
--

LOCK TABLES `profile_images` WRITE;
/*!40000 ALTER TABLE `profile_images` DISABLE KEYS */;
INSERT INTO `profile_images` VALUES (1,'2022-07-08 10:54:54.430620','2022-07-08 10:54:54.430635',1,1),(2,'2022-07-08 10:54:54.432852','2022-07-08 10:54:54.432864',2,2),(3,'2022-07-09 18:04:45.983141','2022-07-09 18:04:45.983290',25,11),(4,'2022-07-09 18:27:35.661544','2022-07-09 18:27:35.661636',26,12),(5,'2022-07-09 18:51:39.974961','2022-07-09 18:51:39.975046',27,13),(6,'2022-07-09 18:51:42.902971','2022-07-09 18:51:42.903031',28,14);
/*!40000 ALTER TABLE `profile_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review_images`
--

DROP TABLE IF EXISTS `review_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review_images` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image_id` bigint NOT NULL,
  `review_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `image_reviews_image_id_86867cf2_fk_images_id` (`image_id`),
  KEY `image_reviews_review_id_b99b8970_fk_reviews_id` (`review_id`),
  CONSTRAINT `image_reviews_image_id_86867cf2_fk_images_id` FOREIGN KEY (`image_id`) REFERENCES `images` (`id`),
  CONSTRAINT `image_reviews_review_id_b99b8970_fk_reviews_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review_images`
--

LOCK TABLES `review_images` WRITE;
/*!40000 ALTER TABLE `review_images` DISABLE KEYS */;
INSERT INTO `review_images` VALUES (1,1,1),(2,2,2);
/*!40000 ALTER TABLE `review_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review_places`
--

DROP TABLE IF EXISTS `review_places`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review_places` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `place_id` bigint NOT NULL,
  `review_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `review_places_place_id_64dc766e_fk_places_id` (`place_id`),
  KEY `review_places_review_id_8e20821e_fk_reviews_id` (`review_id`),
  CONSTRAINT `review_places_place_id_64dc766e_fk_places_id` FOREIGN KEY (`place_id`) REFERENCES `places` (`id`),
  CONSTRAINT `review_places_review_id_8e20821e_fk_reviews_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review_places`
--

LOCK TABLES `review_places` WRITE;
/*!40000 ALTER TABLE `review_places` DISABLE KEYS */;
INSERT INTO `review_places` VALUES (1,'2022-07-08 10:54:54.732744','2022-07-08 10:54:54.732760',1,1),(2,'2022-07-08 10:54:54.739082','2022-07-08 10:54:54.739105',2,2),(3,'2022-07-09 19:42:22.543254','2022-07-09 19:42:22.543301',4,13),(8,'2022-07-10 14:17:22.122032','2022-07-10 14:17:22.122097',4,18),(10,'2022-07-10 14:43:19.335299','2022-07-10 14:43:19.335371',4,20);
/*!40000 ALTER TABLE `review_places` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review_tags`
--

DROP TABLE IF EXISTS `review_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review_tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `review_id` bigint NOT NULL,
  `tag_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reviewtags_review_id_340c5e01_fk_reviews_id` (`review_id`),
  KEY `reviewtags_tag_id_5827afa4_fk_tags_id` (`tag_id`),
  CONSTRAINT `reviewtags_review_id_340c5e01_fk_reviews_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`),
  CONSTRAINT `reviewtags_tag_id_5827afa4_fk_tags_id` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review_tags`
--

LOCK TABLES `review_tags` WRITE;
/*!40000 ALTER TABLE `review_tags` DISABLE KEYS */;
INSERT INTO `review_tags` VALUES (1,1,1),(2,2,2);
/*!40000 ALTER TABLE `review_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `review_users`
--

DROP TABLE IF EXISTS `review_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `review_users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `review_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `review_users_review_id_3f9f39d3_fk_reviews_id` (`review_id`),
  KEY `review_users_user_id_83062004_fk_users_id` (`user_id`),
  CONSTRAINT `review_users_review_id_3f9f39d3_fk_reviews_id` FOREIGN KEY (`review_id`) REFERENCES `reviews` (`id`),
  CONSTRAINT `review_users_user_id_83062004_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `review_users`
--

LOCK TABLES `review_users` WRITE;
/*!40000 ALTER TABLE `review_users` DISABLE KEYS */;
INSERT INTO `review_users` VALUES (1,'2022-07-08 10:54:54.745964','2022-07-08 10:54:54.745983',1,1),(2,'2022-07-08 10:54:54.748429','2022-07-08 10:54:54.748441',2,2);
/*!40000 ALTER TABLE `review_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `title` varchar(100) COLLATE utf8mb4_general_ci NOT NULL,
  `content` longtext COLLATE utf8mb4_general_ci NOT NULL,
  `rating` decimal(2,1) NOT NULL,
  `watched_date` date DEFAULT NULL,
  `watched_time` time(6) DEFAULT NULL,
  `movie_id` bigint NOT NULL,
  `user_id` bigint NOT NULL,
  `with_user` varchar(30) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reviews_user_id_c23b0903_fk_users_id` (`user_id`),
  KEY `reviews_movie_id_838b3811_fk_movies_id` (`movie_id`),
  CONSTRAINT `reviews_movie_id_838b3811_fk_movies_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `reviews_user_id_c23b0903_fk_users_id` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES (1,'2022-07-08 10:54:54.697375','2022-07-08 10:54:54.697400','자.. 흥행의 방으로!','\"이유가 어딨어. 그냥 잡는거야\"\n이 대사처럼 단순하지만 명쾌하고 시원시원하다.\n\"동석이형 보는데 이유가 어딨어. 그냥 즐기는거야. 자 그럼 흥행의 방으로~\".',4.5,'2022-03-05','14:00:00.000000',1,5,'나홀로'),(2,'2022-07-08 10:54:54.700728','2022-07-08 10:54:54.700742','스토리는.. 빈약하지만...','스토리가 좀 빈약하면 어떠한가 자고로 오락 영화라고 하면 이런 통쾌한 카타르시스가 느껴져야 볼 맛이나는 법이지..\n복잡한 설정, 설명 이딴거 다 집어치우고 오로지 직진만 하는.. 그래서 지루 할 틈이 없는 영화.\n\n<이터널스>의 초능력을 그대로 옮겨온 것 같은 마동석의 타격감 넘치는 액션은 이 영화 최고의 볼거리.\n\n전편의 빌런 장첸이 독사 였다면, 손석구가 연기한 강해상은 마치 호랑이 같았다.\n전성기 시절 아사노 타다노부의 모습에 야성미까지 더한 매력..ㄷㄷㄷ;;\n왜 손석구, 손석구.. 하는지 이제야 좀 알 듯..\n(종종 등장하는 손석구의 어이없어 하는 표정이 은근 중독적..ㅎ)\n\n#후속편에서는 장첸과 강해상이 함께 마동석에게 리벤지 하기를 기대하며..ㅋ',4.0,'2022-03-07','16:00:00.000000',1,7,'여자친구'),(3,'2022-07-08 10:54:54.706211','2022-07-08 10:54:54.706235','웰메이드 오락영화!','극장에서 너무 오랜만에 보는 웰메이드 한국형 오락영화!! 그저 반갑고 재밌게 봤다. 관객 분위기도 좋고 코시국 이전으로 돌아간 느낌..\n❤️ 흥행 대박 기원합니다 ❤️',3.5,'2022-03-10','21:30:00.000000',1,8,'남자친구'),(4,'2022-07-08 10:54:54.708668','2022-07-08 10:54:54.708681','재미나는군!','옆자리 아주머니도 손뼉 치게 만드는, 뒷자리 아저씨도 흥분하게 만드는 그런 영화, 다들 웃음이 끊기지 않는 그런 영화였다.\n\n유난히도 그 소음들이 정겹게 느껴졌다.\n\n얼마나 오랜만에 이런 영화였나 싶다.',4.5,'2022-04-08','17:40:00.000000',1,1,'동료들과'),(5,'2022-07-08 10:54:54.710735','2022-07-08 10:54:54.710747','자.. 흥행의 방으로!','\"이유가 어딨어. 그냥 잡는거야\"\n이 대사처럼 단순하지만 명쾌하고 시원시원하다.\n\"동석이형 보는데 이유가 어딨어. 그냥 즐기는거야. 자 그럼 흥행의 방으로~\".',4.5,'2022-03-05','14:00:00.000000',2,5,'나홀로'),(6,'2022-07-08 10:54:54.712757','2022-07-08 10:54:54.712769','스토리는.. 빈약하지만...','스토리가 좀 빈약하면 어떠한가 자고로 오락 영화라고 하면 이런 통쾌한 카타르시스가 느껴져야 볼 맛이나는 법이지..\n복잡한 설정, 설명 이딴거 다 집어치우고 오로지 직진만 하는.. 그래서 지루 할 틈이 없는 영화.\n\n<이터널스>의 초능력을 그대로 옮겨온 것 같은 마동석의 타격감 넘치는 액션은 이 영화 최고의 볼거리.\n\n전편의 빌런 장첸이 독사 였다면, 손석구가 연기한 강해상은 마치 호랑이 같았다.\n전성기 시절 아사노 타다노부의 모습에 야성미까지 더한 매력..ㄷㄷㄷ;;\n왜 손석구, 손석구.. 하는지 이제야 좀 알 듯..\n(종종 등장하는 손석구의 어이없어 하는 표정이 은근 중독적..ㅎ)\n\n#후속편에서는 장첸과 강해상이 함께 마동석에게 리벤지 하기를 기대하며..ㅋ',4.0,'2022-03-07','16:00:00.000000',2,7,'여자친구'),(7,'2022-07-08 10:54:54.714733','2022-07-08 10:54:54.714744','웰메이드 오락영화!','극장에서 너무 오랜만에 보는 웰메이드 한국형 오락영화!! 그저 반갑고 재밌게 봤다. 관객 분위기도 좋고 코시국 이전으로 돌아간 느낌..\n❤️ 흥행 대박 기원합니다 ❤️',3.5,'2022-03-10','21:30:00.000000',2,8,'남자친구'),(8,'2022-07-08 10:54:54.716821','2022-07-08 10:54:54.716832','재미나는군!','옆자리 아주머니도 손뼉 치게 만드는, 뒷자리 아저씨도 흥분하게 만드는 그런 영화, 다들 웃음이 끊기지 않는 그런 영화였다.\n\n유난히도 그 소음들이 정겹게 느껴졌다.\n\n얼마나 오랜만에 이런 영화였나 싶다.',4.5,'2022-04-08','17:40:00.000000',2,3,'동료들과'),(9,'2022-07-08 10:54:54.718950','2022-07-08 10:54:54.718963','자.. 흥행의 방으로!','\"이유가 어딨어. 그냥 잡는거야\"\n이 대사처럼 단순하지만 명쾌하고 시원시원하다.\n\"동석이형 보는데 이유가 어딨어. 그냥 즐기는거야. 자 그럼 흥행의 방으로~\".',4.5,'2022-03-05','14:00:00.000000',3,5,'나홀로'),(10,'2022-07-08 10:54:54.722622','2022-07-08 10:54:54.722652','스토리는.. 빈약하지만...','스토리가 좀 빈약하면 어떠한가 자고로 오락 영화라고 하면 이런 통쾌한 카타르시스가 느껴져야 볼 맛이나는 법이지..\n복잡한 설정, 설명 이딴거 다 집어치우고 오로지 직진만 하는.. 그래서 지루 할 틈이 없는 영화.\n\n<이터널스>의 초능력을 그대로 옮겨온 것 같은 마동석의 타격감 넘치는 액션은 이 영화 최고의 볼거리.\n\n전편의 빌런 장첸이 독사 였다면, 손석구가 연기한 강해상은 마치 호랑이 같았다.\n전성기 시절 아사노 타다노부의 모습에 야성미까지 더한 매력..ㄷㄷㄷ;;\n왜 손석구, 손석구.. 하는지 이제야 좀 알 듯..\n(종종 등장하는 손석구의 어이없어 하는 표정이 은근 중독적..ㅎ)\n\n#후속편에서는 장첸과 강해상이 함께 마동석에게 리벤지 하기를 기대하며..ㅋ',4.0,'2022-03-07','16:00:00.000000',3,7,'여자친구'),(11,'2022-07-08 10:54:54.725397','2022-07-08 10:54:54.725410','웰메이드 오락영화!','극장에서 너무 오랜만에 보는 웰메이드 한국형 오락영화!! 그저 반갑고 재밌게 봤다. 관객 분위기도 좋고 코시국 이전으로 돌아간 느낌..\n❤️ 흥행 대박 기원합니다 ❤️',3.5,'2022-03-10','21:30:00.000000',3,7,'남자친구'),(12,'2022-07-08 10:54:54.727513','2022-07-08 10:54:54.727524','재미나는군!','옆자리 아주머니도 손뼉 치게 만드는, 뒷자리 아저씨도 흥분하게 만드는 그런 영화, 다들 웃음이 끊기지 않는 그런 영화였다.\n\n유난히도 그 소음들이 정겹게 느껴졌다.\n\n얼마나 오랜만에 이런 영화였나 싶다.',4.5,'2022-04-08','17:40:00.000000',3,2,'동료들과'),(13,'2022-07-09 19:42:22.495500','2022-07-09 19:42:22.495566','한줄평','dksaksdg',2.5,'2022-07-10','04:42:02.000000',3,14,'sdssd'),(18,'2022-07-10 14:17:22.093971','2022-07-10 14:17:22.094054','한줄평','새로운 리뷰',3.0,'2022-07-10','23:16:07.000000',1,12,'ㅇㅇ'),(20,'2022-07-10 14:43:19.307242','2022-07-10 14:43:19.307333','한줄평','ㅁㄹㄴㅇㄹ',3.5,'2022-07-10','23:43:09.000000',2,13,'ㅁㄴㅇㄹㄴㅁㅇㄹ');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `roles` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
INSERT INTO `roles` VALUES (1,'주연'),(2,'조연'),(3,'까메오');
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_platforms`
--

DROP TABLE IF EXISTS `social_platforms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_platforms` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_platforms`
--

LOCK TABLES `social_platforms` WRITE;
/*!40000 ALTER TABLE `social_platforms` DISABLE KEYS */;
INSERT INTO `social_platforms` VALUES (1,'google'),(2,'kakao'),(3,'naver'),(4,'github');
/*!40000 ALTER TABLE `social_platforms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `social_tokens`
--

DROP TABLE IF EXISTS `social_tokens`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `social_tokens` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `access_token` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `refresh_token` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `token_type` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `expires_in` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `social_tokens`
--

LOCK TABLES `social_tokens` WRITE;
/*!40000 ALTER TABLE `social_tokens` DISABLE KEYS */;
INSERT INTO `social_tokens` VALUES (1,'2022-07-09 18:04:45.885723','2022-07-09 18:04:45.885823','l-55tC-zzQ-Kg6_Tkn3uukIIvIEQua4Vfcx_51BbCj1zTQAAAYHkIqj9','AskUUT1cY_O1VsiGsP0f6LIMbnzVTYSEpEKINQcXCj1zTQAAAYHkIqj7','bearer','5183999'),(2,'2022-07-09 18:11:19.084669','2022-07-09 18:11:19.084849','ZSI0-mroEh5ddH6l7QxxoUxdkYDUnEsZSno-HOppCj11WwAAAYHkKKjb','dbEcXHSg-XNTg5qbSyiMfTjaYP_i-DW-pJ_r7pFNCj11WwAAAYHkKKja','bearer','5183999'),(3,'2022-07-09 18:27:35.609720','2022-07-09 18:27:35.610088','qQEbi9iiZqfct-YQIQJECtYlUs3_J_NUQ8Y69tCQCisMpgAAAYHkN46r','sjYfAqXUdlJ47qIGshgp0jcIcJ4FlRGEGrNd9l7ACisMpgAAAYHkN46q','bearer','5183999'),(4,'2022-07-09 18:31:42.588527','2022-07-09 18:31:42.588604','FjL9B7a_qcSDflW0nZRnKfI23iQrr9-G0OU4KfvBCj102QAAAYHkO1QU','_QZmzDdd7NqiqfEGt2KD_TFDROlRq6MtIBZfR1OpCj102QAAAYHkO1QT','bearer','5183999'),(5,'2022-07-09 18:41:08.082518','2022-07-09 18:41:08.085683','_Vg0MKBDYS3MmuYEk8xabso6APg6MtM17lpg7fPPCilwnwAAAYHkQ_Pm','izpZgdqejVx3qddQQRdweKTQRWWKgh3i1dUMjVzvCilwnwAAAYHkQ_Pk','bearer','5183999'),(6,'2022-07-09 20:01:43.778930','2022-07-09 20:01:43.778980','vhHGlgd88_T3lq-Jvr36s1FVRSx_fxQ7tYdKQ_GjCj1zGAAAAYHkjb5V','XqfV0aojNBlkV_w1ND69gPftkWiLgq6dxcGGhJp3Cj1zGAAAAYHkjb5T','bearer','5183999'),(7,'2022-07-09 20:24:05.222730','2022-07-09 20:24:05.222763','u0j2Ooiif0IqLUWKD2u92-YhpLHfjoDDwRcx_X4SCilwngAAAYHkojZj','JXPtnvBoojL2Dxq3JpVsDvpLzCm8CFZjy2ykkCCACilwngAAAYHkojZi','bearer','5183999'),(8,'2022-07-10 11:47:41.224335','2022-07-10 11:47:41.225062','S2iDU2uIY-I5iF1yBs4Ves9GUfJ9uf-FnS1Gdr-fCilvuAAAAYHn78q_','bDCwrdAGlFJ7Vd-VRXObXJRVs4B4Zdi6J43rUi0DCilvuAAAAYHn78q-','bearer','5183999'),(9,'2022-07-10 12:27:01.880985','2022-07-10 12:27:01.881033','-oNWqY4a72tFd5R2mrOfX55vPDnIzm8o5R6DOwc5CilvVQAAAYHoE9C7','A-rSV1OtWUiZnXRBoDMNJ06vFApORqrzFcZvHXGACilvVQAAAYHoE9C6','bearer','5183999'),(10,'2022-07-14 00:50:33.166416','2022-07-14 00:50:33.166461','wGYwq5U1e_gqUBkddtgK1Gj2QgttEw-cBMnc7S5pCisM0gAAAYH6L5tn','PkUaX_D5Mr6_7FtrBVcF7UXT_tcTwwv-w4irCfABCisM0gAAAYH6L5tn','bearer','5183999');
/*!40000 ALTER TABLE `social_tokens` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tags` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(50) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
INSERT INTO `tags` VALUES (1,'영화'),(2,'데이트'),(3,'주말'),(4,'평일');
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Thumbnail_images`
--

DROP TABLE IF EXISTS `Thumbnail_images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Thumbnail_images` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `image_id` bigint NOT NULL,
  `movie_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Thumbnail_images_image_id_4d7f1a24_fk_images_id` (`image_id`),
  KEY `Thumbnail_images_movie_id_3544d65c_fk_movies_id` (`movie_id`),
  CONSTRAINT `Thumbnail_images_image_id_4d7f1a24_fk_images_id` FOREIGN KEY (`image_id`) REFERENCES `images` (`id`),
  CONSTRAINT `Thumbnail_images_movie_id_3544d65c_fk_movies_id` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Thumbnail_images`
--

LOCK TABLES `Thumbnail_images` WRITE;
/*!40000 ALTER TABLE `Thumbnail_images` DISABLE KEYS */;
INSERT INTO `Thumbnail_images` VALUES (1,1,1),(2,2,2),(3,24,3);
/*!40000 ALTER TABLE `Thumbnail_images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  `social_id` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  `nickname` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `email` varchar(100) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `password` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `phone_number` varchar(50) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `refresh_token` varchar(300) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `is_valid` tinyint(1) NOT NULL,
  `group_id` bigint NOT NULL,
  `social_platform_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `social_id` (`social_id`),
  UNIQUE KEY `email` (`email`),
  KEY `users_group_id_66e6c4a0_fk_groups_id` (`group_id`),
  KEY `users_social_platform_id_3db2d68a_fk_social_platforms_id` (`social_platform_id`),
  CONSTRAINT `users_group_id_66e6c4a0_fk_groups_id` FOREIGN KEY (`group_id`) REFERENCES `groups` (`id`),
  CONSTRAINT `users_social_platform_id_3db2d68a_fk_social_platforms_id` FOREIGN KEY (`social_platform_id`) REFERENCES `social_platforms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'2022-07-08 10:54:54.409269','2022-07-08 10:54:54.409289','master','master','master@myview.co','manager1111!','010-0000-0000','1',1,1,1),(2,'2022-07-08 10:54:54.411582','2022-07-08 10:54:54.411596','manager_sg','manager_sg','manager_sg@myview.co','manager1111!','010-1111-2222','1',1,1,1),(3,'2022-07-08 10:54:54.412947','2022-07-08 10:54:54.412959','manager_si','manager_si','manager_si@myview.co','manager1111!','010-2222-3333','1',1,1,1),(4,'2022-07-08 10:54:54.414809','2022-07-08 10:54:54.414821','manager_ej','manager_ej','manager_ej@myview.co','manager1111!','010-3333-4444','1',1,1,1),(5,'2022-07-08 10:54:54.417149','2022-07-08 10:54:54.417161','manager_mk','manager_mk','manager_mk@myview.co','manager1111!','010-4444-5555','1',1,1,1),(6,'2022-07-08 10:54:54.419378','2022-07-08 10:54:54.419391','jjang9','짱구','jjang9@gmail.com','test1234!','010-1234-5678','2',1,1,1),(7,'2022-07-08 10:54:54.421599','2022-07-08 10:54:54.421632','chulsoo','철수','chulsoo@gmail.com','test1234!','010-2345-6789','2',1,1,1),(8,'2022-07-08 10:54:54.424577','2022-07-08 10:54:54.424595','hoon2','훈이','hoon2@gmail.com','test1234!','010-3456-7890','2',1,1,1),(9,'2022-07-08 10:54:54.426338','2022-07-08 10:54:54.426351','glass','유리','glass@gmail.com','test1234!','010-4567-8901','2',1,1,1),(10,'2022-07-08 10:54:54.428087','2022-07-08 10:54:54.428099','maeng9','맹구','maeng9@gmail.com','test1234!','010-5678-9012','2',1,1,1),(11,'2022-07-09 18:04:45.934826','2022-07-09 18:04:45.988760','2252016505','윤명국','kkookkss@kakao.com',NULL,NULL,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTEsImV4cCI6MTY1Nzg0NjIzM30.KPmPfqVsmlLV6iefq8KgRaMu0vqGQUDI8iO0qRCMdsY',1,2,2),(12,'2022-07-09 18:27:35.651871','2022-07-09 18:27:35.669646','2258035987','전슬기','jsg9712@naver.com',NULL,NULL,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTIsImV4cCI6MTY1NzU0MjQyMX0.dX2Gi2qBDFe41Ow5hdMwc2ZHn9jfGRGUxcofsHtJs5w',1,2,2),(13,'2022-07-09 18:51:39.949713','2022-07-12 08:38:31.052630','3m_pEXCfl7C-xmokcEUxhRe5WBo3UdujcMbS5q1T_Mc','정수인','audgns9207@naver.com',NULL,NULL,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTMsImV4cCI6MTY1NzcwMTUxMX0.qRzBDU0BijMUYf-3n8oPuxKaKS7pegEFCfZ2McNSj7Y',1,2,3),(14,'2022-07-09 18:51:42.894186','2022-07-10 12:19:21.813221','AVPh7j6w8duUr1EvejqZ-8NmH3I631lD-KoPkla3vlY','전슬기','sg04185@hanmail.net',NULL,NULL,'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MTQsImV4cCI6MTY1NzU0MTk2MX0.-fy9ht0L_EDn2o9tS1_CcuC-rXjT33grObBrdcxZj0c',1,2,3);
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `videos`
--

DROP TABLE IF EXISTS `videos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `videos` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `video_url` varchar(200) COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `videos`
--

LOCK TABLES `videos` WRITE;
/*!40000 ALTER TABLE `videos` DISABLE KEYS */;
INSERT INTO `videos` VALUES (1,'video/movie/%EB%B2%94%EC%A3%84%EB%8F%84%EC%8B%9C2.MOV'),(2,'video/movie/%EB%B2%94%EC%A3%84%EB%8F%84%EC%8B%9C2.MOV'),(3,'video/movie/%EB%B2%94%EC%A3%84%EB%8F%84%EC%8B%9C2.MOV'),(4,'video/movie/%EB%B2%94%EC%A3%84%EB%8F%84%EC%8B%9C2.MOV'),(5,'video/movie/%EB%B2%94%EC%A3%84%EB%8F%84%EC%8B%9C2.MOV'),(6,'video/movie/%EB%B2%84%EC%A6%88_%EB%9D%BC%EC%9D%B4%ED%8A%B8%EC%9D%B4%EC%96%B4.MOV'),(7,'video/movie/%EB%B2%84%EC%A6%88_%EB%9D%BC%EC%9D%B4%ED%8A%B8%EC%9D%B4%EC%96%B4.MOV'),(8,'video/movie/%EB%B2%84%EC%A6%88_%EB%9D%BC%EC%9D%B4%ED%8A%B8%EC%9D%B4%EC%96%B4.MOV'),(9,'video/movie/%EB%B2%84%EC%A6%88_%EB%9D%BC%EC%9D%B4%ED%8A%B8%EC%9D%B4%EC%96%B4.MOV'),(10,'video/movie/%EB%B2%84%EC%A6%88_%EB%9D%BC%EC%9D%B4%ED%8A%B8%EC%9D%B4%EC%96%B4.MOV'),(11,'video/movie/%E1%84%8B%E1%85%A1%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB.MOV'),(12,'video/movie/%E1%84%8B%E1%85%A1%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB.MOV'),(13,'video/movie/%E1%84%8B%E1%85%A1%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB.MOV'),(14,'video/movie/%E1%84%8B%E1%85%A1%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB.MOV'),(15,'video/movie/%E1%84%8B%E1%85%A1%E1%86%A8%E1%84%8B%E1%85%B5%E1%86%AB%E1%84%8C%E1%85%A5%E1%86%AB.MOV');
/*!40000 ALTER TABLE `videos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-14 19:54:17
