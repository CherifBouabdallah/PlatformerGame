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
                    img = pygame.transform.scale(vertical_arrow_img, (pixel, pixely))
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

                
                if i== 5: 
                    img = pygame.transform.scale(stone_img, (pixel, pixely))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col*pixel
                    img_rect.y=nb_ligne*pixely
                    L_monde.append((img, img_rect,i))


                if i== 6: 
                    img = pygame.transform.scale(arrow_img, (pixel, pixely))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col*pixel
                    img_rect.y=nb_ligne*pixely
                    L_monde.append((img, img_rect,i))

                if i== 7: 
                    img = pygame.transform.scale(lava_img, (pixel, pixely))
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


def monde_rect_2():
        L_monde_2=[]
        deb=len(liste_mondes[1][0])-nbr_pixel2 # Ces deux variables là disent oû le monde affiché doit commencer
        fi=len(liste_mondes[1][0])
        nb_ligne2=0
        for ligne in liste_mondes[1]: # on parcours les lignes 
            nb_col2 = 0
            
            for i in ligne[deb:fi]: # on parcours les colonnes

                if i == 1: # si il y a un 1, on doit l'associer à l'image dirt_img et obtenir la position du rectangle
                    img = pygame.transform.scale(dirt_img, (pixel2, pixely2)) # on ajuste l'image aux bonnes dimensions
                    img_rect = img.get_rect() # On crée un rectangle qui a les informations de l'images
                    img_rect.x=nb_col2*pixel2 # On définie les coordonnées du rectangle
                    img_rect.y=nb_ligne2*pixely2 
                    L_monde_2.append((img, img_rect, i)) # on l'ajoute à la liste des blocs (image, rectangle, nbr)

                if i== 2: 
                    img = pygame.transform.scale(lava_img, (pixel2, pixely2))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col2*pixel2
                    img_rect.y=nb_ligne2*pixely2
                    L_monde_2.append((img, img_rect,i))


                if i== 3: 
                    img = pygame.transform.scale(vertical_arrow_img, (pixel2, pixely2))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col2*pixel2
                    img_rect.y=nb_ligne2*pixely2
                    L_monde_2.append((img, img_rect,i))

                if i== 4: 
                    img = pygame.transform.scale(end_level, (pixel2, pixely2))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col2*pixel2
                    img_rect.y=nb_ligne2*pixely2
                    L_monde_2.append((img, img_rect,i))

                if i== 5: 
                    img = pygame.transform.scale(stone_img, (pixel2, pixely2))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col2*pixel2
                    img_rect.y=nb_ligne2*pixely2
                    L_monde_2.append((img, img_rect,i))


                if i== 6: 
                    img = pygame.transform.scale(arrow_img, (pixel2, pixely2))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col2*pixel2
                    img_rect.y=nb_ligne2*pixely2
                    L_monde_2.append((img, img_rect,i))

                if i== 7: 
                    img = pygame.transform.scale(fake_lava_img, (pixel2, pixely2))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col2*pixel2
                    img_rect.y=nb_ligne2*pixely2
                    L_monde_2.append((img, img_rect,i))                 

                    
                nb_col2 += 1
            nb_ligne2 +=1


        return L_monde_2

## Cette fonction dessine les blocs sur l'écran 

def draw_monde_2(screen):
        L_monde_2=monde_rect_2()
        for bloc in L_monde_2:
            screen.blit(bloc[0],bloc[1]) # cette fontion permet d'afficher les blocs 



def monde_rect_3():
        L_monde_3=[]
        deb=len(liste_mondes[2][0]) - nbr_pixel3 # Ces deux variables là disent oû le monde affiché doit commencer
        fi=len(liste_mondes[2][0])
        nb_ligne3=0
        for ligne in liste_mondes[2]: # on parcours les lignes 
            nb_col3 = 0
            
            for i in ligne[deb:fi]: # on parcours les colonnes

                if i == 1: # si il y a un 1, on doit l'associer à l'image dirt_img et obtenir la position du rectangle
                    img = pygame.transform.scale(dirt_img, (pixel3, pixely3)) # on ajuste l'image aux bonnes dimensions
                    img_rect = img.get_rect() # On crée un rectangle qui a les informations de l'images
                    img_rect.x=nb_col3*pixel3 # On définie les coordonnées du rectangle
                    img_rect.y=nb_ligne3*pixely3 
                    L_monde_3.append((img, img_rect, i)) # on l'ajoute à la liste des blocs (image, rectangle, nbr)

                if i== 2: 
                    img = pygame.transform.scale(lava_img, (pixel3, pixely3))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col3*pixel3
                    img_rect.y=nb_ligne3*pixely3
                    L_monde_3.append((img, img_rect,i))


                if i== 3: 
                    img = pygame.transform.scale(vertical_arrow_img, (pixel3, pixely3))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col3*pixel3
                    img_rect.y=nb_ligne3*pixely3
                    L_monde_3.append((img, img_rect,i))

                if i== 4: 
                    img = pygame.transform.scale(end_level, (pixel3, pixely3))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col3*pixel3
                    img_rect.y=nb_ligne3*pixely3
                    L_monde_3.append((img, img_rect,i))

                if i== 5: 
                    img = pygame.transform.scale(stone_img, (pixel3, pixely3))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col3*pixel3
                    img_rect.y=nb_ligne3*pixely3
                    L_monde_3.append((img, img_rect,i))

                if i== 6: 
                    img = pygame.transform.scale(arrow_img, (pixel3, pixely3))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col3*pixel3
                    img_rect.y=nb_ligne3*pixely3
                    L_monde_3.append((img, img_rect,i))

                if i== 7: 
                    img = pygame.transform.scale(fake_lava_img, (pixel3, pixely3))
                    img_rect = img.get_rect()
                    img_rect.x=nb_col3*pixel3
                    img_rect.y=nb_ligne3*pixely3
                    L_monde_3.append((img, img_rect,i))              

                    
                nb_col3 += 1
            nb_ligne3 +=1


        return L_monde_3

## Cette fonction dessine les blocs sur l'écran 

def draw_monde_3(screen):
        L_monde_3 = monde_rect_3()
        for bloc in L_monde_3:
            screen.blit(bloc[0],bloc[1]) # cette fontion permet d'afficher les blocs 
