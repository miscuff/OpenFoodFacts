"""Main to launch the program"""
from MenuHandler import *
from DataManager import *


def main():
    """Main to launch the program"""

    display_menu = MenuHandler()
    initialize_data = DataManager()

    initialize_data.create_tables()
    initialize_data.insert_data()
    initialize_data.quit_database()

    display_menu.show_main_menu()


if __name__ == '__main__':
    main()
