'''
Use https://mariadb.org for installation guidance;
here you will also be prompted to create a root password
'''

# Post install, login as root user to see any databases and to create new user or tables 
waldorna@waldorna-ThinkPad-E570 ~ $ mysql -u root -p
Enter password: 
# Welcome to the MariaDB monitor.  Commands end with ; or \g.
# Your MariaDB connection id is 47
# Server version: 10.3.11-MariaDB-1:10.3.11+maria~bionic mariadb.org binary distribution

# Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.


'''
You are now connected to the MariaDB shell and logged in
'''
MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| mysql              |
| performance_schema |
+--------------------+
3 rows in set (0.001 sec)

MariaDB [(none)]> CREATE DATABASE lxfdata;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> USE lxfdata;
Database changed

waldorna@waldorna-ThinkPad-E570 ~ $ mysql -u lxfuser lxfdata -p
Enter password: 
# Reading table information for completion of table and column names
# You can turn off this feature to get a quicker startup with -A

# Welcome to the MariaDB monitor.  Commands end with ; or \g.
# Your MariaDB connection id is 64
# Server version: 10.3.11-MariaDB-1:10.3.11+maria~bionic mariadb.org binary distribution

# Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [lxfdata]> CREATE TABLE linuxes(
    -> id int(5) NOT NULL AUTO_INCREMENT,
    -> name varchar(32) DEFAULT NULL,
    -> current_version varchar(32) DEFAULT NULL,
    -> easy bool DEFAULT NULL,
    -> PRIMARY KEY(id)
    -> );
Query OK, 0 rows affected (0.279 sec)

MariaDB [lxfdata]> SHOW COLUMNS FROM linuxes;
+-----------------+-------------+------+-----+---------+----------------+
| Field           | Type        | Null | Key | Default | Extra          |
+-----------------+-------------+------+-----+---------+----------------+
| id              | int(5)      | NO   | PRI | NULL    | auto_increment |
| name            | varchar(32) | YES  |     | NULL    |                |
| current_version | varchar(32) | YES  |     | NULL    |                |
| easy            | tinyint(1)  | YES  |     | NULL    |                |
+-----------------+-------------+------+-----+---------+----------------+
4 rows in set (0.003 sec)

MariaDB [lxfdata]> CREATE USER 'lxfuser'@'localhost' IDENTIFIED BY 'password1';

MariaDB [lxfdata]> GRANT INSERT, SELECT on lxfdata.linuxes TO 'lxfusers'@'localhost';

# Using Ctrl + D to exit:
MariaDB [lxfdata]> Bye

waldorna@waldorna-ThinkPad-E570 ~ $ mysql -u lxfuser lxfdata -p
Enter password: 
# Reading table information for completion of table and column names
# You can turn off this feature to get a quicker startup with -A

# Welcome to the MariaDB monitor.  Commands end with ; or \g.
# Your MariaDB connection id is 64
# Server version: 10.3.11-MariaDB-1:10.3.11+maria~bionic mariadb.org binary distribution

# Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [lxfdata]> GRANT INSERT, SELECT on lxfdata.linuxes TO 'lxfuser'@'localhost';
Query OK, 0 rows affected (0.001 sec)

# Using Ctrl + D to exit:
MariaDB [lxfdata]> Bye

MariaDB [lxfdata]> INSERT INTO linuxes(name, current_version, easy) VALUES('Red Star Linux', '3.0',0);
Query OK, 1 row affected (0.055 sec)

MariaDB [lxfdata]> INSERT INTO linuxes(name, easy) VALUES('Arch Linux', 0), ('Gentoo', 0);
Query OK, 2 rows affected (0.056 sec)
Records: 2  Duplicates: 0  Warnings: 0

MariaDB [lxfdata]> INSERT INTO linuxes(name, current_version, easy) VALUES
    -> ('Ubuntu', '18.10 Cosmic Cuttlefish', 1), 
    -> ('Linux Mint', '19.1 Tessa', 1), 
    -> ('Debian', '7.8 Wheezy', 0), 
    -> ('Fedora', '22', 0), 
    -> ('openSUSE', '13.2', 1), 
    -> ('ElementaryOS', '0.2 Luna', 1), 
    -> ('Mageia', '4.1', 1), 
    -> ('Bodhi Linux', '3.0.0', 1);
Query OK, 8 rows affected (0.051 sec)
Records: 8  Duplicates: 0  Warnings: 0

MariaDB [lxfdata]> SELECT * FROM linuxes;
+----+----------------+-------------------------+------+
| id | name           | current_version         | easy |
+----+----------------+-------------------------+------+
|  1 | Red Star Linux | 3.0                     |    0 |
|  2 | Arch Linux     | NULL                    |    0 |
|  3 | Gentoo         | NULL                    |    0 |
|  4 | Ubuntu         | 18.10 Cosmic Cuttlefish |    1 |
|  5 | Linux Mint     | 19.1 Tessa              |    1 |
|  6 | Debian         | 7.8 Wheezy              |    0 |
|  7 | Fedora         | 22                      |    0 |
|  8 | openSUSE       | 13.2                    |    1 |
|  9 | ElementaryOS   | 0.2 Luna                |    1 |
| 10 | Mageia         | 4.1                     |    1 |
| 11 | Bodhi Linux    | 3.0.0                   |    1 |
+----+----------------+-------------------------+------+
11 rows in set (0.001 sec)

MariaDB [lxfdata]> SELECT name, current_version FROM linuxes;
+----------------+-------------------------+
| name           | current_version         |
+----------------+-------------------------+
| Red Star Linux | 3.0                     |
| Arch Linux     | NULL                    |
| Gentoo         | NULL                    |
| Ubuntu         | 18.10 Cosmic Cuttlefish |
| Linux Mint     | 19.1 Tessa              |
| Debian         | 7.8 Wheezy              |
| Fedora         | 22                      |
| openSUSE       | 13.2                    |
| ElementaryOS   | 0.2 Luna                |
| Mageia         | 4.1                     |
| Bodhi Linux    | 3.0.0                   |
+----------------+-------------------------+
11 rows in set (0.001 sec)

MariaDB [lxfdata]> SELECT * FROM linuxes WHERE easy = 1;
+----+--------------+-------------------------+------+
| id | name         | current_version         | easy |
+----+--------------+-------------------------+------+
|  4 | Ubuntu       | 18.10 Cosmic Cuttlefish |    1 |
|  5 | Linux Mint   | 19.1 Tessa              |    1 |
|  8 | openSUSE     | 13.2                    |    1 |
|  9 | ElementaryOS | 0.2 Luna                |    1 |
| 10 | Mageia       | 4.1                     |    1 |
| 11 | Bodhi Linux  | 3.0.0                   |    1 |
+----+--------------+-------------------------+------+
6 rows in set (0.001 sec)

MariaDB [lxfdata]> SELECT * FROM linuxes WHERE easy = 1 ORDER BY name;
+----+--------------+-------------------------+------+
| id | name         | current_version         | easy |
+----+--------------+-------------------------+------+
| 11 | Bodhi Linux  | 3.0.0                   |    1 |
|  9 | ElementaryOS | 0.2 Luna                |    1 |
|  5 | Linux Mint   | 19.1 Tessa              |    1 |
| 10 | Mageia       | 4.1                     |    1 |
|  8 | openSUSE     | 13.2                    |    1 |
|  4 | Ubuntu       | 18.10 Cosmic Cuttlefish |    1 |
+----+--------------+-------------------------+------+
6 rows in set (0.001 sec)

waldorna@waldorna-ThinkPad-E570 ~ $ mysql -u root lxfdata -p
Enter password: 
# Reading table information for completion of table and column names
# You can turn off this feature to get a quicker startup with -A

# Welcome to the MariaDB monitor.  Commands end with ; or \g.
# Your MariaDB connection id is 65
# Server version: 10.3.11-MariaDB-1:10.3.11+maria~bionic mariadb.org binary distribution

# Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [lxfdata]> GRANT UPDATE, DELETE on lxfdata.linuxes TO 'lxfuser'@'localhost';
Query OK, 0 rows affected (0.001 sec)

# Used Ctrl + D command to exit
MariaDB [lxfdata]> Bye
waldorna@waldorna-ThinkPad-E570 ~ $ mysql -u lxfuser lxfdata -p
Enter password: 
# Reading table information for completion of table and column names
# You can turn off this feature to get a quicker startup with -A

# Welcome to the MariaDB monitor.  Commands end with ; or \g.
# Your MariaDB connection id is 66
# Server version: 10.3.11-MariaDB-1:10.3.11+maria~bionic mariadb.org binary distribution

# Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

# Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [lxfdata]> UPDATE linuxes SET easy=1 WHERE name='Gentoo';
Query OK, 1 row affected (0.048 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [lxfdata]> DELETE FROM linuxes WHERE name='Ubuntu';
Query OK, 1 row affected (0.054 sec)

# Used Ctrl + D command to exit
MariaDB [lxfdata]> Bye
waldorna@waldorna-ThinkPad-E570 ~ $ 


'''
To export database or tables - Should be done every-so often to avoid data loss
'''
# Login as root as tables and database are locked - Using 'mysqldump' command in terminal
waldorna@waldorna-ThinkPad-E570 ~ $ mysqldump lxfdata linuxes -u root -p
Enter password: 
-- MySQL dump 10.17  Distrib 10.3.11-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: lxfdata
-- ------------------------------------------------------
-- Server version	10.3.11-MariaDB-1:10.3.11+maria~bionic

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `linuxes`
--

DROP TABLE IF EXISTS `linuxes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `linuxes` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) DEFAULT NULL,
  `current_version` varchar(32) DEFAULT NULL,
  `easy` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `linuxes`
--

LOCK TABLES `linuxes` WRITE;
/*!40000 ALTER TABLE `linuxes` DISABLE KEYS */;
INSERT INTO `linuxes` VALUES (1,'Red Star Linux','3.0',0),(2,'Arch Linux',NULL,0),(3,'Gentoo',NULL,1),(5,'Linux Mint','19.1 Tessa',1),(6,'Debian','7.8 Wheezy',0),(7,'Fedora','22',0),(8,'openSUSE','13.2',1),(9,'ElementaryOS','0.2 Luna',1),(10,'Mageia','4.1',1),(11,'Bodhi Linux','3.0.0',1);
/*!40000 ALTER TABLE `linuxes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-01-16  9:53:46

'''
Or you can dump the data into an sql file so that importing into database
will be much easier
'''
# all you need to add is > dataset-name.sql
waldorna@waldorna-ThinkPad-E570 ~ $ mysqldump lxfdata linuxes -u root -p > linuxes.sql
Enter password: 
waldorna@waldorna-ThinkPad-E570 ~ $