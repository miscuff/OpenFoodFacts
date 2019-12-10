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
        self.data_feeder = DataFeeder()

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
                self.data_feeder.get_substitutes_list()
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
            cat_list = self.data_feeder.get_categories()
            for count, element in enumerate(cat_list):
                print("{} - {} \n".format(count + 1, element))
            ans = input("Veuillez choisir une catégorie dans "
                        "la liste ci-dessus")
            ans = int(ans)
            if ans in range(0, len(cat_list) + 1):
                print("Vous avez choisi la catégorie : {}".format(cat_list
                                                                [ans - 1]))
                category_choose = cat_list[ans - 1]
                self.continue_category_menu = False
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
                self.continue_choose_category = False
                self.continue_category_menu = True
            elif ans != "":
                print("\n 3Ce n'est pas un choix valide")

    # Menu to select a product
    def choose_product(self, category):
        while self.continue_choose_product:
            prod_list = self.data_feeder.get_products(category)
            for count, element in enumerate(prod_list):
                print("{} - {} \n".format(count + 1, element))
            ans = input("Veuillez choisir un produit dans la liste ci-dessus")
            ans = int(ans)
            if ans in range(0, len(prod_list) + 1):
                print("Vous avez choisi le produit : {} \n".format(prod_list
                                                                  [ans - 1]))
                product_choose = prod_list[ans - 1]
                nutriscore_produit = self.data_feeder.\
                    get_product_nutriscore(product_choose)
                print("Le nutriscore associé à votre produit est de {}"
                      .format(nutriscore_produit))
                self.continue_product_menu = False
                self.continue_choose_product = False
                self.continue_choose_substitute = True
                self.choose_substitute(category, nutriscore_produit)
            elif ans != "":
                print("\n4 Ce n'est pas un choix valide")

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
                      "Lien : {} \n".format(sub[0], sub[1], sub[2],
                                            sub[3]))
                self.continue_choose_substitute = False
                self.record_substitute()
            else:
                self.continue_choose_substitute = False
                self.continue_main_menu = True

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

