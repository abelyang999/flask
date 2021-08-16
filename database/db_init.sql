CREATE TABLE IF NOT EXISTS `emp` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `username` varchar(255) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `title` varchar(255) NOT NULL,
  `department` varchar(255) NOT NULL,
  PRIMARY KEY(id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4;


INSERT INTO `emp` (`id`, `username`, `mobile`, `title`, `department`) VALUES (1, 'Ali', '0911-123456', 'SE', 'Platform');
INSERT INTO `emp` (`id`, `username`, `mobile`, `title`, `department`) VALUES (2, 'Bli', '0912-123456', 'DBA', 'Platform');
INSERT INTO `emp` (`id`, `username`, `mobile`, `title`, `department`) VALUES (3, 'Cli', '0913-123456', 'SRE', 'Platform2');
INSERT INTO `emp` (`id`, `username`, `mobile`, `title`, `department`) VALUES (4, 'Dli', '0914-123456', 'SA', 'Platform2');

