from DataFeeder import *

class MenuHandler:

    # Initialisation of the Boolean for the different menus
    def __init__(self):
        self.continue_main_menu = True
        self.continue_category_menu = True
        self.continue_product_menu = True
        self.continue_choose_category = True
        self.continue_choose_product = True
        self.continue_choose_substitute = True
        self.continue_record_substitute = True

    # Starting menu
    def show_main_menu(self):
        while self.continue_main_menu:
            print("""
            1.Quel aliment souhaitez-vous remplacer ?
            2.Retrouver mes aliments substitués
            3.Exit/Quit
            """)
            ans = input("Que voulez-vous faire? ")
            if ans == "1":
                self.continue_category_menu = True
                self.show_category_menu()
            elif ans == "2":
                print("\n La liste de mes aliments substitués :")
            elif ans == "3":
                print("\n Au revoir")
                self.continue_main_menu = False
            elif ans != "":
                print("\n 1Ce n'est pas un choix valide")

    # Menu to manage the categories
    def show_category_menu(self):
        while self.continue_category_menu:
            print("""
            1.Sélectionner une catégorie
            2.Retourner au menu principal
            """)
            ans = input("Que voulez-vous faire? ")
            if ans == "1":
                print("\n La liste des catégories:")
                self.continue_main_menu = False
                self.continue_choose_category = True
                self.choose_category()
            elif ans == "2":
                self.continue_category_menu = False
                self.continue_main_menu = True
            elif ans != "":
                print("\n2 Ce n'est pas un choix valide")

    # Menu to select a catagory
    def choose_category(self):
        while self.continue_choose_category:
            ans = input("Veuillez choisir une catégorie dans "
                        "la liste ci-dessus")
            if ans == "cat":
                self.continue_category_menu = False
                self.continue_product_menu = True
                self.show_product_menu()
            elif ans != "":
                print("\n23 Ce n'est pas un choix valide")

    # Menu to manage the products
    def show_product_menu(self):
        while self.continue_product_menu:
            print("""\n
            1.Sélectionner un produit
            2.Retourner à la liste des catégories
            """)
            ans = input("Que voulez-vous faire?")
            if ans == "1":
                self.continue_choose_category = False
                self.continue_choose_product = True
                self.choose_product()
            elif ans == "2":
                self.continue_product_menu = False
                self.continue_choose_category = False
                self.continue_category_menu = True
            elif ans != "":
                print("\n 3Ce n'est pas un choix valide")

    # Menu to select a product
    def choose_product(self):
        while self.continue_choose_product:
            ans = input("Veuillez choisir un aliment dans la liste ci-dessus")
            if ans == "aliment":
                self.continue_product_menu = False
                self.continue_choose_product = False
                self.continue_choose_substitute = True
                self.choose_substitute()
            elif ans != "":
                print("\n4 Ce n'est pas un choix valide")

    # Menu to select a substitute
    def choose_substitute(self):
        while self.continue_choose_substitute:
            print("Ci-dessous la liste des substituts à ce produit"
                        "avec un meilleur nutriscore grade")
            ans = input("Veuillez choisir un des substituts")
            if ans == "sub":
                self.continue_choose_substitute = False
                self.continue_record_substitute = True
                self.record_substitute()
            elif ans != "":
                print("\n4 Ce n'est pas un choix valide")

    # Menu to record the substitute
    def record_substitute(self):
        while self.continue_record_substitute:
            ans = input("Voulez vous sauvegarder cet aliment dans "
                        " votre base de données? (Oui/Non) ")
            if ans == "Oui":
                print("\n L'aliment a été sauvegardé")
                self.continue_record_substitute = False
                self.continue_main_menu = True
            elif ans == "Non":
                print("\n L'aliment n'a pas été sauvegardé")
                self.continue_record_substitute = False
                self.continue_main_menu = True
            elif ans != "":
                print("\n 5Ce n'est pas un choix valide")
