"""Main to launch the program"""
from MenuHandler import *
from DataManager import *
from DBCreator import *


def main():
    """Main to launch the program"""

    # Initialize the DB when launching the program
    create_db = DBCreator()
    create_db.create_user()
    create_db.create_db()
    create_db.quit_database()

    # Fill in The DB just created with data from OpenFoodFacts
    initialize_data = DataManager()
    initialize_data.create_tables()
    initialize_data.insert_data()
    initialize_data.quit_database()

    # Launch the menu to interact with the program
    display_menu = MenuHandler()
    display_menu.show_main_menu()


if __name__ == '__main__':
    main()
