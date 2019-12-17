from DataFeeder import *
from DataManager import *

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
        self.data_feeder = DataFeeder()
        self.data_manager = DataManager()

    # Starting menu
    def show_main_menu(self):
        while self.continue_main_menu:
            self.data_manager.push_data()
            print("""
            1.Quel aliment souhaitez-vous remplacer ?
            2.Retrouver mes aliments substitués
            3.Réinitialiser la base de données
            4.Exit/Quit
            """)
            ans = input("Que voulez-vous faire? ")
            if ans == "1":
                self.continue_category_menu = True
                self.show_category_menu()
            elif ans == "2":
                print("\n La liste de mes aliments substitués :")
                subs = self.data_feeder.get_substitutes_list()
                subs_list = list()
                for i in subs:
                    subs_list.append(str(i[0]))
                for count, elt in enumerate(subs_list):
                    print("{} - {}".format(count + 1, elt))
                self.show_main_menu()
            elif ans == "3":
                self.data_manager.reinitialize_base()
                print("La base a été réinitialisée")
                self.show_main_menu()
            elif ans == "4":
                print("\n Au revoir")
                self.data_manager.quit_database()
                self.continue_main_menu = False
            elif ans != "":
                print("\n Ce n'est pas un choix valide")

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
                print("\n Ce n'est pas un choix valide")

    # Menu to select a catagory
    def choose_category(self):
        while self.continue_choose_category:
            cat_list = self.data_feeder.get_categories()
            for count, element in enumerate(cat_list):
                print("{} - {}".format(count + 1, element))
            ans = input("Veuillez choisir une catégorie dans "
                        "la liste ci-dessus")
            ans = int(ans)
            if ans in range(0, len(cat_list) + 1):
                print("Vous avez choisi la catégorie : {}".format(cat_list
                                                                [ans - 1]))
                category_choose = cat_list[ans - 1]
                self.continue_category_menu = False
                self.continue_choose_category = False
                self.continue_product_menu = True
                self.show_product_menu(category_choose)
            elif ans != "":
                print("\nCe n'est pas un choix valide \n")

    # Menu to manage the products
    def show_product_menu(self, category):
        while self.continue_product_menu:
            print("""\n
            1.Sélectionner un produit
            2.Retourner à la liste des catégories
            """)
            ans = input("Que voulez-vous faire?")
            if ans == "1":
                self.continue_choose_category = False
                self.continue_choose_product = True
                self.choose_product(category)
            elif ans == "2":
                self.continue_product_menu = False
                self.continue_choose_category = True
            elif ans != "":
                print("\n Ce n'est pas un choix valide")

    # Menu to select a product
    def choose_product(self, category):
        while self.continue_choose_product:
            prod_list = self.data_feeder.get_products(category)
            if prod_list:
                for count, element in enumerate(prod_list):
                    print("{} - {}".format(count + 1, element))
                ans = \
                    input("Veuillez choisir un produit dans la liste ci-dessus")
                ans = int(ans)
                if ans in range(0, len(prod_list) + 1):
                    print("Vous avez choisi le produit : {} \n".format(
                        prod_list[ans - 1]))
                    product_choose = prod_list[ans - 1]
                    nutriscore_produit = self.data_feeder.\
                        get_product_nutriscore(product_choose)
                    print("Le nutriscore associé à votre produit est de {}"
                          .format(nutriscore_produit))
                    self.choose_substitute(category, nutriscore_produit)
                    self.continue_product_menu = False
                    self.continue_choose_product = False
                    self.continue_choose_substitute = True
                elif ans != "":
                    print("\n Ce n'est pas un choix valide")
            else:
                self.continue_choose_category = True
                self.continue_product_menu = False
                self.continue_choose_product = False

    # Menu to select a substitute
    def choose_substitute(self, category, nutriscore):
        while self.continue_choose_substitute:
            sub = self.data_feeder.get_substitutes(category, nutriscore)
            if sub:
                print("Nous avons trouvé un substitut à votre produit"
                      " avec un meilleur nutriscore \n:")
                print("Nom : {} \n"
                      "Description : {} \n"
                      "Magasin : {} \n"
                      "Lien : {} \n".format(sub[0].replace("""(""", ""),
                                            sub[1],
                                            sub[2],
                                            sub[3].replace(""")""", "")))
                self.record_substitute(sub[0])
                self.continue_choose_substitute = False
            else:
                self.continue_choose_substitute = False
                self.continue_main_menu = True

    # Menu to record the substitute
    def record_substitute(self, product_name):
        product_name = product_name.replace("""(\'""", "")
        product_name = product_name.replace("""\'""", "")
        while self.continue_record_substitute:
            ans = input("Voulez vous sauvegarder cet aliment dans "
                        " votre base de données? (Oui/Non) ")
            if ans == "Oui":
                self.data_feeder.record_substitutes(product_name)
                print("\n L'aliment a été sauvegardé")
                self.continue_record_substitute = False
                self.continue_main_menu = True
            elif ans == "Non":
                print("\n L'aliment n'a pas été sauvegardé")
                self.continue_record_substitute = False
                self.continue_main_menu = True
            elif ans != "":
                print("\n Ce n'est pas un choix valide")

