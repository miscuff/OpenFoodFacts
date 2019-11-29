from DataManager import *


def main():
    """Main to launch the program"""
    Create_database = DataManager()
    Create_database.push_data(Create_database.create_table(
        Create_database.create_categories))

    Create_database.push_data(Create_database.insert_categories())



if __name__ == '__main__':
    main()