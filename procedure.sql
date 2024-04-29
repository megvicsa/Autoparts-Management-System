{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fmodern\fcharset0 CourierNewPSMT;}
{\colortbl;\red255\green255\blue255;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c100000\c100000\c100000;\cssrgb\c0\c0\c0;}
\margl1440\margr1440\vieww34000\viewh21380\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf0 \cb2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 USE \cb2 \outl0\strokewidth0 CS348-Information-Systems\cb2 \outl0\strokewidth0 \strokec3 ;\
DROP PROCEDURE IF EXISTS GetTotalSalesPerDay;\
DROP PROCEDURE IF EXISTS GetTopSellingProducts;\
DROP PROCEDURE IF EXISTS GetAverageOrderValue;\
DELIMITER //\
\
CREATE PROCEDURE GetTotalSalesPerDay()\
BEGIN\
    SELECT DATE(timestamp) AS date, SUM(total_price) AS total_sales \
    FROM \'91CS348-Information-Systems.orders \
    GROUP BY DATE(timestamp);\
END //\
\
CREATE PROCEDURE GetTopSellingProducts()\
BEGIN\
    SELECT p.name, COUNT(*) AS total_orders\
    FROM \cb2 \outl0\strokewidth0 \'91CS348-Information-Systems.order_details\cb2 \outl0\strokewidth0 \strokec3  od\
    JOIN \cb2 \outl0\strokewidth0 \'91CS348-Information-Systems.products\cb2 \outl0\strokewidth0 \strokec3  p ON od.product_id = p.product_id\
    GROUP BY p.product_id\
    ORDER BY total_orders DESC\
    LIMIT 10;\
END //\
\
CREATE PROCEDURE GetAverageOrderValue()\
BEGIN\
    SELECT AVG(total_price) AS avg_order_value\
    FROM \cb2 \outl0\strokewidth0 \'91CS348-Information-Systems\cb2 \outl0\strokewidth0 \strokec3 .orders;\
END //\
\
DELIMITER ;\
}