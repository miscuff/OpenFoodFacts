"""Create the DB """
import mysql.connector
from settings import *
from queries_sql import *


class DBCreator:

    def __init__(self):
        self.conn = mysql.connector.connect(host=HOST_ROOT,
                                            user=CONNECTOR_ROOT,
                                            password=PASSWORD_ROOT,
                                            auth_plugin='mysql_native_password')
        self.cursor = self.conn.cursor()

    def create_user(self):
        query_user = CREATE_USER
        query_priv = GRANT_PRIV
        self.cursor.execute(query_user)
        self.cursor.execute(query_priv)

    def create_db(self):
        query_db = CREATE_DB
        self.cursor.execute(query_db)

    def delete_base(self):
        query_db = "DROP DATABASE OpenFoodFacts"
        self.cursor.execute(query_db)

    def quit_database(self):
        self.conn.close()