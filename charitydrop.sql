-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 25, 2025 at 09:50 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

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
-- Table structure for table `causes`
--

CREATE TABLE `causes` (
  `id` int(11) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `duration` int(11) DEFAULT NULL,
  `target_amount` decimal(10,2) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `description` text DEFAULT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `causes`
--

INSERT INTO `causes` (`id`, `title`, `duration`, `target_amount`, `category`, `description`, `created_at`) VALUES
(1, 'XYZ', 20, 1000.00, 'Menstrual Hygiene Kits', 'FOR WOMENS SAFETY', '2025-07-26 00:58:01');

-- --------------------------------------------------------

--
-- Table structure for table `contact_messages`
--

CREATE TABLE `contact_messages` (
  `id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(150) DEFAULT NULL,
  `subject` varchar(150) DEFAULT NULL,
  `message` text DEFAULT NULL,
  `created_at` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `contact_messages`
--

INSERT INTO `contact_messages` (`id`, `user_id`, `name`, `email`, `subject`, `message`, `created_at`) VALUES
(1, 1, 'Meena Nirvan', 'meenanirvan@gmail.com', 'want to meet the developer', 'ABCD WOWW!!', '2025-07-24 18:21:37'),
(2, 5, 'Ashok Nirvan', 'meenanirvan@gmail.com', 'abx', 'sfvvegt', '2025-07-25 04:39:11');

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
  `donation_type` varchar(255) DEFAULT NULL,
  `food_option` enum('self','cash') DEFAULT NULL,
  `cash_purpose` varchar(100) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `study_items` text DEFAULT NULL,
  `message` text DEFAULT NULL,
  `donation_time` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `donations`
--

INSERT INTO `donations` (`id`, `user_id`, `first_name`, `last_name`, `email`, `phone`, `donation_type`, `food_option`, `cash_purpose`, `amount`, `study_items`, `message`, `donation_time`) VALUES
(1, 1, 'Meena', 'Nirvan', 'meena@gmail.com', '8768809876', 'studies', NULL, '', 100.00, 'Books, Pen', 'ejkbkj', '2025-07-24 15:23:01'),
(2, 1, 'Meena', 'Nirvan', 'meena@gmail.com', '8768809876', 'studies', NULL, '', 100.00, 'Books, Pen', 'ejkbkj', '2025-07-24 15:23:07'),
(3, 1, 'Meena', 'Nirvan', 'meena@gmail.com', '8768809876', 'studies', NULL, '', 100.00, 'Books, Pen', 'dhruuf', '2025-07-24 15:27:42'),
(4, 5, 'Ashok', 'Nirvan', 'ashok@gmail.com', '2212412133', 'cash', NULL, 'Food Relief', 100.00, '', 'djfkhkeufgug', '2025-07-25 04:37:15'),
(5, 5, 'Ashok', 'Nirvan', 'ashok@gmail.com', '2212412133', 'cash', NULL, '', 100.00, '', '', '2025-07-25 04:42:56'),
(6, 5, 'Ashok', 'Nirvan', 'ashok@gmail.com', '2212412133', 'cash', NULL, '', 100.00, '', '', '2025-07-25 04:42:56'),
(7, 5, 'Ashok', 'Nirvan', 'ashok@gmail.com', '2212412133', 'cash', NULL, '', 100.00, '', '', '2025-07-25 04:42:57'),
(8, 5, 'Ashok', 'Nirvan', 'ashok@gmail.com', '2212412133', 'cash', NULL, '', 100.00, '', '', '2025-07-25 04:42:57'),
(9, 5, 'Ashok', 'Nirvan', 'ashok@gmail.com', '2212412133', 'cash', NULL, '', 100.00, '', '', '2025-07-25 04:42:57'),
(10, 4, 'neav', 'panjwani', 'meenanirvan@gmail.com', '1234', 'cash', NULL, 'Education', 100.00, '', '', '2025-07-25 05:26:59'),
(11, 4, 'neav', 'panjwani', 'meenanirvan@gmail.com', '1234', 'cash', NULL, 'Education', 100.00, '', '', '2025-07-25 05:27:01'),
(12, 4, 'neav', 'panjwani', 'meenanirvan@gmail.com', '1234', 'cloth', NULL, 'Education', 100.00, '', 'kkya bhai ', '2025-07-25 05:27:36'),
(13, 4, 'neav', 'panjwani', 'meenanirvan@gmail.com', '1234', 'cloth', NULL, 'Education', 100.00, '', 'kkya bhai ', '2025-07-25 05:27:37'),
(14, 4, 'neav', 'panjwani', 'meenanirvan@gmail.com', '1234', 'cloth', NULL, 'Education', 100.00, '', 'kkya bhai ', '2025-07-25 05:27:37'),
(15, 1, 'Meena', 'Nirvan', 'meenanirvan@gmail.com', '08169070930', 'cash', NULL, 'Education', 5.00, '', 'ghfuyuf', '2025-07-25 16:46:49'),
(16, 5, 'Ashok', 'Nirvan', 'ashoknirvan@gmail.com', '8369663943', 'food', 'self', '', 0.00, '', 'ewgrrg', '2025-07-25 17:43:11'),
(17, 5, 'Ashok', 'Nirvan', 'ashok@gmail.com', '2212412133', '', 'self', 'Other', 0.00, 'Pen, Notebooks, Art materials', 'whqfu3g', '2025-07-25 19:04:58'),
(18, 1, 'Ashok', 'Nirvan', 'ashok@gmail.com', '1234', 'Study Materials', NULL, '', 0.00, 'Books, School\r\n          bag', '', '2025-07-25 19:41:12');

-- --------------------------------------------------------

--
-- Table structure for table `donation_types`
--

CREATE TABLE `donation_types` (
  `id` int(11) NOT NULL,
  `name` varchar(100) NOT NULL,
  `created_at` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `donation_types`
--

INSERT INTO `donation_types` (`id`, `name`, `created_at`) VALUES
(1, 'Food', '2025-07-26 00:29:18'),
(2, 'Study Materials', '2025-07-26 00:29:18'),
(3, 'Cash', '2025-07-26 00:29:38'),
(4, 'Cloth', '2025-07-26 00:29:38'),
(5, 'Menstrual Hygiene Kits', '2025-07-26 00:58:01');

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
(8, 1, '103.44.117.91', 'Mumbai', 'IN', '2025-07-24 00:37:05', 'donor'),
(9, 4, 'Unknown', 'Unknown', 'Unknown', '2025-07-24 10:05:22', 'admin'),
(10, 1, '103.44.117.91', 'Mumbai', 'IN', '2025-07-24 20:36:03', 'donor'),
(11, 1, '103.44.117.91', 'Mumbai', 'IN', '2025-07-24 20:52:06', 'donor'),
(12, 1, '103.44.117.91', 'Mumbai', 'IN', '2025-07-24 20:57:11', 'donor'),
(13, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-24 21:04:12', 'admin'),
(14, 1, '103.44.117.91', 'Mumbai', 'IN', '2025-07-24 23:50:44', 'donor'),
(15, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 00:19:14', 'admin'),
(16, 5, '2409:40c0:79:bb4e:4e0:238e:845b:1d8e', 'Mumbai', 'IN', '2025-07-25 10:05:08', 'donor'),
(17, 5, '2409:40c0:79:bb4e:4e0:238e:845b:1d8e', 'Mumbai', 'IN', '2025-07-25 10:10:49', 'donor'),
(18, 4, '2409:40c0:79:bb4e:4e0:238e:845b:1d8e', 'Mumbai', 'IN', '2025-07-25 10:14:25', 'admin'),
(19, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 21:42:06', 'admin'),
(20, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 21:49:50', 'admin'),
(21, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 22:01:38', 'admin'),
(22, 1, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 22:04:49', 'donor'),
(23, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 22:14:02', 'admin'),
(24, 1, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 22:15:44', 'donor'),
(25, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 22:18:23', 'admin'),
(26, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 22:33:33', 'admin'),
(27, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 22:37:13', 'admin'),
(28, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 22:45:07', 'admin'),
(29, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 22:46:23', 'admin'),
(30, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 22:51:03', 'admin'),
(31, 5, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 23:12:39', 'donor'),
(32, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 23:22:50', 'admin'),
(33, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-25 23:38:26', 'admin'),
(34, 5, '103.44.117.91', 'Mumbai', 'IN', '2025-07-26 00:28:16', 'donor'),
(35, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-26 00:38:30', 'admin'),
(36, 4, '103.44.117.91', 'Mumbai', 'IN', '2025-07-26 00:56:30', 'admin'),
(37, 1, '103.44.117.91', 'Mumbai', 'IN', '2025-07-26 00:58:51', 'donor');

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
(4, 'manya@gmail.com', 'scrypt:32768:8:1$tGogh0UyRWi9zGHh$d68839fe3dec03f07ba8b31123d97b49bd8d6dd1f41c1654f2517b75028d8c4792b8998c3ed895e090469240b61ba4c29b79517d691c984c5e72436d0e21706f', NULL, NULL, NULL, 'Manya', 'Nirvan', NULL, 'GRACE CHS', 'admin'),
(5, 'ashok@gmail.com', 'scrypt:32768:8:1$B40V4EcuMtmo1q4v$37ebecd1b0bd8a4161b6aca373edad1867b899f771171e9c6e2ee02b9e235f9153b4c1166c4acbc083e6c50c6dffe3f590e50a7800ad987b5f5a4cc58ef82251', '', '', '', 'Ashok', 'Nirvan', '2212412133', 'grace chs', 'donor'),
(6, 'neav.panjwani@gmail.com', 'scrypt:32768:8:1$n3GKIDqCVzYdRmo9$7dfa98d9ede2cbd47532982e7ff35bbe4c04cb0a7eee39072c3729839f77c214c9b002dce5a0e59968a653163485c90efe2b4073db1ab346df0c1128808a6c8b', NULL, NULL, NULL, 'Neav', 'Panjwani', '1233343543', 'Ulhasnagar', 'admin');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `causes`
--
ALTER TABLE `causes`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `contact_messages`
--
ALTER TABLE `contact_messages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `donations`
--
ALTER TABLE `donations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `donation_types`
--
ALTER TABLE `donation_types`
  ADD PRIMARY KEY (`id`);

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
-- AUTO_INCREMENT for table `causes`
--
ALTER TABLE `causes`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `contact_messages`
--
ALTER TABLE `contact_messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `donations`
--
ALTER TABLE `donations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `donation_types`
--
ALTER TABLE `donation_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `login_logs`
--
ALTER TABLE `login_logs`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `contact_messages`
--
ALTER TABLE `contact_messages`
  ADD CONSTRAINT `contact_messages_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE SET NULL;

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
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
