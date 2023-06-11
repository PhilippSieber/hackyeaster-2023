CREATE DATABASE passwordsafe;
use passwordsafe;

CREATE USER 'readonly'@'%' IDENTIFIED BY '8ezv7QEiSHLE4wv4emmi';
GRANT SELECT,  SHOW DATABASES ON *.* TO `readonly`@`%` WITH GRANT OPTION;

CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `login` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `role` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `user`(`id`, `name`, `email`, `login`, `password`, `role`) values 
(1,'Roy Muller', 'roy@passwordsafe.com', 'roy', '$2b$12$vq5mTFBcRM8X.3bZbPovOe0bU4fKuEXs0aZ1xeRa0aEqa7G6qCteK', 'admin'),
(2,'Igor Kranic', 'igor@passwordsafe.com', 'igor', '$2b$12$vq5mTFBcRM8X.3bZbPovOe0bU4fKuEXs0aZ1xeRa0aEqa7G6qCteK', 'user');

CREATE TABLE `safe` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned NOT NULL,
  `title` varchar(100) NOT NULL,
  `url` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(400) NOT NULL,
  `comment` varchar(400) NULL,
  PRIMARY KEY (`id`),
  FOREIGN KEY (`user_id`) REFERENCES user(`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert  into `safe`(`user_id`, `title`, `url`, `username`, `password`, `comment`) values 
(1, 'The Flag', 'https://hackyeaster.com', 'hopper', '24NkWQ0iMf/zR0UNh7leZFdNhNVenCydnco9IzR9AEmTKAqFgdUvDSUdbHMloWbrgVk9bJQpcx5OuGoQS26BKg==', 'Here is the flag for this challenge'),
(1, 'gmail', 'https://gmail.com', 'hopper', ' DWnLY1zaWEaZLVOnuaaXPLj+qqpY+Fuc4oRKgxrPzCyY8S3UXtFWRqH9Brm3X9ML', 'My private gmail Account'),
(2, 'gmail', 'https://gmail.com', 'igor99', '+A1s8mrBeX7z+QbmSULk7x8ZI6ji5AS0wJVT0jRjPDs=', 'My private gmail Account'),
(2, 'M365', 'https://office.com', 'igor@passwordsafe.com', 'oNOx9yl4E0pRwnC25qdI4QxelhJfiHXfXvfrv2gNnUIzh40lPuFhg5ueZhdBkGiK', 'My office M365 account'),
(2, 'Twitter', 'https://twitter.com', 'igorTheGreat', 'ry9kHCdUkMVjTHuXQ88xPibkSfXVfIYJC7tFOmW1K1E=', 'My twitter account');