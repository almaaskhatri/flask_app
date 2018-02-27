-- phpMyAdmin SQL Dump
-- version 4.5.1
-- http://www.phpmyadmin.net
--
-- Host: 127.0.0.1
-- Generation Time: Feb 27, 2018 at 12:35 PM
-- Server version: 10.1.13-MariaDB
-- PHP Version: 5.6.23

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `myflaskapp`
--

-- --------------------------------------------------------

--
-- Table structure for table `articles`
--

CREATE TABLE `articles` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL,
  `author` varchar(100) NOT NULL,
  `body` text NOT NULL,
  `create_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `articles`
--

INSERT INTO `articles` (`id`, `title`, `author`, `body`, `create_date`) VALUES
(3, '11111111', 'AbcdAbcd', '<p>asdasdaadsdasddasda</p>\r\n\r\n<p>&nbsp;</p>\r\n', '2018-02-27 10:58:12');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `username` varchar(30) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `DateTime` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `name`, `username`, `email`, `password`, `DateTime`) VALUES
(9, 'knadksjdn', 'nalsdnas', 'lndsadnal', 'scdsnsfsf', '2018-02-21 18:12:05'),
(23, 'name', 'email', 'username', 'password', '2018-02-21 18:31:23'),
(24, 'name', 'email', 'username', 'password', '2018-02-21 18:31:23'),
(30, 'dsalmaslk', 'dsalmaslk', 'dsalmaslk', 'dsalmaslk', '2018-02-21 18:46:25'),
(31, 'dsalmaslk', 'dsalmaslk', 'dsalmaslk', 'dsalmaslk', '2018-02-21 18:46:34'),
(32, 'fafkml', 'fafkml', 'fafkml', 'fafkml', '2018-02-22 11:15:49'),
(33, 'fafkmlfafkml', 'fafkmlfafkml', 'fafkmlfafkml', 'fafkml', '2018-02-22 11:15:55'),
(34, 'fafkmlfafkml', 'fafkmlfafkml', 'fafkmlfafkml', 'fafkml', '2018-02-22 11:16:39'),
(35, 'fafkmlfafkmlfafkml', 'fafkmlfafafkml', 'fafkmlfafkml', 'fafkml', '2018-02-22 11:18:24'),
(36, 'fafkmlfafkmlfafkml', 'fafkmlfafafkml', 'fafkmlfafkml', 'fafkml', '2018-02-22 11:26:55'),
(37, 'fafkmlfafkmlfafkml', 'fafkmlfafafkml', 'fafkmlfafkml', 'fafkml', '2018-02-22 11:27:43'),
(38, 'fafkmlfafkmlfafkml', 'fafkmlfafafkml', 'fafkmlfafkml', 'fafkml', '2018-02-22 11:27:51'),
(39, 'fafkmlfafkmlfafkml', 'fafkmlfafafkml', 'fafkmlfafkml', 'fafkml', '2018-02-22 11:30:55'),
(40, 'fafkmlfafkmlfafkml', 'fafkmlfafafkml', 'fafkmlfafkml', 'fafkml', '2018-02-22 11:31:43'),
(41, 'asdmakld', 'asdmakld', 'asdmakld', 'asdmakld', '2018-02-22 11:33:01'),
(42, 'dasasd', 'dasasd', 'dasasd', 'dasasd', '2018-02-22 11:37:15'),
(43, 'dasasd', 'dasasd', 'dasasd', 'dasasd', '2018-02-22 11:37:24'),
(44, 'dasasd', 'dasasd', 'dasasd', 'dasasd', '2018-02-22 11:39:13'),
(45, 'dasasd', 'dasasd', 'dasasd', 'dasasd', '2018-02-22 11:39:23'),
(46, 'dasasd', 'dasasd', 'dasasd', 'dasasd', '2018-02-22 11:40:47'),
(47, 'dasasd', 'dasasd', 'dasasd', 'dasasd', '2018-02-22 11:40:51'),
(48, 'Abcd', 'AbcdAbcd', 'Abcd', '$5$rounds=535000$L7E.rOay3Z3s693W$l3ZG.OqlHDKQS6frdhrbB8tFJczvVXb4T5oga/2VSJ8', '2018-02-23 12:58:48');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `articles`
--
ALTER TABLE `articles`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `articles`
--
ALTER TABLE `articles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
