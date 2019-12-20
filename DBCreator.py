"""Create the DB """
import mysql.connector
from settings import *
from queries_sql import *


class DBCreator:

    # Initialize the DB with a root connector
    def __init__(self):
        self.conn = mysql.connector.connect(host=HOST_ROOT,
                                            user=CONNECTOR_ROOT,
                                            password=PASSWORD_ROOT,
                                            auth_plugin='mysql_native_password')
        self.cursor = self.conn.cursor()

    # Create a new user for the database
    def create_user(self):
        query_user = CREATE_USER
        query_priv = GRANT_PRIV
        self.cursor.execute(query_user)
        self.cursor.execute(query_priv)

    # Create a DB
    def create_db(self):
        query_db = CREATE_DB
        self.cursor.execute(query_db)

    # Delete the DB
    def delete_base(self):
        query_db = "DROP DATABASE OpenFoodFacts"
        self.cursor.execute(query_db)

    # Close the mysql Connector
    def quit_database(self):
        self.conn.close()