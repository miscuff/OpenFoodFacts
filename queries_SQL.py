"""Queries used for the program"""

#Create table Categories
CREATE_CATEGORIES = """ 
CREATE TABLE IF NOT EXISTS Categories ( 
   id VARCHAR(100) NOT NULL, 
   name VARCHAR(100) NOT NULL, 
   PRIMARY KEY(id)
   ) 
ENGINE=INNODB;"""

#Create table Products
CREATE_PRODUCTS = """ 
CREATE TABLE IF NOT EXISTS Products 
   id BIGINT NOT NULL, 
   category_id VARCHAR(100) NOT NULL,
   product_name VARCHAR(100) NOT NULL, 
   nutriscore_grade VARCHAR(1) DEFAULT NULL,
   PRIMARY KEY(id),
   CONSTRAINT fk_categories_id
    FOREIGN KEY(category_id)
    REFERENCES Categories(id)
   ) 
ENGINE=INNODB;"""

#Create table Substitutes
CREATE_SUBSTITUTES = """ 
CREATE TABLE IF NOT EXISTS Substitutes( 
   id BIGINT NOT NULL, 
   category_id VARCHAR(100) NOT NULL,
   product_name VARCHAR(100) NOT NULL, 
   nutriscore_grade VARCHAR(1) DEFAULT NULL,
   PRIMARY KEY(id),
   CONSTRAINT fk_categories_id
    FOREIGN KEY(category_id)
    REFERENCES Categories(id)
   ) 
ENGINE=INNODB;"""

