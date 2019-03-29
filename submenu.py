from zulu import Zulu
from food import Food
import random
from sqlfunc import Sqlfunc


class Submenu():
    """Contain functions from the deep end of the menu"""

    def get_a_sample(self, food):
        """Return 10 food from selected categorie"""
        rows = random.sample(S.get_all_aliments_with_categories(food), 10)
        rows.append("Regenerer la liste")
        rows.append("Retour au menu précédent")
        return rows

    def generating_query_from_criteria(self, foodobject):
        """Generate a big bad MySQL query from all selected criterias"""
        query = "SELECT nom FROM alimentsss WHERE categorie LIKE '%" + foodobject.categorie + "%' "
        if foodobject.unwantedpackaging:
            query += su.packaging_query(foodobject)
        if foodobject.wantednutritionnalvalue:
            query += su.nutrionnal_query(foodobject)
        if foodobject.unwantedallergen:
            query += su.allergen_query(foodobject)
        if foodobject.unwantedadditives:
            query += su.additives_query(foodobject)
        if foodobject.betterscore:
            query += su.score_query(foodobject)
        su.proposing_new_aliments(foodobject, query)

    def proposing_new_aliments(self, foodobject, query):
        """Propose 10 aliments with selected criterias"""
        if S.get_new_aliment_from_super_query(query):
            results = random.sample(S.get_new_aliment_from_super_query(query), 10)
            results.append("Regenerer la liste")
            z.allquestions[14].propositions = results
            cntnue = True
            while cntnue:
                z.allquestions[14].play_question()
                choice = input()
                if z.allquestions[14].check_if_choice_is_valable(choice):
                    cntnue = False
                    if int(choice) == len(z.allquestions[14].propositions):
                        su.proposing_new_aliments(foodobject, query)
                    else:
                        su.choose_or_loose(foodobject, z.allquestions[14].propositions[int(
                            choice) - 1])
        else:
            print("Aucun résultat avec les critères choisis")

    def choose_or_loose(self, foodobject, newfoodname):
        """Propose to save the found food or to go back to start"""
        cntnue = True
        newfood = Food(newfoodname, foodobject.categorie)
        while cntnue:
            print("Vous avez choisi {1}.\nNutri-Score : {2}\nUrl du produit : {3}\nSouhaitez "
                  "vous remplacer {0} par {1} ?\n"
                  "1.Oui\n2.Non je suis particulièrement déçu et souhaite revenir à "
                  "l'acceuil".format(foodobject.name, newfoodname, newfood.score[0],
                                     newfood.producturl))
            choice = input()
            if int(choice) == 1 or int(choice) == 2:
                cntnue = False
                if int(choice) == 1:
                    S.save_new_food(foodobject.name, newfoodname)

    def packaging_query(self, foodobject):
        """Generate the query from selected packaging"""
        query = []
        for x in foodobject.unwantedpackaging:
            query.append(" packaging NOT LIKE '%" + x + "%' ")
        query = "AND".join(str(x) for x in query)
        query = "AND " + query
        return query

    def nutrionnal_query(self, foodobject):
        """Generate the query from selected nutrionnal value"""
        query = "AND teneur LIKE '%" + su.get_nutrional_trad(foodobject) + "%'"
        return query

    def get_nutrional_trad(self, foodobject):
        """Trade FR to EN for query"""
        value = ""
        if "Graisse en grande" in foodobject.wantednutritionnalvalue:
            value = "fat-in-high"
        if "Graisse en faible" in foodobject.wantednutritionnalvalue:
            value = "fat-in-low"
        if "Sucre en grande quantité" in foodobject.wantednutritionnalvalue:
            value = "sugars-in-high"
        if "Sucre en faible quantité" in foodobject.wantednutritionnalvalue:
            value = "sugars-in-low"
        if "Protéines en grande quantité" in foodobject.wantednutritionnalvalue:
            value = "salt-in-high"
        if "Protéines en faible quantité" in foodobject.wantednutritionnalvalue:
            value = "salt-in-low"
        return value

    def allergen_query(self, foodobject):
        """Generate the query from selected allergen"""
        query = "AND allergen NOT LIKE " + "'%" + "".join(foodobject.unwantedallergen) + "%'"
        return query

    def additives_query(self, foodobject):
        """Generate the query from selected additives"""
        query = "AND additifs NOT LIKE " + "'%" + "".join(foodobject.unwantedadditives) + "%'"
        return query

    def score_query(self, foodobject):
        """Generate the query from selected nutriscore"""
        scorelst = ["F", "E", "D", "C", "B", "A"]
        i = 0
        while i < scorelst.index(foodobject.score[0]):
            scorelst.remove(scorelst[i])
            i += 1
        query = []
        for x in scorelst:
            query.append(" score LIKE '%" + x + "%'")
        query = "OR".join(str(x) for x in query)
        query = "AND (" + query + ")"
        return query


z = Zulu()
S = Sqlfunc()
su = Submenu()
