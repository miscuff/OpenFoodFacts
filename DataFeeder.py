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
    def get_substitutes(self):
        id_sub = self.cursor.execute("""SELECT  FROM Substitues""")

    # Get the list of all categories in the database
    def get_categories(self):

    # Get the list of all products for a category
    def get_products(self, category):

    # Get the list of all substitutes for a product
    # The substitutes are the products with a better nustricore grade
    def get_substitutes(self, product):

    # Record the substitute chosen in the database
    def record_substitutes(self):
