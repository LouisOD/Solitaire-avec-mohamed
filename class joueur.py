class Joueur:
    def __init__(self):
        self.PaquetJoueur = deque() # On va Utiliser  une  file pour représenter le paquet du joueur

    def distribuerJoueur(self, PaquetDeDistribution):
        # On Distribue la moitié du paquet au joueur
        self.PaquetJoueur.extend(PaquetDeDistribution.contenu[:26])
        PaquetDeDistribution.contenu = PaquetDeDistribution.contenu[26:]