-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 28, 2020 at 07:19 PM
-- Server version: 10.4.13-MariaDB
-- PHP Version: 7.2.32

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tech blogs`
--

-- --------------------------------------------------------

--
-- Table structure for table `contacts`
--

CREATE TABLE `contacts` (
  `SNo` int(10) NOT NULL,
  `NAME` text NOT NULL,
  `EMAIL` varchar(50) NOT NULL,
  `Phone` int(50) NOT NULL,
  `MESSAGE` text NOT NULL,
  `DATE` datetime DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `contacts`
--

INSERT INTO `contacts` (`SNo`, `NAME`, `EMAIL`, `Phone`, `MESSAGE`, `DATE`) VALUES
(1, 'meranaam', 'naam@gmail.com', 122354555, 'hdjjcnjcn', '2020-07-24 00:10:32'),
(19, 'ha', '', 0, '', '2020-07-24 21:43:17'),
(20, 'harsh', 'harsh@gmail.com', 1234556877, 'Bhai Mai Expert Hu ', '2020-07-24 21:43:37'),
(21, 'harsh', 'harsh@gmail.com', 1234556877, 'Bhai Mai Expert Hu ', '2020-07-24 23:57:10'),
(22, 'prinsu', 'example@gmail.com', 1234569870, 'Bas aise hi mann kar raha tha', '2020-07-25 12:23:14'),
(23, 'Hmm', 'example@gmail.com', 1234556877, 'bhai Bahut achha blog h', '2020-07-28 13:14:21');

-- --------------------------------------------------------

--
-- Table structure for table `posts`
--

CREATE TABLE `posts` (
  `SNo` int(10) NOT NULL,
  `Title` text NOT NULL,
  `Slug` varchar(20) NOT NULL,
  `Content` text NOT NULL,
  `Subtitle` text NOT NULL,
  `img_name` varchar(15) NOT NULL,
  `Date` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `posts`
--

INSERT INTO `posts` (`SNo`, `Title`, `Slug`, `Content`, `Subtitle`, `img_name`, `Date`) VALUES
(1, 'This is a Demo Post ', 'Demo-post', '  I\'m doing the testing part for adding post from database , so this is just a demo post    ', 'Subtitle nhi mil', 'post-bg.jpg', '2020-07-27 20:55:25'),
(2, 'Temlate Designer Documentation', 'Second-post', '', 'All about template ', 'about-bg.jpg', '2020-07-27 12:54:07'),
(3, 'Variables', 'third-post', 'Template variables are defined by the context dictionary passed to the template.\r\n\r\nYou can mess aro', 'what to learn Variables', 'contact-bg.jpg', '2020-07-25 13:15:40'),
(4, 'Filters', 'Slug-next', ' Variables can be modified by filters. Filters are separated from the variable by a pipe symbol aur Bhai A gaye Swad !!!!', 'Ab hum padhenge Filters ke bare me', 'home-bg.jpg', '2020-07-27 12:56:07'),
(5, 'Comments', 'slug-2', 'To comment-out part of a line in a template, use the comment syntax which is by default set to {# ..', 'learn about Comments', 'home-bg.jpg', '2020-07-25 13:21:22'),
(7, 'adding Post', 'add-0', 'Badhai Ho Post Add Ho gyi h..', 'ye wali post add kar de', 'admin-bg.jpg', '2020-07-27 20:55:00'),
(8, 'Final Post', 'Final-check', '   Holaaaaaaaa!!!!!!! Blog Completed!!!!!!!!!!! ', 'Bhai Blog Complete ho gya ', 'contact-bg.jpg', '2020-07-28 13:05:32');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `contacts`
--
ALTER TABLE `contacts`
  ADD PRIMARY KEY (`SNo`);

--
-- Indexes for table `posts`
--
ALTER TABLE `posts`
  ADD PRIMARY KEY (`SNo`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `contacts`
--
ALTER TABLE `contacts`
  MODIFY `SNo` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `posts`
--
ALTER TABLE `posts`
  MODIFY `SNo` int(10) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
