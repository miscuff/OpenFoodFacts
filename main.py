"""Main to launch the program"""
from MenuHandler import *
from DataManager import *
from DBCreator import *


def main():
    """Main to launch the program"""

    create_db = DBCreator()
    create_db.create_user()
    create_db.create_db()
    create_db.quit_database()

    initialize_data = DataManager()
    initialize_data.create_tables()
    initialize_data.insert_data()
    initialize_data.quit_database()

    display_menu = MenuHandler()
    display_menu.show_main_menu()


if __name__ == '__main__':
    main()
