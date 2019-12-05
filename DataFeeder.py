import mysql.connector
# import openfoodfacts
from queries_sql import *


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


    # Get the list of all categories in the database
    def get_categories(self):
        query_cat = """SELECT name FROM Categories"""
        self.cursor.execute(query_cat)

    # Get the list of all products for a category
    def get_products(self, category):
        query_prod = """SELECT Products.product_name AS nom
        FROM Products
        INNER JOIN Categories
            ON Products.category_id = Categories.id
        where Categories.name = '%s' """ % category
        self.cursor.execute(query_prod)

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

    # Record the substitute chosen in the database
    def record_substitutes(self):
