import json
import requests
import mysql.connector
from sqlfunc import Sqlfunc


class Generatingdb:
    """Contain all the function to generate Database"""
    S = Sqlfunc()

    def insert_aliment_record(self, url):
        """Insert records for aliments"""
        G = Generatingdb()
        r = requests.get(url)
        r2 = json.loads(r.text)
        r3 = r2["product"]
        r4 = r3["nutriments"]
        if r3.get("product_name_fr") != "null" and r3.get("product_name_fr") != "None" and \
                r3.get("product_name_fr") != None and r3.get("product_name_fr") != "":
            Generatingdb.S.insert_record("alimentsss",
                                         json.dumps(r3.get("product_name_fr"),
                                                    ensure_ascii=False).encode('utf8'),
                                         json.dumps(r3.get("allergens"),
                                                    ensure_ascii=False).encode('utf8'),
                                         json.dumps(r3.get("nutrient_levels_tags"),
                                                    ensure_ascii=False).encode('utf8'),
                                         json.dumps(r3.get("additives_tags"),
                                                    ensure_ascii=False).encode('utf8'),
                                         json.dumps(r3.get("packaging_tags"),
                                                    ensure_ascii=False).encode('utf8'),
                                         json.dumps(r3.get("categories_hierarchy"),
                                                    ensure_ascii=False).encode('utf8'),
                                         json.dumps(G.get_nutriscore(r4.get("nutrition-score-fr")),
                                                    ensure_ascii=False).encode('utf8'),
                                         json.dumps(r3.get("image_url"),
                                                    ensure_ascii=False).encode('utf8'),
                                         json.dumps(r3.get("stores"),
                                                    ensure_ascii=False).encode('utf8'),
                                         url
                                         )

    def distrib_url(self):
        """For each categorie url, take 200 aliments"""
        G = Generatingdb()
        urlsdescategories = ["https://world.openfoodfacts.org/category/snacks",
                             "https://world.openfoodfacts.org/category/meals",
                             "https://world.openfoodfacts.org/category/cereals-and-potatoes",
                             "https://world.openfoodfacts.org/category/meats",
                             "https://world.openfoodfacts.org/category/cheeses",
                             "https://world.openfoodfacts.org/category/desserts",
                             "https://world.openfoodfacts.org/category/frozen-foods"]
        for url in urlsdescategories:
            i = 0
            while i < 10:
                newurl = url + "/" + str(i) + ".json"
                codes = []
                r = requests.get(newurl)
                r2 = json.loads(r.text)
                r3 = r2["products"]
                for keys in r3:
                    codes.append(keys["code"])
                for code in codes:
                    G.insert_aliment_record(G.get_product_url_from_code(code))
                i += 1

    def get_product_url_from_code(self, code):
        """return the url from the code"""
        return "https://fr.openfoodfacts.org/api/v0/produit/" + code + ".json"

    def get_nutriscore(self, score):
        """Change the number score to letter score"""
        if score is not None:
            score = int(score)
            if score == -1:
                return "A"
            elif score >= 0 and score <= 2:
                return "B"
            elif score >= 3 and score <= 10:
                return "C"
            elif score >= 11 and score <= 18:
                return "D"
            elif score >= 19:
                return "E"
            else:
                return "Ce produit n'est pas noté"
        else:
            return "Ce produit n'est pas noté"
