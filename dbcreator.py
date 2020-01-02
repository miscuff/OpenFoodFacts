import mysql.connector  # Import after installation requirements.txt

from settings import (HOST_ROOT, CONNECTOR_ROOT, PASSWORD_ROOT)

from queries_sql import (CREATE_USER, GRANT_PRIV, CREATE_DB)


class DBCreator:

    def __init__(self):
        """Initialize the DB with a root connector"""
        self.conn = mysql.connector.connect(host=HOST_ROOT,
                                            user=CONNECTOR_ROOT,
                                            password=PASSWORD_ROOT,
                                            auth_plugin='mysql_'
                                                        'native_password')
        self.cursor = self.conn.cursor()

    def create_user(self):
        """Create a new user for the database"""
        query_user = CREATE_USER
        query_priv = GRANT_PRIV
        self.cursor.execute(query_user)
        self.cursor.execute(query_priv)

    def create_db(self):
        """Create a DB"""
        query_db = CREATE_DB
        self.cursor.execute(query_db)

    def delete_base(self):
        """Delete the DB"""
        query_db = "DROP DATABASE OpenFoodFacts"
        self.cursor.execute(query_db)

    def quit_database(self):
        """Close the mysql Connector"""
        self.conn.close()
