# OpenFoodFacts

Installation library OpenFoodFacts :
sudo pip install git+https://github.com/openfoodfacts/openfoodfacts-python

Installation MySQL
Pour Python3 : pip3 install mysql-connector-python 
Modifier le paramètrage dans le fichier settings.py pour vous connecter à votre DB MySQL

Pour lancer le programme : Exécuter le Main()

Le programme est composé de 3 classes :
- DataManager : Récupère les données de la base OpenFoodFacts et les insère dans votre base SQL
- DataFeeder : Récupère les données de votre base SQL pour alimenter le programme
- MenuHandler : Gère IHM pour accèder à ses données et interagir avec le programme
