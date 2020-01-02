"""Queries used for the program"""
from settings import (CONNECTOR_USER, CONNECTOR_HOST, CONNECTOR_DATABASE,
                      CONNECTOR_PASSWORD)

# Create User
CREATE_USER = """
CREATE USER IF NOT EXISTS
'%s'@'%s' IDENTIFIED BY '%s'; """ % (CONNECTOR_USER, CONNECTOR_HOST,
                                     CONNECTOR_PASSWORD)

# Grant Privileges to the user
GRANT_PRIV = """
GRANT ALL PRIVILEGES ON %s.* TO '%s'@'%s';""" % (CONNECTOR_DATABASE,
                                                 CONNECTOR_USER,
                                                 CONNECTOR_HOST)
# Create DataBase
CREATE_DB = """
CREATE DATABASE IF NOT EXISTS %s;""" % CONNECTOR_DATABASE

# Create table Categories
CREATE_CATEGORIES = """
CREATE TABLE IF NOT EXISTS Categories (
   id VARCHAR(100) NOT NULL,
   name VARCHAR(100) NOT NULL,
   PRIMARY KEY(id)
   )
ENGINE=INNODB;"""

# Create table Products
CREATE_PRODUCTS = """
CREATE TABLE IF NOT EXISTS Products (
   id BIGINT NOT NULL,
   category_id VARCHAR(100) NOT NULL,
   product_name VARCHAR(100) NOT NULL,
   nutriscore_grade VARCHAR(1) DEFAULT NULL,
   store VARCHAR(50) DEFAULT NULL,
   url_product VARCHAR(100) NOT NULL,
   description TEXT DEFAULT NULL,
   PRIMARY KEY(id),
   CONSTRAINT fk_categories_id
    FOREIGN KEY(category_id)
    REFERENCES Categories(id)
   )
ENGINE=INNODB;"""

# Create table Substitutes
CREATE_SUBSTITUTES = """
CREATE TABLE IF NOT EXISTS Substitutes (
   id INT NOT NULL AUTO_INCREMENT,
   product_id BIGINT NOT NULL,
   substitute_id BIGINT NOT NULL,
   PRIMARY KEY(id),
   CONSTRAINT fk_products_id
    FOREIGN KEY(product_id)
    REFERENCES Products(id),
    CONSTRAINT fk_substitutes_id
    FOREIGN KEY(substitute_id)
    REFERENCES Products(id)
   )
ENGINE=INNODB;"""
