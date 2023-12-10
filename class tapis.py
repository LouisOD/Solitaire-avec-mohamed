# Créé par basrirm, le 28/11/2023 en Python 3.7
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
