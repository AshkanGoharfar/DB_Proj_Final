
SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE `account_system_info` (
  `p_id` int(11) NOT NULL,
  `username` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_day` datetime NOT NULL DEFAULT current_timestamp(),
  `budget` int(16) DEFAULT NULL,
  `First_name` varchar(255) DEFAULT NULL,
  `Last_name` varchar(255) DEFAULT NULL,
  `Phone` varchar(30) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  `user_type` varchar(30) DEFAULT NULL,
  `uni_job` varchar(80) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `books` (
  `b_id` int(11) NOT NULL,
  `b_title` varchar(255) DEFAULT NULL,
  `b_category` varchar(60) DEFAULT NULL,
  `b_num_of_pages` int(15) DEFAULT NULL,
  `b_price` int(60) DEFAULT NULL,
  `pub_id` int(11) NOT NULL,
  `b_author` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `borrow_history` (
  `borr_id` int(11) NOT NULL,
  `b_id` int(11) NOT NULL,
  `limit_days` int(11) DEFAULT NULL,
  `borr_cost` int(11) DEFAULT NULL,
  `isbacked` int(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `log_history` (
  `p_id` int(11) NOT NULL,
  `changed_attribute` varchar(255) DEFAULT NULL,
  `transaction` varchar(100) DEFAULT NULL,
  `timestamp` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `publisher` (
  `pub_id` int(11) NOT NULL,
  `pub_address` varchar(255) DEFAULT NULL,
  `pub_website` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



ALTER TABLE `account_system_info`
  ADD PRIMARY KEY (`p_id`),
  ADD UNIQUE KEY `Address` (`Address`),
  ADD UNIQUE KEY `Phone` (`Phone`);


ALTER TABLE `books`
  ADD PRIMARY KEY (`b_id`),
  ADD KEY `pub_id` (`pub_id`) USING BTREE;


ALTER TABLE `borrow_history`
  ADD PRIMARY KEY (`borr_id`),
  ADD KEY `p_id` (`p_id`),
  ADD KEY `b_id` (`b_id`);


ALTER TABLE `log_history`
  ADD KEY `p_id` (`p_id`);


ALTER TABLE `publisher`
  ADD PRIMARY KEY (`pub_id`);


ALTER TABLE `account_system_info`
  MODIFY `p_id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `books`
  MODIFY `b_id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `borrow_history`
  MODIFY `borr_id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `publisher`
  MODIFY `pub_id` int(11) NOT NULL AUTO_INCREMENT;


ALTER TABLE `borrow_history`
  ADD CONSTRAINT `p_id` FOREIGN KEY (`p_id`) REFERENCES `account_system_info` (`p_id`);
COMMIT;



ALTER TABLE `books`
  ADD CONSTRAINT `pub_id` FOREIGN KEY (`pub_id`) REFERENCES `publisher` (`pub_id`);
COMMIT;



