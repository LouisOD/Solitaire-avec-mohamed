# Créé par basri, le 10/12/2023 en Python 3.7
import random
from collections import deque
# Définition des valeurs et couleurs des cartes
VALEURS = ['', '', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
COULEURS = ['', 'pique', 'coeur', 'carreau', 'trefle']
# Définition de la classe Carte
class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

    def get_nom(self):
        return VALEURS[self.valeur]

    def get_couleur(self):
        return COULEURS[self.couleur]

    def get_valeur(self):
        return self.valeur
# Définition de la classe PaquetDeCarte
class PaquetDeCarte:
    def __init__(self):
        self.contenu = []

    def remplir(self):
        # Création d'un paquet de cartes avec l'ensemble des combinaisons de valeurs et de couleurs possibles
        self.contenu = [Carte(couleur, valeur) for couleur in range(1, 5) for valeur in range(2, 15)]
        random.shuffle(self.contenu)
# Définition de la classe Joueur
class Joueur:
    def __init__(self):
        self.PaquetJoueur = deque() # On va Utiliser  une  file pour représenter le paquet du joueur

    def distribuerJoueur(self, PaquetDeDistribution):
        # On Distribue la moitié du paquet au joueur
        self.PaquetJoueur.extend(PaquetDeDistribution.contenu[:26])
        PaquetDeDistribution.contenu = PaquetDeDistribution.contenu[26:]
# Définition de la classe Tapis
class Tapis:
    def __init__(self):
        self.cartes_en_jeu = deque() # File pour les cartes en jeu
        self.paquet_bataille = deque() # Pile pour les cartes dans la  bataille

    def poser_carte(self, joueur):
        if joueur.PaquetJoueur:
            return joueur.PaquetJoueur.popleft()  # Prendre la carte du dessus sur le  paquet du joueur
        else:
            return None

    def comparer_cartes(self, PaquetJoueur1, PaquetJoueur2):
        while PaquetJoueur1.PaquetJoueur and PaquetJoueur2.PaquetJoueur:
            # Comparaison des cartes et gestion de la bataille
            carte_joueur1 = self.poser_carte(PaquetJoueur1)
            carte_joueur2 = self.poser_carte(PaquetJoueur2)

            if carte_joueur1 is not None and carte_joueur2 is not None:
                if carte_joueur1.get_valeur() > carte_joueur2.get_valeur():
                    self.recuperer_cartes(PaquetJoueur1)
                else:
                    self.recuperer_cartes(PaquetJoueur2)

    def recuperer_cartes(self, gagnant):
         # Récupération des cartes dans le paquet du gagnant et la pile de la  bataille
        self.cartes_en_jeu.extend(gagnant.PaquetJoueur)
        self.cartes_en_jeu.extend(self.paquet_bataille)
        gagnant.PaquetJoueur.clear()
        self.paquet_bataille.clear()

def bataille():
    # Init du paquet de cartes, des joueurs et du tapis
    PaquetDeDistribution = PaquetDeCarte()
    PaquetDeDistribution.remplir()

    PaquetJoueur1 = Joueur()
    PaquetJoueur2 = Joueur()

    PaquetJoueur1.distribuerJoueur(PaquetDeDistribution)
    PaquetJoueur2.distribuerJoueur(PaquetDeDistribution)

    TapisJeu = Tapis()
    # Début de la bataille
    TapisJeu.comparer_cartes(PaquetJoueur1, PaquetJoueur2)
     # Afficher les résultats
    if not PaquetJoueur1.PaquetJoueur or not PaquetJoueur2.PaquetJoueur:
        print("La partie est terminée.")

    if not PaquetJoueur1.PaquetJoueur:
        print("Joueur 2 vainqueur!")
    elif not PaquetJoueur2.PaquetJoueur:
        print("Joueur 1 vainqueur!")

# Test du jeu
bataille()


