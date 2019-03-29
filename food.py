from sqlfunc import Sqlfunc


class Food:
    """The food object contain all information from the aliment and all information wanted by
    the user"""
    def __init__(self, name, categorie):
        s = Sqlfunc()
        self.name = name
        self.number = self.clean_result(s.get_something_from(self.name, "url"))
        self.additives = self.clean_result(s.get_something_from(self.name, "additifs"))
        self.packaging = self.clean_result(s.get_something_from(self.name, "packaging"))
        self.score = self.clean_result(s.get_something_from(self.name, "score"))
        self.allergen = self.clean_result(s.get_something_from(self.name, "allergen"))
        self.image = self.clean_result(s.get_something_from(self.name, "imageurl"))
        self.producturl = self.get_product_url()
        self.stores = self.clean_result(s.get_something_from(self.name, "shop"))
        self.categorie = categorie
        self.unwantedpackaging = []
        self.wantednutritionnalvalue = []
        self.unwantedallergen = []
        self.unwantedadditives = []
        self.numberofcriteria = 0
        self.betterscore = False


    def clean_list(self):
        """Transform the value into a list"""
        self.packaging = self.packaging[0].split(', ')

    def clean_allergen(self):
        """Transform the value into a list"""
        self.allergen = self.allergen[0].split(', ')

    def clean_result(self, lst):
        """Clean the results"""
        newlst = [''.join(x).replace("('", "") for x in lst]
        newlst = [''.join(x).replace('"', '') for x in newlst]
        newlst = [''.join(x).replace('[', '') for x in newlst]
        newlst = [''.join(x).replace(']', '') for x in newlst]
        newlst = [''.join(x).replace('.json', '') for x in newlst]
        return newlst

    def get_image_url(self):
        """Print image url if possible"""
        if self.image is not "null":
            print("Url de l'image : {0}".format(self.image[0]))

    def get_product_url(self):
        """Return product url from code"""
        producturl = self.number[0].replace("api/v0/", "")
        return producturl

    def enumerate_shop(self):
        """If stores are recorded, print them"""
        if self.stores is not None or self.stores[0] != "null":
            for i in self.stores:
                print(i, end=", ")


