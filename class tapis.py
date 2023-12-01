# Créé par basrirm, le 28/11/2023 en Python 3.7
class Tapis:
    def __init__(self):
     self.cartes_en_jeu = [] #attribut cartes_en_jeu qui est une liste vide. il  stocke les cartes posées sur le tapis

    def poser_carte(self, carte): #pose une carte sur le tapis. Prend une carte en argument
        self.cartes_en_jeu.append(carte) #Ajoute la carte à la liste cartes_en_jeu

    def recuperer_cartes(self):#récupére toutes les cartes du tapis
        cartes = self.cartes_en_jeu.copy() #Copie la liste des cartes sur le tapis dans une nouvelle liste appelée cartes
        self.cartes_en_jeu.clear() # Vide la liste des cartes sur le tapis
        return cartes # Renvoie  la copie des cartes récupérées

    def afficher_tapis(self): #affiche les cartes actuellement sur le tapis
        if self.cartes_en_jeu: # sa Vérifie si la liste cartes_en_jeu n'est pas vide
            print("Cartes sur le tapis:") # indique bien que les cartes sont sur la tapis
            for carte in self.cartes_en_jeu: #Boucle qui  traverse tt les cartes sur le tapis
                print(f"{carte.get_nom()} de {carte.get_couleur()}") #  donne  le nom et la couleur de chaque carte sur une nouvelle ligne
        else: # sinon exécuté si la liste cartes_en_jeu est vide
            print("Le tapis est vide.")
