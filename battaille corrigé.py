import random

VALEURS = ['', '', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
COULEURS = ['', 'pique', 'coeur', 'carreau', 'trefle']

class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def get_nom(self):
        return VALEURS[self.valeur]

    def get_couleur(self):
        return COULEURS[self.couleur]

class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    def remplir(self):
        self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(2, 15)]

    def get_carte_at(self, pos):
        if 0 <= pos < 52:
            return self.contenu[pos]

    def __len__(self):
        return len(self.contenu)

class Joueur:
    def __init__(self):
        self.PaquetJoueur = []

    def distribuerJoueur(self):
        if len(PaquetDeDistribution) >= 52:
            for i in range(27, 52):
                if PaquetDeDistribution.contenu:
                    index = random.randint(0, len(PaquetDeDistribution.contenu) - 1)
                    self.PaquetJoueur.append(PaquetDeDistribution.contenu.pop(index))
        else:
            for i in range(1, 26):
                if PaquetDeDistribution.contenu:
                    index = random.randint(0, len(PaquetDeDistribution.contenu) - 1)
                    self.PaquetJoueur.append(PaquetDeDistribution.contenu.pop(index))

PaquetDeDistribution = PaquetDeCarte()
PaquetDeDistribution.remplir()

PaquetJoueur1 = Joueur()
PaquetJoueur2 = Joueur()
PaquetJoueur1.distribuerJoueur()
PaquetJoueur2.distribuerJoueur()

