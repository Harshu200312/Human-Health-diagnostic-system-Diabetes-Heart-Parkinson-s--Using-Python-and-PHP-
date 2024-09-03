-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jan 03, 2024 at 10:32 AM
-- Server version: 8.0.34
-- PHP Version: 8.1.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ashwini`
--

-- --------------------------------------------------------

--
-- Table structure for table `diabetes_data`
--

DROP TABLE IF EXISTS `diabetes_data`;
CREATE TABLE IF NOT EXISTS `diabetes_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `pregnancies` float DEFAULT NULL,
  `glucose` float DEFAULT NULL,
  `blood_pressure` float DEFAULT NULL,
  `skin_thickness` float DEFAULT NULL,
  `insulin` float DEFAULT NULL,
  `bmi` float DEFAULT NULL,
  `diabetes_pedigree_function` float DEFAULT NULL,
  `age` float DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `result` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
) 

--
-- Dumping data for table `diabetes_data`
--

INSERT INTO `diabetes_data` (`id`, `user_id`, `pregnancies`, `glucose`, `blood_pressure`, `skin_thickness`, `insulin`, `bmi`, `diabetes_pedigree_function`, `age`, `timestamp`, `result`) VALUES
(1, 2, 2, 120, 70, 23, 80, 25.5, 0.45, 30, '2023-12-28 08:57:39', NULL),
(2, 2, 2, 120, 70, 23, 80, 25.5, 0.45, 30, '2023-12-28 09:12:21', 'The person is not likely to have diabetes.');

-- --------------------------------------------------------

--
-- Table structure for table `heart_disease_data`
--

DROP TABLE IF EXISTS `heart_disease_data`;
CREATE TABLE IF NOT EXISTS `heart_disease_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `age` int DEFAULT NULL,
  `sex` varchar(10) DEFAULT NULL,
  `cp` int DEFAULT NULL,
  `trestbps` int DEFAULT NULL,
  `chol` int DEFAULT NULL,
  `fbs` int DEFAULT NULL,
  `restecg` int DEFAULT NULL,
  `thalach` int DEFAULT NULL,
  `exang` int DEFAULT NULL,
  `oldpeak` float DEFAULT NULL,
  `slope` int DEFAULT NULL,
  `ca` int DEFAULT NULL,
  `thal` int DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `result` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
)

--
-- Dumping data for table `heart_disease_data`
--

INSERT INTO `heart_disease_data` (`id`, `user_id`, `age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`, `timestamp`, `result`) VALUES
(1, 2, 54, '1', 0, 125, 210, 0, 0, 170, 0, 1.6, 0, 0, 0, '2023-12-30 07:08:00', 'The person is likely to have heart disease.');

-- --------------------------------------------------------

--
-- Table structure for table `parkinsons_data`
--

DROP TABLE IF EXISTS `parkinsons_data`;
CREATE TABLE IF NOT EXISTS `parkinsons_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `mdvp_fo` float DEFAULT NULL,
  `mdvp_fhi` float DEFAULT NULL,
  `mdvp_flo` float DEFAULT NULL,
  `mdvp_jitter` float DEFAULT NULL,
  `mdvp_jitter_abs` float DEFAULT NULL,
  `rap` float DEFAULT NULL,
  `ppq` float DEFAULT NULL,
  `ddp` float DEFAULT NULL,
  `mdvp_shimmer` float DEFAULT NULL,
  `shimmer_db` float DEFAULT NULL,
  `apq3` float DEFAULT NULL,
  `apq5` float DEFAULT NULL,
  `apq` float DEFAULT NULL,
  `dda` float DEFAULT NULL,
  `nhr` float DEFAULT NULL,
  `hnr` float DEFAULT NULL,
  `rpde` float DEFAULT NULL,
  `dfa` float DEFAULT NULL,
  `spread1` float DEFAULT NULL,
  `spread2` float DEFAULT NULL,
  `d2` float DEFAULT NULL,
  `ppe` float DEFAULT NULL,
  `timestamp` datetime DEFAULT NULL,
  `result` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`)
)

--
-- Dumping data for table `parkinsons_data`
--

INSERT INTO `parkinsons_data` (`id`, `user_id`, `mdvp_fo`, `mdvp_fhi`, `mdvp_flo`, `mdvp_jitter`, `mdvp_jitter_abs`, `rap`, `ppq`, `ddp`, `mdvp_shimmer`, `shimmer_db`, `apq3`, `apq5`, `apq`, `dda`, `nhr`, `hnr`, `rpde`, `dfa`, `spread1`, `spread2`, `d2`, `ppe`, `timestamp`, `result`) VALUES
(1, 2, 119.992, 157.302, 74.997, 0.00784, 0.00003, 0.0037, 0.00554, 0.01109, 0.04374, 0.426, 0.02971, 0.0313, 0.02971, 0.08868, 0.01393, 21, 0.414783, 0.815285, -4.81303, 0.266482, 2.30144, 0.284654, '2023-12-28 09:44:29', 'The person is likely to have Parkinson\'s disease.');

-- --------------------------------------------------------

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
CREATE TABLE IF NOT EXISTS `user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(80) NOT NULL,
  `last_name` varchar(80) NOT NULL,
  `email` varchar(120) NOT NULL,
  `phone_number` varchar(20) DEFAULT NULL,
  `birthdate` date DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `username` varchar(80) NOT NULL,
  `password` varchar(80) NOT NULL,
  `verified` tinyint(1) DEFAULT '0',
  `otp` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) 

--
-- Dumping data for table `user`
--

INSERT INTO `user` (`id`, `first_name`, `last_name`, `email`, `phone_number`, `birthdate`, `gender`, `username`, `password`, `verified`, `otp`) VALUES
(2, 'harshu', '2003', 'harshu@gmail.com', '8097837008', '2003-10-01', 'Female', 'Harshu', 'harshu123', 0, NULL);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `diabetes_data`
--
ALTER TABLE `diabetes_data`
  ADD CONSTRAINT `diabetes_data_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `heart_disease_data`
--
ALTER TABLE `heart_disease_data`
  ADD CONSTRAINT `heart_disease_data_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);

--
-- Constraints for table `parkinsons_data`
--
ALTER TABLE `parkinsons_data`
  ADD CONSTRAINT `parkinsons_data_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
