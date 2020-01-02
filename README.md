# OpenFoodFacts
Program to get the products in the public database OpenFoodFacts and find an
other product with a better nutriscore

## Before running the program
It needs to launch this instructions below in the terminal 

### Requirements
**pip3 install -r requirements.txt**

Requirements will install :
* MySQL conector python 8.0.18
* git+https://github.com/openfoodfacts/openfoodfacts-python

### Manage settings
Change the parameters in the file settings.py

## How to run the program
Execute the Main()

## This program is composed of 4 Classes:
- DBCreator : Create the user and the DB
- DataManager : Get the data from OpenFoodFacts 
- DataFeeder : Get the data in your DB MySQL
- MenuHandler : Manage the IHM in the console
