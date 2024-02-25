from Joueur import *

L_alien=[]
L_ennemy = []

## Cette fonction permet la création des différents éléments du jeu
def initialisation(Actor): 
    alien= Joueur(Actor('alien'))  # Création du personnage alien
    alien.actor.topright = 500, 0  # Position en partant du coin en haut à droite
    alien2= Joueur(Actor('alien'),0.5) # Création du personnage alien2
    alien2.actor.topleft =0, 600     # Position de départ
    ennemy= Ennemy(Actor('ennemy'), 0.075, "ennemy") # Création du personnage ennemy
    ennemy.actor.topright = 1400, 700     # Position de départ
    return alien, alien2, ennemy           # On retourne les personnages pour pouvoir les utiliser



def collision_ennemi(self, L_ennemi, L_mob, animate, sounds, clock):
        for i in L_ennemi:  # on prend un à un tout les ennemis un à un
            if self.actor.left<=i.actor.right and self.actor.right>=i.actor.left and self.actor.bottom>i.actor.top and self.actor.top <=i.actor.bottom:  # Si l'ennemi touche le joueur on vérifie que des coordonées du joueur soit à l'intérieur de l'ennemi
                self.vie-=1  # alors le Joueur perd une vie
                self.actor.topleft =0,300
                self.dx=0
                self.dy=0
            if self.actor.left<=i.actor.right and self.actor.right>=i.actor.left and self.actor.bottom<=i.actor.top and self.actor.bottom>=i.actor.top-6: # Si le bas du joueur est entre les coordonés du haut de l'ennemi et 3 pixels au dessus
                L_mob.remove(i)  # alors l'ennemi est supprimé des listes contenant les différents acteurs et ennemis
                L_ennemi.remove(i)