import pgzrun
import pygame
import time
from pgzhelper import *
from Parametre import * 
from Monde import *
from Joueur import * 
from Initialisation import *

################################################################################################################
## Initialisation du jeu 
################################################################################################################
L_alien=[]
alien, alien2, ennemy = initialisation(Actor)
L_alien.append(alien)
L_alien.append(alien2)
L_alien.append(ennemy)


################################################################################################################
## Gestion des évènements
################################################################################################################

## Cette fonction gère les cliques de souris
# Si on appuits sur le bouton gauche de la souris à un endroit où se trouve un alien alors
# on applique la fonction set_alien_hurt
def on_mouse_down(pos,button):
    for i in L_alien:
        if button == mouse.LEFT and i.actor.collidepoint(pos): 
            i.set_alien_hurt(sounds,clock)

################################################################################################################
## Affichage
################################################################################################################        

# Cette fonction est essentielle, elle est appelée directement par pgzrun.go() (à la fin). 
# Elle gère l'affichage du monde 
def draw():
    screen.clear() ## Efface l'écran précédent
    bkg_img=pygame.transform.scale(bkg,(WIDTH, HEIGHT))
    screen.blit(bkg_img ,(0,0))
    
    
    draw_monde(screen)
    for i in L_alien:
        i.actor.draw()
        if i.gauche:
            i.image(i.name+"_g",i.scale)
        else: 
            i.image(i.name,i.scale)
 
    if not alien2.vivant:
        screen.draw.text("You Loose", (WIDTH/2-pixel, HEIGHT/2-pixely), color="red", fontsize=60)

################################################################################################################
## Mise à jour
################################################################################################################   


# Cette fonction est aussi essentielle et elle est appelée directement par pgzrun.go() (à la fin). 
# Elle est la fonction rappelée systématiquement par pgzrun.go() pour que les éléments évolue. 
def update():
    
    # Déplacement de l'alien volant
    alien.deplacement_volant()

    # Déplacement de l'alien rampant
    alien2.deplacement_rampant(ennemy, keyboard,animate,sounds, clock)
    ennemy.deplacement_rampant(5, gravity)

    # la gestion de la suite dois être placé ici
    
pgzrun.go()
