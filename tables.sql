{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww34000\viewh21380\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf0 \cb2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 -- Firstly, create database schema called auto parts management system\
\
-- Create products table\
CREATE TABLE `products` (\
  `product_id` int NOT NULL AUTO_INCREMENT,\
  `name` varchar(45) NOT NULL,\
  `brand_id` int NOT NULL,\
  `price` double NOT NULL,\
  PRIMARY KEY (`product_id`),\
  KEY `fs_brand_id_idx` (`brand_id`),\
  CONSTRAINT `fs_brand_id` FOREIGN KEY (`brand_id`) REFERENCES `brand` (`brand_id`) ON UPDATE RESTRICT\
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci\
\
\--Create orders table\
CREATE TABLE `orders` (\
  `order_id` int NOT NULL AUTO_INCREMENT,\
  `customer_name` varchar(100) NOT NULL,\
  `total_price` double NOT NULL,\
  `date` datetime NOT NULL,\
  PRIMARY KEY (`order_id`)\
) ENGINE=InnoDB AUTO_INCREMENT=5880 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci\
\
--Create order_details table\
CREATE TABLE `order_details` (\
  `order_id` int NOT NULL AUTO_INCREMENT,\
  `product_id` int NOT NULL,\
  `quatity` int NOT NULL,\
  `price` double NOT NULL,\
  PRIMARY KEY (`order_id`),\
  KEY `fs_product_id_idx` (`product_id`),\
  CONSTRAINT `fs_order_id` FOREIGN KEY (`order_id`) REFERENCES `orders` (`order_id`) ON UPDATE RESTRICT,\
  CONSTRAINT `fs_product_id` FOREIGN KEY (`product_id`) REFERENCES `products` (`product_id`) ON UPDATE RESTRICT\
) ENGINE=InnoDB AUTO_INCREMENT=5880 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci\
\
-- Create brands table\
CREATE TABLE `brand` (\
  `brand_id` int NOT NULL AUTO_INCREMENT,\
  `name` varchar(45) NOT NULL,\
  PRIMARY KEY (`brand_id`)\
) ENGINE=InnoDB AUTO_INCREMENT=95 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci\
}-- 