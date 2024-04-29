-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 30, 2024 at 08:10 AM
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
-- Database: `multidisease`
--

-- --------------------------------------------------------

--
-- Table structure for table `newuser`
--

CREATE TABLE `newuser` (
  `userid` int(3) NOT NULL,
  `name` varchar(20) NOT NULL,
  `area` varchar(20) NOT NULL,
  `gender` varchar(10) NOT NULL,
  `ptype` varchar(10) NOT NULL,
  `mobile` varchar(10) NOT NULL,
  `email` varchar(20) NOT NULL,
  `password` varchar(8) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `newuser`
--

INSERT INTO `newuser` (`userid`, `name`, `area`, `gender`, `ptype`, `mobile`, `email`, `password`) VALUES
(1, 'kannan', 'puthur', 'radio', '', '2147483647', 'kannan@gmail.com', '!@#$%^&*'),
(1, 'kannan', 'puthur', 'male', '', '2147483647', 'kannan@gmail.com', '!@#$%^&*'),
(1, 'kannan', 'puthur', 'male', '', '6379007560', 'kannan@gmail.com', '!@#$%^&*'),
(2, 'kumar', 'thennur', 'male', '', '7558105934', 'killer@gmail.com', 'killer'),
(1, 'kamala kannan', 'puthur', 'male', '', '6379007560', 'fraudkk123@gmail.com', 'kannan12'),
(1, 'kannan', 'chathiram', 'male', 'child', '6379007560', 'kannan@gmail.com', 'kannan12');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
