import mysql.connector
import openfoodfacts
from queries_sql import *
from settings import *


class DataManager:

    # Initialization of the DataManager
    def __init__(self):
        """Initializing the DataManager"""
        self.conn = mysql.connector.connect(CONNECTOR)
        self.cursor = self.conn.cursor()
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
        self.cat_name = [s.replace('fr:', '') for s in self.cat_id]
        i = 0
        while i < self.category_size:
            try:
                query_cat = """INSERT INTO Categories (id, name) 
                VALUES ('%s','%s')""" % (self.cat_id[i], self.cat_name[i])
                # print("Ajout de la catégorie {} dans la DB"
                #       .format(self.cat_name[i]))
                self.cursor.execute(query_cat)
            except Exception:
                print("la catégorie {} a déjà été créée "
                      .format(self.cat_name[i]))
            i += 1
        print("Inserted", self.cursor.rowcount, "row(s) of data.")

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
        print("Inserted", self.cursor.rowcount, "row(s) of data.")

    # Build and Return the url of a product from the id
    def get_url_product(self, product_id):
        url = "https://world.openfoodfacts.org/api/v0/product/" + product_id
        return url

    # Call the functions and manage the MySQL DB
    def push_data(self):
        try:
            self.create_table(self.create_categories)
            self.create_table(self.create_products)
            self.create_table(self.create_substitutes)

            self.insert_categories()
            self.insert_products()

            self.conn.commit()
        except Exception as e:
            print("RollBack : {}".format(e))
            self.conn.rollback()

        self.conn.close()
