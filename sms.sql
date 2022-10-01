-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 09, 2021 at 05:55 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.0.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sms`
--

-- --------------------------------------------------------

--
-- Table structure for table `advisor`
--

CREATE TABLE `advisor` (
  `ID` varchar(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Phone` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `advisor`
--

INSERT INTO `advisor` (`ID`, `Name`, `Phone`, `Email`) VALUES
('710000000', 'Tania Khatun', '0123456789', 'tania@diu.com'),
('720000000', 'Shaila Sharmin', '01234567890', '@diu.com');

-- --------------------------------------------------------

--
-- Table structure for table `cgpa`
--

CREATE TABLE `cgpa` (
  `ID` varchar(100) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `CGPA` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `cgpa`
--

INSERT INTO `cgpa` (`ID`, `Name`, `CGPA`) VALUES
('201-15-3057', 'Real', '1.75'),
('201-15-3201', 'Fahim', '3.20'),
('201-15-3333', 'Efti', '2.00');

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `deptname` varchar(100) NOT NULL,
  `Facultyname` varchar(100) NOT NULL,
  `Email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`deptname`, `Facultyname`, `Email`) VALUES
('Department of Business Administration', 'Dr. Gouranga Chandra Debnath', 'debnath@daffodilvarsity.edu.bd'),
('Department of Business Studies', 'Md. Ali Imran', 'headdbs@daffodilvarsity.edu.bd');

-- --------------------------------------------------------

--
-- Table structure for table `greengarden`
--

CREATE TABLE `greengarden` (
  `Name` varchar(200) NOT NULL,
  `Price` varchar(200) NOT NULL,
  `Time` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `greengarden`
--

INSERT INTO `greengarden` (`Name`, `Price`, `Time`) VALUES
('Alu borta', '10', 'Dinner'),
('morgi', '100', 'Dinner');

-- --------------------------------------------------------

--
-- Table structure for table `registers`
--

CREATE TABLE `registers` (
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `securityQ` varchar(100) NOT NULL,
  `securityA` varchar(100) NOT NULL,
  `pass` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registers`
--

INSERT INTO `registers` (`fname`, `lname`, `contact`, `email`, `securityQ`, `securityA`, `pass`) VALUES
('MD', 'Fahim', '0123456789', '@diu.com', 'Your Pet Name', 'Cat', '1234'),
('Alif', 'vai', '123456789', 'alif@diu.com', 'Your Pet Name', 'cat', '123'),
('B.M.Samiul Haque', 'Real', '01709855540', 'diu@edu.bd', 'Your Birth Place', 'Chittagang', '123'),
('Efti', 'haidar', '123456789', 'efti@edu.com', 'Your Pet Name', 'Cat', '1234'),
('Mimmoy', 'Islam', '1234567890', 'm@gmail.com', 'Your Pet Name', 'Cat', '1234'),
('Shanjida Hossain', 'Shefa', '0123456789', 'shefa@diu.com', 'Your Pet Name', 'cat', '123');

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `ID` varchar(100) NOT NULL,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `contact` varchar(100) NOT NULL,
  `dob` varchar(100) NOT NULL,
  `address` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`ID`, `name`, `email`, `gender`, `contact`, `dob`, `address`) VALUES
('3042', 'Shefa', 'shefa@edu.bd', 'Female', '01234567890', '27 November 2000', 'Mirpur\n'),
('3057', 'Real', 'diu@edu.bd', 'Male', '1709855540', '06 April 2000', 'ECB Chattar\n\n\n'),
('3201', 'Fahim', 'fahim@diu.com', 'Male', '1234567890', 'May 2000', 'Mipur 10\n\n\n\n\n\n\n\n\n');

-- --------------------------------------------------------

--
-- Table structure for table `waiver`
--

CREATE TABLE `waiver` (
  `ID` varchar(100) NOT NULL,
  `Semester` varchar(100) NOT NULL,
  `Percentage` varchar(100) NOT NULL,
  `Total Tuition Fees` varchar(100) NOT NULL,
  `After Waiver Fees` varchar(100) NOT NULL,
  `Registration Fees` varchar(100) NOT NULL,
  `Without Registration Fees` varchar(100) NOT NULL,
  `Mid Fees` varchar(100) NOT NULL,
  `Final Fees` varchar(100) NOT NULL,
  `Name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `waiver`
--

INSERT INTO `waiver` (`ID`, `Semester`, `Percentage`, `Total Tuition Fees`, `After Waiver Fees`, `Registration Fees`, `Without Registration Fees`, `Mid Fees`, `Final Fees`, `Name`) VALUES
('201-15-3042', '6', '40', '59300', '49080.0', '13500', '35580.0', '17790.0', '17790.0', 'Shefa'),
('201-15-3057', '6', '70', '59300', '31290.0', '13500', '17790.0', '8895.0', '8895.0', 'Real'),
('201-15-3201', '6', '60', '59300', '37220.0', '13500', '23720.0', '11860.0', '11860.0', 'Fahim'),
('201-15-3333', '6', '80', '59300', '25360.0', '13500', '11860.0', '5930.0', '5930.0', 'Efti');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `advisor`
--
ALTER TABLE `advisor`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `cgpa`
--
ALTER TABLE `cgpa`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`deptname`);

--
-- Indexes for table `greengarden`
--
ALTER TABLE `greengarden`
  ADD PRIMARY KEY (`Name`);

--
-- Indexes for table `registers`
--
ALTER TABLE `registers`
  ADD PRIMARY KEY (`email`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `waiver`
--
ALTER TABLE `waiver`
  ADD PRIMARY KEY (`ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
