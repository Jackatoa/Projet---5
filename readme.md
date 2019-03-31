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

## Disclaimer
This program has been developped for a python formation. 
No red panda have been injured during this work.