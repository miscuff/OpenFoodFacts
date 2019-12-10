import mysql.connector
import openfoodfacts
from queries_sql import *
import random


class DataFeeder:

    def __init__(self):
        """Initializing the DataManager"""
        self.conn = mysql.connector.connect(host="localhost", user="ocr",
                               password="password", database="OpenFoodFacts",
                               auth_plugin='mysql_native_password')
        self.cursor = self.conn.cursor()

    # Get the list of substitutes in mysql
    def get_substitutes_list(self):
        query_sub_list = """SELECT Products.product_name AS nom,
        Products.description AS Description,
        Products.store AS Magasin,
        Products.url_product AS Lien
        FROM Substitutes
        INNER JOIN Products
            ON Substitutes.product_id = Products.id """
        self.cursor.execute(query_sub_list)
        substitutes = self.cursor.fetchall()
        return substitutes

    # Get the list of all categories in the database
    def get_categories(self):
        query_cat = """SELECT name FROM Categories"""
        self.cursor.execute(query_cat)
        categories = self.cursor.fetchall()
        categories_list = list()
        for i in categories:
            categories_list.append(str(i[0]))
        categories_list = random.sample(categories_list, 10)
        return categories_list

    # Get the list of all products for a category
    def get_products(self, category):
        query_prod = """SELECT Products.product_name AS nom
        FROM Products
        INNER JOIN Categories
            ON Products.category_id = Categories.id
        where Categories.name = '%s' """ % category
        self.cursor.execute(query_prod)
        products = self.cursor.fetchall()
        products_list = list()
        for i in products:
            products_list.append(str(i[0]))
        products_list = random.sample(products_list, 5)
        return products_list

    def get_product_nutriscore(self, product):
        query_prod = """SELECT Products.nutriscore_grade
                FROM Products
                where Products.product_name = '%s' """ % product
        self.cursor.execute(query_prod)
        product = self.cursor.fetchall()
        product_nutriscore = str(product[0][0])
        return product_nutriscore

    # The substitutes are the products with a better nustricore grade
    def get_substitutes(self, category, nutriscore_product):
        query_sub = """SELECT Products.product_name AS nom,
        Products.description AS Description,
        Products.store AS Magasin,
        Products.url_product AS Lien
        FROM Products
        INNER JOIN Categories
            ON Products.category_id = Categories.id 
        where Categories.name = '%s' 
        AND Products.nutriscore_grade < '%s' """ \
                    % (category, nutriscore_product)
        self.cursor.execute(query_sub)
        substitutes = self.cursor.fetchall()
        substitutes_list = list()
        for i in substitutes:
            substitutes_list.append(str(i))
        substitute = random.sample(substitutes_list, 1)
        substitute = substitute[0].split(",")
        return substitute

    # Record the substitute chosen in the database
    # def record_substitutes(self):
    def get_data(self):
        try:
            # substitute_list = self.get_substitutes_list()
            # print(substitute_list)
            cat_list = self.get_categories()
            print(cat_list)
            # product_charcuterie = self.get_products("charcuteries-diverses")
            # print(product_charcuterie)
            # sub_lardons = self.get_substitutes("charcuteries-diverses", "e")
            # print(sub_lardons)
            self.conn.commit()
        except:
            self.conn.rollback()
            print("Error as occurred, Rollback")
        self.conn.close()