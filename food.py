from sqlfunc import Sqlfunc


class Food:
    def __init__(self, name, categorie):
        s = Sqlfunc()
        self.name = name
        self.number = self.clean_result(s.get_number_from(self.name))
        self.additives = self.clean_result(s.get_additives_from(self.name))
        self.packaging = self.clean_result(s.get_packaging_from(self.name))
        self.score = self.clean_result(s.get_score_from(self.name))
        self.allergen = self.clean_result(s.get_allergen_from(self.name))
        self.substitute = None
        self.categorie = categorie
        self.unwantedpackaging = []
        self.wantednutritionnalvalue = []
        self.unwantedallergen = []
        self.unwantedadditives = []
        self.numberofcriteria = 0
        self.betterscore = False

    def clean_list(self):
        self.packaging = self.packaging[0].split(', ')

    def clean_allergen(self):
        self.allergen = self.allergen[0].split(', ')

    def clean_result(self, lst):
        newlst = [''.join(x).replace("('", "") for x in lst]
        newlst = [''.join(x).replace('"', '') for x in newlst]
        newlst = [''.join(x).replace('[', '') for x in newlst]
        newlst = [''.join(x).replace(']', '') for x in newlst]
        newlst = [''.join(x).replace('.json', '') for x in newlst]
        return newlst
