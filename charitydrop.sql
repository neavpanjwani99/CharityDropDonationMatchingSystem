-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 23, 2025 at 09:38 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET FOREIGN_KEY_CHECKS=0;
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `charitydrop`
--

-- --------------------------------------------------------

--
-- Table structure for table `donations`
--

CREATE TABLE `donations` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `donation_type` enum('food','cloth','cash','studies') DEFAULT NULL,
  `food_option` enum('self','cash') DEFAULT NULL,
  `cash_purpose` varchar(100) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `study_items` text DEFAULT NULL,
  `message` text DEFAULT NULL,
  `donation_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `login_logs`
--

CREATE TABLE `login_logs` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `ip_address` varchar(50) DEFAULT NULL,
  `city` varchar(100) DEFAULT NULL,
  `country` varchar(100) DEFAULT NULL,
  `login_time` datetime DEFAULT NULL,
  `role` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login_logs`
--

INSERT INTO `login_logs` (`id`, `user_id`, `ip_address`, `city`, `country`, `login_time`, `role`) VALUES
(1, 1, '127.0.0.1', NULL, NULL, '2025-07-21 01:25:22', NULL),
(2, 2, '127.0.0.1', NULL, NULL, '2025-07-21 01:38:14', NULL),
(3, 1, '127.0.0.1', NULL, NULL, '2025-07-21 21:09:05', NULL),
(4, 2, '8.8.8.8', 'Mountain View', 'US', '2025-07-21 21:23:58', NULL),
(5, 1, '8.8.8.8', 'Mountain View', 'US', '2025-07-21 21:52:37', NULL),
(6, 1, '103.44.117.91', 'Mumbai', 'IN', '2025-07-23 23:56:25', 'donor'),
(7, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-23 23:57:40', 'admin'),
(8, 1, '103.44.117.91', 'Mumbai', 'IN', '2025-07-24 00:37:05', 'donor');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `twitter` varchar(100) DEFAULT NULL,
  `facebook` varchar(100) DEFAULT NULL,
  `gplus` varchar(100) DEFAULT NULL,
  `fname` varchar(50) DEFAULT NULL,
  `lname` varchar(50) DEFAULT NULL,
  `phone` varchar(20) DEFAULT NULL,
  `address` text DEFAULT NULL,
  `role` enum('donor','admin') NOT NULL DEFAULT 'donor'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `password`, `twitter`, `facebook`, `gplus`, `fname`, `lname`, `phone`, `address`, `role`) VALUES
(1, 'meena@gmail.com', 'scrypt:32768:8:1$oHYZeyMHu1p7MVdq$4b1c27b412475d7b0bf248e8b6f38746cebe1c26d784eacfb4c2e35fdf069b84be2565ac38a2f4d2220d784f48603f4dfa0e25d159a968562f5260b29741cd84', 'meena12', 'meena_12', 'meena', 'Meena', 'Nirvan', '08169070930', 'grace chs', 'donor'),
(4, 'manya@gmail.com', 'scrypt:32768:8:1$tGogh0UyRWi9zGHh$d68839fe3dec03f07ba8b31123d97b49bd8d6dd1f41c1654f2517b75028d8c4792b8998c3ed895e090469240b61ba4c29b79517d691c984c5e72436d0e21706f', NULL, NULL, NULL, 'Manya', 'Nirvan', NULL, 'GRACE CHS', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `donations`
--
ALTER TABLE `donations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `login_logs`
--
ALTER TABLE `login_logs`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `donations`
--
ALTER TABLE `donations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `login_logs`
--
ALTER TABLE `login_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `donations`
--
ALTER TABLE `donations`
  ADD CONSTRAINT `donations_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

--
-- Constraints for table `login_logs`
--
ALTER TABLE `login_logs`
  ADD CONSTRAINT `login_logs_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);
SET FOREIGN_KEY_CHECKS=1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
