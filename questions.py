class Question:
    questionstext = [
        "Bienvenue sur ce logiciel. Que voulez vous faire ?",
        "Voici les catégories.",
        "Voici 10 aliments de la catégorie choisie.",
        "Sélectionnez un critère.",
        "Voici le conditionnement du produit que vous avez choisi. \n Quel conditionnement "
        "préférez vous éviter ?.",
        "Voici le(s) allergène(s) présents dans le produit choisi. Lequel voulez vous éviter ?",
        "Voici le(s) additif(s) présents dans le produit choisi. Lequel voulez vous éviter ?",
        "Choisissez un critère de valeur nutritionelle :",
        "La base de données est actuellement vide. Souhaitez vous :",
        "Voici le(s) conditionnement(s), sélectionnez celui que vous ne souhaitez pas",
        "Souhaitez vous sélectionner un autre conditionnement ?",
        "Vous avez déjà choisi un critère de valeur nutritionelle. Souhaitez vous en "
        "changer ?",
        "Vous avez déjà choisi un allergène. Souhaitez vous en changer ?",
        "Vous avez déjà choisi un additif. Souhaitez vous en changer ?",
        "Voici un ou plusieurs résultats répondant aux critères choisis",
        "Souhaitez vous vraiment supprimer vos aliments substitués ? \nCette opération est "
        "irréversible."
    ]

    questionspropositions = [
        ["Choisir un aliment.", "Voir les aliments substitués.", "Regenerer la base de données.",
         "Supprimer les aliments substitués.", "Quitter le logiciel."],
        ["Snacks", "Meals", "Cereals", "Meats", "Retour au menu précédent"],
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
        print(self.text)
        self.print_prop()

    def print_prop(self):
        i = 0
        self.clean_result()
        while i < len(self.propositions):
            print("{0}.{1}".format(i, self.propositions[i]))
            i += 1

    def check_if_choice_is_valable(self, choice):
        if choice.isdigit() and 0 <= int(choice) < len(self.propositions):
            return True
        else:
            print("Merci de rentrer un chiffre dans l'intervalle proposé")

    def clean_result(self):
        self.propositions = [''.join(x).replace("('", "") for x in self.propositions]
        self.propositions = [''.join(x).replace('"', '') for x in self.propositions]

    def generate_questions(self):
        allquestions = []
        i = 0
        while i < len(Question.questionstext):
            allquestions.append(
                Question(Question.questionstext[i], Question.questionspropositions[i]))
            i += 1
        return allquestions
