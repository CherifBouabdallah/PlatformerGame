from Joueur import *



## Cette fonction permet la création des différents éléments du jeu
def initialisation(Actor): 
    alien= Joueur(Actor('alien'))  # Création du personnage alien
    alien.actor.topright = 500, 0  # Position en partant du coin en haut à droite
    alien2= Joueur(Actor('alien'),0.5) # Création du personnage alien2
    alien2.actor.topleft =0, 600     # Position de départ
    ennemy= Ennemy(Actor('ennemy'), 0.075, "ennemy") # Création du personnage ennemy
    ennemy.actor.topleft =0, 0     # Position de départ
    return alien, alien2, ennemy           # On retourne les personnages pour pouvoir les utiliser