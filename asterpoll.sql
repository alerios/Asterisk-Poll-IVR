CREATE TABLE `question` (
  `id_question` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `audio_filename` varchar(256) COLLATE utf8_unicode_ci  NOT NULL DEFAULT 'beep',
  `options` varchar(256) COLLATE utf8_unicode_ci NOT NULL DEFAULT '1,2',
  PRIMARY KEY (`id_question`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


CREATE TABLE `answer` (
  `id_answer` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `recordID` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `id_question` int(11) DEFAULT NULL,
  `callerid` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `answer` varchar(16) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id_answer`),
  KEY `IDX_47860B054FCEFE48` (`id_question`),
  CONSTRAINT `FK_47860B054FCEFE48` FOREIGN KEY (`id_question`) REFERENCES `question` (`id_question`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

CREATE TABLE `log` (
  `id_log` int(11) NOT NULL AUTO_INCREMENT,
  `date` datetime NOT NULL,
  `asteriskID` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  `message` varchar(256) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id_log`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci; 
