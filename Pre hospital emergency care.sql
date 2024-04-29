-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 04, 2024 at 11:03 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `firstaidthroughai`
--

-- --------------------------------------------------------

--
-- Table structure for table `doctorsolution`
--

CREATE TABLE `doctorsolution` (
  `incident` varchar(50) NOT NULL,
  `firstaid` varchar(500) NOT NULL,
  `finalaid` varchar(500) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctorsolution`
--

INSERT INTO `doctorsolution` (`incident`, `firstaid`, `finalaid`) VALUES
('headache', 'take rest', 'consult doctor');

-- --------------------------------------------------------

--
-- Table structure for table `patientregister`
--

CREATE TABLE `patientregister` (
  `patientid` int(5) NOT NULL,
  `patientname` varchar(100) NOT NULL,
  `area` varchar(50) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `patienttype` varchar(10) NOT NULL,
  `sick` varchar(10) NOT NULL,
  `age` varchar(10) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patientregister`
--

INSERT INTO `patientregister` (`patientid`, `patientname`, `area`, `gender`, `patienttype`, `sick`, `age`, `password`) VALUES
(1, 'kannan', 'central', 'male', 'adult', 'Chest Pain', '25', 'kannan12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `patientregister`
--
ALTER TABLE `patientregister`
  ADD PRIMARY KEY (`patientid`,`password`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
