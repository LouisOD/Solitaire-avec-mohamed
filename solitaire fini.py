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
TapisJoueur1=Tapis()
TapisJoueur2=Tapis()
carte_en_jeu_joueur1=[]
carte_en_jeu_joueur2=[]
class Tapis:
    def __init__(self):
     self.cartes_en_jeu = [] #attribut cartes_en_jeu qui est une liste vide. il  stocke les cartes posées sur le tapis

    def poser_carte(self): #pose une carte sur le tapis. Prend une carte en argument
        self.cartes_en_jeu.append()
        self.pop()

    def recuperer_cartes(self,Joueurconcerné):#récupére toutes les cartes du tapis
       Joueurconcerné.append(self[0].pop()


##    def afficher_tapis(self):
##        ##affiche les cartes actuellement sur le tapis
##        if self.cartes_en_jeu:
##            ## sa Vérifie si la liste cartes_en_jeu n'est pas vide
##            print("Cartes sur le tapis:")
##            ## indique bien que les cartes sont sur la tapis
##            for carte in self.cartes_en_jeu:
##                ##Boucle qui  traverse tt les cartes sur le tapis
##                print(f"{carte.get_nom()} de {carte.get_couleur()}")
##                ##  donne  le nom et la couleur de chaque carte sur une nouvelle ligne
##        else:
##            ## sinon exécuté si la liste cartes_en_jeu est vide
##            print("Le tapis est vide.")


def bataille():
    while PaquetJoueur1!=[] or PaquetJoueur2!=[]:
        TapisJoueur1.poser_carte()
        TapisJoueur2.poser_carte()
        while TapisJoueur1[0].get_nom()==TapisJoueur2[0].get_nom()
			for i in range(2):
                TapisJoueur1.empiler()
                TapisJoueur2.empiler()
        if TapisJoueur1[0].get_nom() > TapisJoueur2[0].get_nom()
            while TapisJoueur1!=[]
    			TapisJoueur1.recuperer_cartes(PaquetJoueur1)
    		while TapisJoueur2!=[]
    			TapisJoueur2.recuperer_cartes(PaquetJoueur1)
    	else :
    		while TapisJoueur1!=[]
    			TapisJoueur1.recuperer_cartes(PaquetJoueur2)
    		while TapisJoueur2!=[]
    			TapisJoueur2.recuperer_cartes(PaquetJoueur2)
    if PaquetJoueur1==[]:
        return("Joueur 2 vainqueur!")
    elif PaquetJoueur2==[]:
        return("Joueur 1 vainqueur!")
