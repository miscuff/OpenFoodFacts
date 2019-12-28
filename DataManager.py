import mysql.connector
import openfoodfacts
from queries_sql import *
from settings import *


class DataManager:

    # Initialization of the DataManager
    def __init__(self):
        """Initializing the DataManager"""
        self.conn = mysql.connector.connect(host=CONNECTOR_HOST,
                                            user=CONNECTOR_USER,
                                            password=CONNECTOR_PASSWORD,
                                            database=CONNECTOR_DATABASE,
                                            auth_plugin='mysql_'
                                                        'native_password')
        self.cursor = self.conn.cursor()
        self.create_user = CREATE_USER
        self.create_db = CREATE_DB
        self.create_categories = CREATE_CATEGORIES
        self.create_products = CREATE_PRODUCTS
        self.create_substitutes = CREATE_SUBSTITUTES
        self.category_size = CATEGORY_SIZE
        self.cat_id = []
        self.cat_name = []

    # Create table from a specify table
    def create_table(self, table):
        self.cursor.execute(table)

    # Return all the french categories in openfoodfacts database
    def get_categories(self):
        categories = openfoodfacts.facets.get_categories()
        category_id = list()
        for i in categories:
            if "fr:" in i["id"]:
                category_id.append(i["id"])
        return category_id

    # Transform a tuple in a list and return it
    def get_id_categories(self):
        self.cursor.execute("""SELECT id FROM Categories""")
        products = self.cursor.fetchall()
        id_categories = list()
        for t in products:
            id_categories.append(str(t[0]))
        return id_categories

    # Insert 5 categories in the MySQL DataBase
    def insert_categories(self):
        self.cat_id = self.get_categories()
        if not self.get_id_categories():
            self.cat_name = [s.replace('fr:', '') for s in self.cat_id]
            i = 0
            while i < self.category_size:
                try:
                    query_cat = """INSERT INTO Categories (id, name)
                    VALUES ('%s','%s')""" % (self.cat_id[i], self.cat_name[i])
                    self.cursor.execute(query_cat)
                except:
                    continue
                i += 1
            self.insert_products()
        else:
            print("Votre base est a jour")

    # Insert all the products associate to the category in the MySQL DB
    def insert_products(self):
        id_categories = self.get_id_categories()
        for j in id_categories:
            products_list = openfoodfacts.products.get_by_category(j)
            for i in products_list:
                try:
                    query_prod = """INSERT INTO Products (id, category_id,
                    product_name, nutriscore_grade, store, url_product,
                    description) VALUES ('%s','%s','%s','%s','%s','%s','%s')
                    """ % (i["id"], "{}".format(j), i["product_name"],
                           i["nutriscore_grade"], i["stores"],
                           self.get_url_product(i["id"]), i["generic_name"])
                    self.cursor.execute(query_prod)
                except:
                    continue

    # Build and Return the url of a product from the id
    def get_url_product(self, product_id):
        url = "https://world.openfoodfacts.org/api/v0/product/" + product_id
        return url

    # Call the functions and manage the MySQL DB
    def create_tables(self):
        try:
            self.create_table(self.create_categories)
            self.create_table(self.create_products)
            self.create_table(self.create_substitutes)
            self.conn.commit()
        except Exception as e:
            print("RollBack : {}".format(e))
            self.conn.rollback()

    # Insert data in the tables Categories and Products
    def insert_data(self):
        try:
            self.insert_categories()
            self.conn.commit()
        except Exception as e_cat:
            print("RollBack : {}".format(e_cat))
            self.conn.rollback()

    # Close the connector mysql
    def quit_database(self):
        self.conn.close()
