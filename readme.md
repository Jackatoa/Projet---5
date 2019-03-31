# BetterFood

BetterFood is script using the openfoodfacts.org API to propose food substitutes.

## Installation

First you need the access to a MySQL database, you can set the host, the username and the password in the file sqlfunc.py. Be sure to change the value at the line 7, 8, 9 and 22, 23, 24. Then simply run the script from the main file and you are good to go !

```python
    mydb2 = mysql.connector.connect(
        host="yourhost",
        user="yourusername",
        passwd="yourpassword",
        charset="utf8",
        use_unicode=True
    )
```

## Usage
Simply enter the number corresponding to your choice.
```
Bienvenue sur ce logiciel. Que voulez vous faire ?
1.Choisir un aliment.
2.Voir les aliments substitués.
3.Regenerer la base de données.
4.Supprimer les aliments substitués.
5.Quitter le logiciel.

```

## Adding categories for search
To add a categorie for search, you have to manually add an element to the list questionspropositions in questions.py. Be sure to add the categorie before "Retour au menu précédent" and to add a comma after the newcategorie.
```Python
"""Before :"""
questionspropositions = [
        ["Choisir un aliment.", "Voir les aliments substitués.", "Regenerer la base de données.",
         "Supprimer les aliments substitués.", "Quitter le logiciel."],
        ["Snacks", "Meals", "Cereals", "Meats", "Cheeses", "Retour au menu précédent"],
        [],

"""After :"""
questionspropositions = [
        ["Choisir un aliment.", "Voir les aliments substitués.", "Regenerer la base de données.",
         "Supprimer les aliments substitués.", "Quitter le logiciel."],
        ["Snacks", "Meals", "Cereals", "Meats", "Cheeses", "NEWCATEGORIE", "Retour au menu précédent"],
        [],
```

## Adding categories for the database
To add a categorie for the database, you have to manually add an element to the list categoriesurl in generatingdb.py. Be sure to add a correct url and a comma before the url element.
```Python
"""Before :"""
categoriesurl = ["https://world.openfoodfacts.org/category/snacks",
                             "https://world.openfoodfacts.org/category/meals",
                             "https://world.openfoodfacts.org/category/cereals-and-potatoes",
                             "https://world.openfoodfacts.org/category/meats",
                             "https://world.openfoodfacts.org/category/cheeses",
                             "https://world.openfoodfacts.org/category/desserts",
                             "https://world.openfoodfacts.org/category/frozen-foods"
                             ]

"""After :"""
categoriesurl = ["https://world.openfoodfacts.org/category/snacks",
                             "https://world.openfoodfacts.org/category/meals",
                             "https://world.openfoodfacts.org/category/cereals-and-potatoes",
                             "https://world.openfoodfacts.org/category/meats",
                             "https://world.openfoodfacts.org/category/cheeses",
                             "https://world.openfoodfacts.org/category/desserts",
                             "https://world.openfoodfacts.org/category/frozen-foods",
                             "https://world.openfoodfacts.org/category/NEWCATEGORIE"
                             ]
```
## Disclaimer
This program has been developped for a python formation. 
No red panda have been injured during this work.