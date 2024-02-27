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

alien, alien2, ennemy = initialisation(Actor)
L_alien.append(alien)
L_alien.append(alien2)
L_ennemy.append(ennemy)

flag_menu=0 # 0 - le menu apparait, autre le jeu se lance 
start_button=Actor("start_button",pos=(600,450)) # Donne le bouton début 
end_button=Actor("end_button",pos=(1000,450)) # Donne le bouton sortir

start_button.scale = 0.08
end_button.scale = 0.3

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

    global flag_menu
    if flag_menu ==0:
        if start_button.collidepoint(pos):
            flag_menu=1
            
        if end_button.collidepoint(pos):
            exit() # quite le programme



################################################################################################################
## Affichage
################################################################################################################        

# Cette fonction est essentielle, elle est appelée directement par pgzrun.go() (à la fin). 
# Elle gère l'affichage du monde 
            
def draw():
    screen.clear() ## Efface l’écran précédent 
    if flag_menu == 0:
        screen.fill('white')
        start_button.draw()
        end_button.draw()
    
    else:
        timer(screen)
        draw_world()



def draw_world():
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

    for i in L_ennemy:
        i.actor.draw()
        if i.gauche:
            i.image(i.name+"_g",i.scale)
        else: 
            i.image(i.name,i.scale)    
        
    if not alien2.vivant:
        screen.draw.text("You Lose", (WIDTH/2-pixel, HEIGHT/2-pixely), color="red", fontsize=60)



################################################################################################################
## Mise à jour
################################################################################################################   


# Cette fonction est aussi essentielle et elle est appelée directement par pgzrun.go() (à la fin). 
# Elle est la fonction rappelée systématiquement par pgzrun.go() pour que les éléments évolue. 
def update():
    if flag_menu != 0:

        # Déplacement de l'alien volant
        alien.deplacement_volant()

        # Déplacement de l'alien rampant
        alien2.deplacement_rampant(ennemy, keyboard,animate,sounds, clock)
        alien2.DEV_MODE(keyboard, dev_mode)

        ennemy.deplacement_rampant(gravity, sounds, animate, clock) 
        ennemy.set_ennemy_death(sounds, animate, dev_mode, alien2, clock)

        # la gestion de la suite dois être placé ici
    
pgzrun.go()
