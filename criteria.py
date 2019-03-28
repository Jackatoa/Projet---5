from zulu import Zulu
from submenu import Submenu
from sqlfunc import Sqlfunc
from food import Food


class Criteria():
    """Contains the main submenu category"""

    def choosing_categorie(self):
        """Propose the categories to the users"""
        cntnue = True
        while cntnue:
            z.allquestions[1].play_question()
            choice = input()
            if z.allquestions[1].check_if_choice_is_valable(choice):
                cntnue = False
                if int(choice) < len(z.allquestions[1].propositions) - 1:
                    c.choosing_food(z.allquestions[1].propositions[int(choice)])

    def choosing_food(self, food):
        """Propose food from the choosen categorie"""
        cntnue = True
        while cntnue:
            z.allquestions[2].propositions = su.get_a_sample(food)
            z.allquestions[2].play_question()
            choice = input()
            if z.allquestions[2].check_if_choice_is_valable(choice):
                cntnue = False
                if int(choice) < len(z.allquestions[2].propositions) - 2:
                    newfood = Food(z.allquestions[2].propositions[int(choice)], food)
                    c.choosing_criteria(newfood, food)
                if int(choice) == 10:
                    c.choosing_food(food)
                if int(choice) == 11:
                    c.choosing_categorie()

    def nutritionnal_value(self, foodobject, food):
        """Propose nutrionnal values choices"""
        cntnue = True
        if not foodobject.wantednutritionnalvalue:
            while cntnue:
                z.allquestions[7].play_question()
                choice = input()
                if z.allquestions[7].check_if_choice_is_valable(choice):
                    cntnue = False
                    if int(choice) == len(z.allquestions[7].propositions) - 1:
                        c.choosing_criteria(foodobject, food)
                    else:
                        foodobject.wantednutritionnalvalue.append(
                            z.allquestions[7].propositions[int(choice)])
                        foodobject.numberofcriteria += 1
                        c.choosing_criteria(foodobject, food)
        else:
            c.choosing_another_nutrionnal_value(foodobject, food)

    def choosing_another_nutrionnal_value(self, foodobject, food):
        """Check if the user want to change his nutritionnal value criteria"""
        cntnue = True
        while cntnue:
            z.allquestions[11].play_question()
            choice = input()
            if z.allquestions[11].check_if_choice_is_valable(choice):
                cntnue = False
                if int(choice) == 0:
                    foodobject.wantednutritionnalvalue = []
                    foodobject.numberofcriteria -= 1
                    c.nutritionnal_value(foodobject, food)
                else:
                    c.choosing_criteria(foodobject, food)

    def choosing_criteria(self, foodobject, food):
        """Propose criterias for comparaison"""
        cntnue = True
        while cntnue:
            z.allquestions[3].play_question()
            choice = input()
            if z.allquestions[3].check_if_choice_is_valable(choice):
                if foodobject.numberofcriteria == 0 and int(choice) == 6:
                    print("Vous n'avez actuellement choisi aucun critère\n")
                else:
                    cntnue = False
                    if int(choice) == 0:
                        c.packaging(foodobject, food)
                    if int(choice) == 1:
                        c.nutritionnal_value(foodobject, food)
                    if int(choice) == 2:
                        c.allergen(foodobject, food)
                    if int(choice) == 3:
                        c.additives(foodobject, food)
                    if int(choice) == 4:
                        print("Le critère Nutri-Score a bien été ajouté")
                        c.nutri_score(foodobject, food)
                    if int(choice) == 5:
                        c.choosing_food(food)
                    if foodobject.numberofcriteria > 0 and int(choice) == 6:
                        su.generating_query_from_criteria(foodobject)

    def packaging(self, foodobject, food):
        """Check if the selected food have packaging"""
        if foodobject.packaging:
            if foodobject.packaging[0] != "null" and foodobject.packaging[0] != "":
                foodobject.clean_list()
                c.choosing_packaging(foodobject, food)
            else:
                print("Il n'y a pas de conditionnement enregistré pour cet objet")
                c.choosing_criteria(foodobject, food)
        else:
            print("Il n'y a pas de conditionnement enregistré pour cet objet")
            c.choosing_criteria(foodobject, food)

    def choosing_packaging(self, foodobject, food):
        """Propose packaging criteria from selected food"""
        z.allquestions[9].propositions = foodobject.packaging
        cntnue = True
        while cntnue:
            z.allquestions[9].play_question()
            choice = input()
            if z.allquestions[9].check_if_choice_is_valable(choice):
                if foodobject.packaging[int(choice)] not in foodobject.unwantedpackaging:
                    cntnue = False
                    foodobject.unwantedpackaging.append(foodobject.packaging[int(choice)])
                    foodobject.numberofcriteria += 1
                    if len(z.allquestions[9].propositions) > 1 and not \
                            set(foodobject.packaging).issubset(foodobject.unwantedpackaging):
                        c.choosing_another_packaging(foodobject, food)
                    else:
                        c.choosing_criteria(foodobject, food)
                else:
                    print("Cet élément est déja choisi. Choissisez en un autre.")

    def choosing_another_packaging(self, foodobject, food):
        """Propose to add a new packaging criteria"""
        cntnue = True
        while cntnue:
            z.allquestions[10].play_question()
            choice = input()
            if z.allquestions[10].check_if_choice_is_valable(choice):
                cntnue = False
                if int(choice) == 0:
                    c.choosing_packaging(foodobject, food)
                if int(choice) == 1:
                    c.choosing_criteria(foodobject, food)

    def allergen(self, foodobject, food):
        """Propose allergen criteria from selected food"""
        cntnue = True
        while cntnue:
            if not foodobject.unwantedallergen:
                if foodobject.allergen and foodobject.allergen[0] != "null" and \
                        foodobject.allergen[0] != "":
                    foodobject.clean_allergen()
                    z.allquestions[5].propositions = foodobject.allergen
                    z.allquestions[5].play_question()
                    choice = input()
                    if z.allquestions[5].check_if_choice_is_valable(choice):
                        cntnue = False
                        foodobject.unwantedallergen.append(
                            z.allquestions[5].propositions[int(choice)])
                        foodobject.numberofcriteria += 1
                        c.choosing_criteria(foodobject, food)
                else:
                    cntnue = False
                    print("Ce produit n'a pas d'allergène enregistré.")
                    c.choosing_criteria(foodobject, food)
            else:
                c.choosing_another_allergen(foodobject, food)

    def choosing_another_allergen(self, foodobject, food):
        """Check if the user want to change his allergen criteria"""
        cntnue = True
        while cntnue:
            z.allquestions[12].play_question()
            choice = input()
            if z.allquestions[12].check_if_choice_is_valable(choice):
                cntnue = False
                if int(choice) == 0:
                    foodobject.unwantedallergen = []
                    foodobject.numberofcriteria -= 1
                    c.allergen(foodobject, food)
                else:
                    c.choosing_criteria(foodobject, food)

    def additives(self, foodobject, food):
        """Propose additive criteria from selected food"""
        cntnue = True
        while cntnue:
            if not foodobject.unwantedadditives:
                if foodobject.additives and foodobject.additives[0] != "null" and \
                        foodobject.additives[0] != "":
                    foodobject.clean_allergen()
                    z.allquestions[6].propositions = foodobject.additives
                    z.allquestions[6].play_question()
                    choice = input()
                    if z.allquestions[6].check_if_choice_is_valable(choice):
                        cntnue = False
                        foodobject.unwantedadditives.append(
                            z.allquestions[6].propositions[int(choice)])
                        foodobject.numberofcriteria += 1
                        c.choosing_criteria(foodobject, food)
                else:
                    cntnue = False
                    print("Ce produit n'a pas d'additif enregistré.")
                    c.choosing_criteria(foodobject, food)
            else:
                c.choosing_another_additive(foodobject, food)

    def choosing_another_additive(self, foodobject, food):
        """Check if the user want to change his additive criteria"""
        cntnue = True
        while cntnue:
            z.allquestions[13].play_question()
            choice = input()
            if z.allquestions[13].check_if_choice_is_valable(choice):
                cntnue = False
                if int(choice) == 0:
                    foodobject.unwantedadditives = []
                    foodobject.numberofcriteria -= 1
                    c.additives(foodobject, food)
                else:
                    c.choosing_criteria(foodobject, food)

    def nutri_score(self, foodobject, food):
        """Select the criteria nutri score"""
        foodobject.numberofcriteria += 1
        foodobject.betterscore = True
        c.choosing_criteria(foodobject, food)

    def get_substitued_aliments(self):
        """Print all substituted aliments"""
        substitutelst = S.get_substitued()
        newsubstitutelst = []
        for x in substitutelst:
            newsubstitutelst.append(list(x))
        i = 0
        while i < len(newsubstitutelst) - 1:
            print("Vous avez remplacé {0} par {1}".format(newsubstitutelst[i][0], substitutelst[
                i + 1][1]))
            i += 1


c = Criteria()
z = Zulu()
S = Sqlfunc()
su = Submenu()
