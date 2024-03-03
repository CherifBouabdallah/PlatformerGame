from Joueur import *

L_alien=[]
L_ennemy = []

## Cette fonction permet la création des différents éléments du jeu
def initialisation(Actor): 
    alien= Joueur(Actor('alien'))  # Création du personnage alien
    alien.actor.topright = 500, 0  # Position en partant du coin en haut à droite
    alien2= Joueur(Actor('alien'), 0.75) # Création du personnage alien2
    alien2.actor.topright = 50, 750    # Position de départ
    ennemy= Ennemy(Actor('ennemy'), 0.075, "ennemy") # Création du personnage ennemy
    ennemy.actor.topright = 1300, 740     # Position de départ
    return alien, alien2, ennemy           # On retourne les personnages pour pouvoir les utiliser