
# -*- coding: utf-8 -*-

import pygame, sys, random

pygame.init()


#variable
blanc = (250,250,250)
noir = (0,0,0)
chrono = pygame.time.Clock()
vitesse_balle_y = 9
vitesse_balle_x = 9
vitesse_barre_joueur_y = 0
vitesse_barre_ennemi_y = 8
point_joueur = 0
point_ennemi = 0
police_jeu = pygame.font.Font("freesansbold.ttf",52)
run = True

#caracteristique de l'ecran
largeur_ecran = 1080
longueur_ecran = 720
ecran = pygame.display.set_mode((largeur_ecran,longueur_ecran))
pygame.display.set_caption("pong")

#placement balle et barres
barre_joueur = pygame.Rect(largeur_ecran - 10,longueur_ecran/2 - 80,10,140)
barre_ennemi = pygame.Rect(0,longueur_ecran/2 - 80,10,140)
balle = pygame.Rect(largeur_ecran/2 - 15,longueur_ecran/2 -15,30,30)

while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#annimation de la barre joueur
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                vitesse_barre_joueur_y -= 7
            if event.key == pygame.K_UP:
                vitesse_barre_joueur_y += 7
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                vitesse_barre_joueur_y += 7
            if event.key == pygame.K_UP:
                vitesse_barre_joueur_y -= 7
                                      
#annimation de la balle
    balle.x += vitesse_balle_x
    balle.y += vitesse_balle_y

    if balle.bottom >= longueur_ecran or balle.top <= 0:
        vitesse_balle_y *= -1
        
#annimation de la barre ennemi
    if barre_ennemi.bottom < balle.y:
        barre_ennemi.top += vitesse_barre_ennemi_y
    if barre_ennemi.top > balle.y:
        barre_ennemi.bottom -= vitesse_barre_ennemi_y
        
#annimation collition
    if balle.colliderect(barre_ennemi) or balle.colliderect(barre_joueur):
        vitesse_balle_x *= -1
        
    barre_joueur.y += vitesse_barre_joueur_y
        
    if barre_joueur.top <= 0:
            barre_joueur.top = 0
    if barre_joueur.bottom >= longueur_ecran:
            barre_joueur.bottom = longueur_ecran

#annimation nouvelle partie
    if balle.right >= largeur_ecran:
        balle.center =(largeur_ecran/2, longueur_ecran/2)
        barre_joueur.center =(largeur_ecran - 5, longueur_ecran/2)
        barre_ennemi.center =(5, longueur_ecran/2)
        vitesse_balle_y *= random.choice((1,-1))
        vitesse_balle_x *= random.choice((1,-1))
        point_ennemi += 1
        
    if balle.left <= 0:
        balle.center =(largeur_ecran/2, longueur_ecran/2)
        barre_joueur.center =(largeur_ecran - 5, longueur_ecran/2)
        barre_ennemi.center =(5, longueur_ecran/2)
        vitesse_balle_y *= random.choice((1,-1))
        vitesse_balle_x *= random.choice((1,-1)) 
        point_joueur += 1
        
#affichage general
    ecran.fill(noir)       
    pygame.draw.rect(ecran,blanc,barre_joueur)
    pygame.draw.rect(ecran,blanc,barre_ennemi)
    pygame.draw.ellipse(ecran,blanc,balle)
    pygame.draw.aaline(ecran,blanc, (largeur_ecran/2,2), (largeur_ecran/2,longueur_ecran))
  
#affichage score
    score_joueur = police_jeu.render(f"{point_joueur}",False,(156,169,184))
    ecran.blit(score_joueur,(largeur_ecran*3/4,longueur_ecran/2))
    
    score_ennemi = police_jeu.render(f"{point_ennemi}",False,(156,169,184))
    ecran.blit(score_ennemi,(largeur_ecran/4,longueur_ecran/2)) 
    
    pygame.display.flip()
    chrono.tick(60)
    
#fin jeu
    if point_joueur == 5:
        run = False
    if point_ennemi == 5:
        run = False
