import random
VALEURS = ['','', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
COULEURS = ['', 'pique', 'coeur', 'carreau', 'trefle']


class Carte:
    """Initialise couleur (de 1 à 4), et valeur (de 2 à 14)"""

    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def get_nom(self):
        """Renvoie le nom de la Carte As, 2, ... 10, Valet, Dame, Roi"""
        return VALEURS[self.valeur]

    def get_couleur(self):
        """Renvoie la couleur de la Carte (parmi pique, coeur, carreau, trefle)"""
        return COULEURS[self.couleur]

class PaquetDeCarte:
    """Initialise un paquet de cartes, avec un attribut contenu, de type list, vide"""

    def __init__(self):
        self.contenu = []

    def remplir(self):
        """Remplit le paquet de cartes : en parcourant les couleurs puis les valeurs"""
        self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(2, 15)]

    def get_carte_at(self, pos):
        """Renvoie la Carte qui se trouve à la position donnée"""
        if 0 <= pos < 52:
            return self.contenu[pos]

PaquetDeDistribution=PaquetDeCarte()
PaquetDeDistribution.remplir()

class Joueur:

    def distribuerJoueur(self):
        if len(PaquetDeDistribution)==52:
            for i in range(27,52,-1):
                PaquetJoueur.append(PaquetDeDistribution.pop(random.randint(1,i)))
        else:
            for i in range(1,26,-1):
                PaquetJoueur.append(PaquetDeDistribution.pop(random.randint(1,i)))

    def get_carte_at_Joueur(self, pos):
        if 0 <= pos < 26:
            return self.PaquetJoueur[pos]


PaquetJoueur1=Joueur()
PaquetJoueur2=Joueur()
PaquetJoueur1.distribuerJoueur()
PaquetJoueur2.distribuerJoueur()
