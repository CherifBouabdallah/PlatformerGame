import pygame

## Taille de l'image 
WIDTH = 1600
HEIGHT =900

## Caractéristique du monde
nbr_pixel= 10 # Donne le nombre de bloc dans mon monde, il y en aura 10x10 
pixel= round(WIDTH/nbr_pixel) # taille horizontal des blocs 
pixely= round(HEIGHT/nbr_pixel) # taille vertical des blocs

## Map du monde 
Monde=[
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,3,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1]] 

## Image des blocs
lava_img = pygame.image.load('images/lave.png')
dirt_img = pygame.image.load('images/grass.png')
cloud_img = pygame.image.load('images/cloud.png')

## Constante de gravité de notre monde
gravity=0.04