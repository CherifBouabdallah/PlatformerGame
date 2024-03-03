import pygame
import time
from Parametre import * 

''' Ce fichier gère la création du monde, l'affichage et l'enregistrement des positions des blocs'''


## Cette fonction lit la "Map" et la convertie en une liste de bloc contenant les différentes 
# images des différents blocs
 
def monde_rect():
        L_monde=[]
        deb=len(liste_mondes[0][0])-nbr_pixel # Ces deux variables là disent oû le monde affiché doit commencer
        fi=len(liste_mondes[0][0])
        nb_ligne=0
        for ligne in liste_mondes[0]: # on parcours les lignes 
            nb_col = 0
            
            for i in ligne[deb:fi]: # on parcours les colonnes

                if i == 1: # si il y a un 1, on doit l'associer à l'image dirt_img et obtenir la position du rectangle
                    img = pygame.transform.scale(dirt_img, (pixel, pixely)) # on ajuste l'image aux bonnes dimensions
                    img_rect = img.get_rect() # On crée un rectangle qui a les informations de l'images
                    img_rect.x=nb_col*pixel # On définie les coordonnées du rectangle
                    img_rect.y=nb_ligne*pixely 
                    L_monde.append((img, img_rect, i)) # on l'ajoute à la liste des blocs (image, rectangle, nbr)

                if i== 2: 
                    img = pygame.transform.scale(lava_img, (pixel, pixely))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col*pixel
                    img_rect.y=nb_ligne*pixely
                    L_monde.append((img, img_rect,i))


                if i== 3: 
                    img = pygame.transform.scale(cloud_img, (pixel, pixely))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col*pixel
                    img_rect.y=nb_ligne*pixely
                    L_monde.append((img, img_rect,i))

                if i== 4: 
                    img = pygame.transform.scale(end_level, (pixel, pixely))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col*pixel
                    img_rect.y=nb_ligne*pixely
                    L_monde.append((img, img_rect,i))

                    
                nb_col += 1
            nb_ligne +=1


        return L_monde

## Cette fonction dessine les blocs sur l'écran 

def draw_monde(screen):
        L_monde=monde_rect()
        for bloc in L_monde:
            screen.blit(bloc[0],bloc[1]) # cette fontion permet d'afficher les blocs 