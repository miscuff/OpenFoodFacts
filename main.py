from DataManager import *
from MenuHandler import *
from DataFeeder import *

def main():
    """Main to launch the program"""
    # create_table = DataManager()
    # create_table.push_data()

    display_menu = MenuHandler()
    display_menu.show_main_menu()

    # show_data = DataFeeder()
    # show_data.get_data()

if __name__ == '__main__':
    main()
