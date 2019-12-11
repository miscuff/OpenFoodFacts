"""Settings used for the program"""

#Choose the number of categories in the DB MySQL
CATEGORY_SIZE = 50

#Change the connector for MySQL
CONNECTOR = """host="localhost", user="ocr", password="password", 
database="OpenFoodFacts", auth_plugin='mysql_native_password'"""