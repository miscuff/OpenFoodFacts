import mysql.connector
import openfoodfacts
from queries_sql import *


class DataManager:

    def __init__(self):
        """Initializing the DataManager"""
        self.conn = mysql.connector.connect(host="localhost", user="ocr",
                               password="password", database="OpenFoodFacts",
                               auth_plugin='mysql_native_password')
        self.cursor = self.conn.cursor()
        self.create_categories = CREATE_CATEGORIES
        self.create_products = CREATE_PRODUCTS
        self.create_substitutes = CREATE_SUBSTITUTES
        self.cat_id = []
        self.cat_name = []

    def create_table(self, table):
        self.cursor.execute(table)

    def get_categories(self):
        categories = openfoodfacts.facets.get_categories()
        category_id = list()
        for i in categories:
            if "fr:" in i["id"]:
                category_id.append(i["id"])
        return category_id

    def get_products(self, category_id):
        products_list = openfoodfacts.products.get_by_category(category_id)
        return products_list

    def insert_categories(self):
        self.cat_id = self.get_categories()
        self.cat_name = [s.replace('fr:', '') for s in self.cat_id]
        i = 0
        while i < 5:
            query_cat = """INSERT INTO Categories (id, name) 
            VALUES ('%s','%s')""" % (self.cat_id[i], self.cat_name[i])
            self.cursor.execute(query_cat)
            i += 1

    def insert_products(self, category_id):
        products_list = self.get_products(category_id)
        for i in products_list:
            try:
                query_prod = """INSERT INTO Produits (id, categorie_id, 
                product_name, nutriscore_grade, store, url_product, 
                description) VALUES ('%s','%s','%s','%s','%s','%s','%s') """ \
                             % (i["id"], category_id, i["product_name"],
                                i["nutriscore_grade"], i["stores"],
                                self.get_url_product(i["id"]),
                                i["generic_name"])
                self.cursor.execute(query_prod)
            except KeyError:
                query_prod = """INSERT INTO Produits (id, categorie_id, 
                product_name, store, url_product, 
                description) VALUES ('%s','%s','%s','%s','%s','%s') """ \
                             % (i["id"], category_id, i["product_name"],
                                i["stores"],
                                self.get_url_product(i["id"]),
                                i["generic_name"])
                self.cursor.execute(query_prod)
                continue

    def get_url_product(self, product_id):
        url = "https://world.openfoodfacts.org/api/v0/product/" + product_id
        return url

    def push_data(self, method):
        try:
            method()
            self.conn.commit()
            print("Inserted", self.cursor.rowcount, "row(s) of data.")
        except:
            self.conn.rollback()
            print("Error as occurred, Rollback")
        self.conn.close()

    #Récupérer les id catlogues stockées dans la base de données
    # afin de trouver les produits correspondants