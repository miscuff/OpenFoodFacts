# OpenFoodFacts

##To use Requirements
pip3 install -r requirements.txt

###We will install
1- Library OpenFoodFacts
sudo pip3 install git+https://github.com/openfoodfacts/openfoodfacts-python

2- MySQL
sudo pip3 install mysql-connector-python 

###Manage settings
Change the parameters in the file settings.py

##How to launch the programme : 
Execute the Main()

##This program is composed of 4 Classes:
- DBCreator : Create the user and the DB
- DataManager : Get the data from OpenFoodFacts 
- DataFeeder : Get the data in your DB MySQL
- MenuHandler : Manage the IHM in the console
