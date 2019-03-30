from questions import Question
from sqlfunc import Sqlfunc
from generatingdb import Generatingdb
from criteria import Criteria
from zulu import Zulu


class Main:
    """Contain the main loop functions"""
    cntinue = True

    def main(self):
        """main loop"""
        while Main.cntinue:
            z.allquestions[0].play_question()
            choice = input()
            if z.allquestions[0].check_if_choice_is_valable(choice):
                if int(choice) == 1:
                    if s.get_number_of_rows("alimentsss") >= 50:
                        c.choosing_categorie()
                    else:
                        m.database_is_empty()
                if int(choice) == 2:
                    m.looking_substituted()
                if int(choice) == 3:
                    print("En cours de création de la base de données, patientez SVP")
                    s.clean_table("alimentsss")
                    m.generate_db()
                    print("Base de données prête à l'emploi")
                if int(choice) == 4:
                    m.clean_substitued()
                if int(choice) == 5:
                    break

    def looking_substituted(self):
        """Check if substituted food exist, if yes, it prints them"""
        if s.get_number_of_rows("newaliments") != 0:
            c.get_substitued_aliments()
        else:
            print("Il n'y a actuellement aucun aliment substitué")

    def generate_db(self):
        """Generate database"""
        g.distrib_url()

    def database_is_empty(self):
        """Ask if the user want to create the database"""
        z.allquestions[8].play_question()
        choice = input()
        if z.allquestions[8].check_if_choice_is_valable(choice):
            if int(choice) == 1:
                print("En cours de création de la base de données, patientez SVP")
                m.database_creation()
                print("Base de données prête à l'emploi")
            elif int(choice) == 2:
                Main.cntinue = False

    def database_creation(self):
        """Clean and recreate the database"""
        s.clean_table("alimentsss")
        g.distrib_url()

    def clean_substitued(self):
        """Clean the substituted food database"""
        cntnue = True
        while cntnue:
            z.allquestions[15].play_question()
            choice = input()
            if z.allquestions[15].check_if_choice_is_valable(choice):
                cntnue = False
                if int(choice) == 1:
                    s.clean_table("newaliments")
                else:
                    m.main()


m = Main()
s = Sqlfunc()
g = Generatingdb()
c = Criteria()
q = Question(None, None)
z = Zulu()
m.main()
print("Au revoir")
