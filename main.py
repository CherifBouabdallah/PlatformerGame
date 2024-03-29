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

alien2, ennemy = initialisation(Actor)
#L_alien.append(alien)
L_alien.append(alien2)
L_ennemy.append(ennemy)

flag_menu = 0
flag_timer = 0

start_button=Actor("start_button",pos=(600,450)) # Donne le bouton début 
end_button=Actor("end_button",pos=(1000,450)) # Donne le bouton sortir
alternatif_button = Actor("alternatif",pos=(800,600)) # Donne le bouton alternatif

start_button.scale = 0.08
end_button.scale = 0.3
alternatif_button.scale = 0.1

start_time = time.time()

def restart():
    alien2.scale = 0.75
    ennemy.scale =  0.075

    alien2.vivant = True
    ennemy.vivant = True
    
    start_time = time.time() 

    alien2.level = 0
    ennemy.level = 0

    alien2.actor.topright = 50, 750
    ennemy.actor.topright = 1300, 740


    for i in range(3, 0, -1):
            screen.clear()
            draw_world()
            screen.draw.text(str(i), (WIDTH/2-pixel, (HEIGHT/2-pixely)-200), color="red", fontsize=200)
            pygame.display.update()
            time.sleep(timer_time)


    return start_time


def activ(keyboard):
    if keyboard.r:
        restart()

################################################################################################################
## Gestion des évènements
################################################################################################################

## Cette fonction gère les cliques de souris
# Si on appuits sur le bouton gauche de la souris à un endroit où se trouve un alien alors
# on applique la fonction set_alien_hurt


def on_mouse_down(pos,button):
    global flag_menu, flag_timer, alternatif_mode

    if flag_menu ==0:
        if start_button.collidepoint(pos):
            flag_menu = 1
            flag_timer = 1
            
        if end_button.collidepoint(pos):
            exit() # quite le programme
        
        if alternatif_button.collidepoint(pos):
            flag_menu = 1
            flag_timer = 1
            alternatif_mode = True
    
    for i in L_alien:
        if button == mouse.LEFT and i.actor.collidepoint(pos): 
            i.set_alien_hurt(sounds,clock)



def gestion_alternative(alternatif_mode):
    global timer_time, bkg, image_gauche, image_droite
    if alternatif_mode:
        timer_time = 0.25
        bkg = bkg_alternatif
        image_droite = 'alien_hurt'
        image_gauche = 'alien_hurt_g'





################################################################################################################
## Affichage
################################################################################################################        

# Cette fonction est essentielle, elle est appelée directement par pgzrun.go() (à la fin). 
# Elle gère l'affichage du monde 
            
def draw():

    screen.clear() ## Efface l’écran précédent 

    global flag_timer #timer au début
    if flag_timer == 1:
        for i in range(3, 0, -1):
            screen.clear()
            draw_world()
            screen.draw.text(str(i), (WIDTH/2-pixel, (HEIGHT/2-pixely)-200), color="red", fontsize=200)
            pygame.display.update()
            time.sleep(timer_time)
            flag_timer = 0

    if flag_menu == 0:
        bkg_img=pygame.transform.scale(bkg,(WIDTH, HEIGHT))
        screen.blit(bkg_img ,(0,0))
        start_button.draw()
        end_button.draw()
        alternatif_button.draw()
    
    else:
        draw_world()

def draw_world():
    screen.clear() ## Efface l'écran précédent
    bkg_img=pygame.transform.scale(bkg,(WIDTH, HEIGHT))
    screen.blit(bkg_img ,(0,0))
    
    if alien2.level == 0:
        draw_monde(screen)
    if alien2.level == 1:
        draw_monde_2(screen)
    
    time_counter = font.render(f'Time in game : {time_clock()//60}m {time_clock()%60}s', True, (0, 0, 0))
    screen.blit(time_counter, (0, 0))

    pos = font.render(str(alien2.actor.topright), True, (0, 0, 0))
    screen.blit(pos, (800, 0))

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
# Elle est la fonction rappelée systématiquement par pgzrun.go() pour que les éléments évoluent. 
        

def time_clock():
    play_time = time.time() - start_time
    return round(play_time)

def update():
    if flag_menu != 0:

        # Déplacement de l'alien rampant
        alien2.deplacement_rampant(ennemy, keyboard,animate,sounds, clock)
        alien2.death_image()

        ennemy.deplacement_rampant(gravity, sounds, animate, clock, alien2) 
        ennemy.set_ennemy_death(sounds, animate, dev_mode, alien2, clock)

        gestion_alternative(alternatif_mode)

        activ(keyboard)
        # la gestion de la suite dois être placé ici

    if not alien2.vivant:
        music_channel.stop()

    
pgzrun.go()

