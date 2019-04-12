class Question:
    """Questionning or not, I am hungry said a wise men"""
    questionstext = [
        "\nBienvenue sur ce logiciel. Que voulez vous faire ?",
        "\nVoici les catégories.",
        "\nVoici 10 aliments de la catégorie choisie.",
        "\nSélectionnez un critère.",
        "\nVoici le conditionnement du produit que vous avez choisi. \n Quel conditionnement "
        "préférez vous éviter ?.",
        "\nVoici le(s) allergène(s) présents dans le produit choisi. Lequel voulez vous éviter ?",
        "\nVoici le(s) additif(s) présents dans le produit choisi. Lequel voulez vous éviter ?",
        "\nChoisissez un critère de valeur nutritionelle :",
        "\nLa base de données est actuellement vide. Souhaitez vous :",
        "\nVoici le(s) conditionnement(s), sélectionnez celui que vous ne souhaitez pas",
        "\nSouhaitez vous sélectionner un autre conditionnement ?",
        "\nVous avez déjà choisi un critère de valeur nutritionelle. Souhaitez vous en "
        "changer ?",
        "\nVous avez déjà choisi un allergène. Souhaitez vous en changer ?",
        "\nVous avez déjà choisi un additif. Souhaitez vous en changer ?",
        "\nVoici un ou plusieurs résultats répondant aux critères choisis",
        "\nSouhaitez vous vraiment supprimer vos aliments substitués ? \nCette opération est "
        "irréversible."
    ]

    questionspropositions = [
        ["Choisir un aliment.", "Voir les aliments substitués.", "Regenerer la base de données.",
         "Supprimer les aliments substitués.", "Quitter le logiciel."],
        ["Snacks", "Meals", "Cereals", "Meats", "Cheeses", "Retour au menu précédent"],
        [],
        ["Packaging", "Indice Nutritionnel", "Allergènes", "Additifs", "Nutri-score",
         "Retour au menu précédent", "Trouver un aliment avec les critères choisis"],
        [],
        [],
        [],
        ["Graisse en grande quantité", "Graisse en faible quantité", "Sucre en grande quantité",
         "Sucre en faible quantité", "Sel en grande quantité", "Sel en faible quantité",
         "Retour au menu précédent"],
        ["Créer la base de données", "Quitter le logiciel"],
        [],
        ["Oui", "Non"],
        ["Oui", "Non"],
        ["Oui", "Non"],
        ["Oui", "Non"],
        [],
        ["Oui", "Non"]

    ]

    def __init__(self, text, propositions, option=None):
        self.text = text
        self.propositions = propositions
        self.option = option

    def play_question(self):
        """play the question and propositions"""
        print(self.text)
        self.print_prop()

    def print_prop(self):
        """print the propositions"""
        i = 1
        self.clean_result()
        while i < len(self.propositions) + 1:
            print("{0}.{1}".format(i, self.propositions[i - 1]))
            i += 1

    def check_if_choice_is_valable(self, choice):
        """check if input is valable and return True"""
        if choice.isdigit() and 1 <= int(choice) < len(self.propositions) + 1:
            return True
        else:
            print("Merci de rentrer un chiffre dans l'intervalle proposé")

    def clean_result(self):
        """Clean the results"""
        self.propositions = [''.join(x).replace("('", "") for x in self.propositions]
        self.propositions = [''.join(x).replace('"', '') for x in self.propositions]

    def generate_questions(self):
        """Generate all the questions"""
        allquestions = []
        i = 0
        while i < len(Question.questionstext):
            allquestions.append(
                Question(Question.questionstext[i], Question.questionspropositions[i]))
            i += 1
        return allquestions


