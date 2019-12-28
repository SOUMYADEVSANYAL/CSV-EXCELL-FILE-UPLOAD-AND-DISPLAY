-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 06, 2019 at 11:45 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.1.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student_db`
--
CREATE DATABASE IF NOT EXISTS `student_db` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE `student_db`;

-- --------------------------------------------------------

--
-- Table structure for table `cse`
--

CREATE TABLE `cse` (
  `id` int(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Roll_Number` int(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Email_Sent` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cse`
--

INSERT INTO `cse` (`id`, `Name`, `Roll_Number`, `Email`, `Email_Sent`) VALUES
(1, 'Siddhartha Addy', 99, 'sbdk12@gmail.com', 1),
(14, 'Sachin', 19, '', 0),
(15, 'Ritam', 21, '', 0),
(16, 'Pritha', 22, '', 0),
(34, 'Bal Baba', 39, 'abc@gmail.com', 0);

-- --------------------------------------------------------

--
-- Table structure for table `ece`
--

CREATE TABLE `ece` (
  `id` int(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Roll_Number` int(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Email_Sent` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `ee`
--

CREATE TABLE `ee` (
  `id` int(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Roll_Number` int(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Email_Sent` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `me`
--

CREATE TABLE `me` (
  `id` int(255) NOT NULL,
  `Name` varchar(255) NOT NULL,
  `Roll_Number` int(255) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Email_Sent` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `cse`
--
ALTER TABLE `cse`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ece`
--
ALTER TABLE `ece`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `ee`
--
ALTER TABLE `ee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `me`
--
ALTER TABLE `me`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `cse`
--
ALTER TABLE `cse`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `ece`
--
ALTER TABLE `ece`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `ee`
--
ALTER TABLE `ee`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `me`
--
ALTER TABLE `me`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
