# -*- coding: utf-8 -*-

# Module pour toutes les animations en tout genre
import pygame
from ressource import Option
n = 0
p = 0
frame = 0
option = Option()

width   = option.w  # caractéristiques de la fenêtre
height  = option.h
#ratio qui aide à redimensionner tous les éléments graphiques
#si égal à 1, veut dire que le jeu est dans les dimensions de base c'est à dire 1920*1080    

dialogue_x = 50
dialogue_y = 520
pygame.display.init()
#on garde les valeurs initiales dans d'autres variables
first_x = dialogue_x
first_y = dialogue_y
#on crée une chaîne vide pour  conserver les anciennes lettres dans animation_text
string = ""
#les processus de passage et de fin sont de base désactivés

white = pygame.Color(255,255,255) #référence RGB du blanc
black = pygame.Color(0,0,0) #référence RGB du noir
red   = pygame.Color(255,0,0)

#Prédisposition pour que le son marche bien 	
pygame.mixer.pre_init(44100, -16, 1, 512)
#on démarre le module de l'écran
pygame.display.init()
#on démarre le son
pygame.mixer.init()

#on charge le son de lecture des textes
sfx_dialogue = pygame.mixer.Sound("text.wav")
#et on baisse le son
sfx_dialogue.set_volume(0.2)
loading     = pygame.image.load #pour que ce soit plus rapide pour charger des images  
#et on charge les images nécessaires


def animation_text(text,screen,sprite,dialogue_box,curseur,level):
    global dialogue_x,dialogue_y,first_x,first_y
    global string
    global n,frame,p
    frameP = 0
    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf",26)   
    pygame.event.clear()
    
    def face(screen,n,frame,face,frame_nb,PosX,PosY):
        i = n%frame_nb
        if i < 6:
            frame = 0
        elif 6 <= i < 18:
            frame = 1
        elif 18 <= i < 30:
            frame = 2
        elif 30 <= i < 42:
            frame = 3
        if i >= 42:
            frame = 4
        
        screen.blit(face[frame],(PosX,PosY))
    DposX, DposY = 33, 500
    
    #une frame sur deux
    #on affiche la boite de dialogue
    if n%2 == 0:
        screen.blit(dialogue_box,(DposX,DposY))
        face(screen, n, frameP, sprite.bounce,42,980,348)
    else:
        #on affiche la boite de dialogue
        screen.blit(dialogue_box,(DposX,DposY))
        #et le texte qui a déjà été affiché
        screen.blit(font.render(string,False,white),(first_x,first_y))
        face(screen, n, frameP, sprite.bounce,42,980,348)
    #si les commandes sont actives
    if sprite.commande_get():
        #On les désactive et on active l'animation du texte
        sprite.set_commande(False)
        sprite.set_animation(True)
    
    if not sprite.animation_get()and not sprite.passer:
        #si c'est la 60ème frame
        p = n%60     
        #on affiche tout le texte
        i = font.render(text, False, white)
        screen.blit(i,(first_x,first_y))
        #puis on fait l'animation en 4 images
        if p<15 or p >= 30 and p < 45: 
            frame = 0
        elif p >= 15 and p < 30 or p >= 45:
            frame = 1
        screen.blit(curseur[frame],(630,685))
        pygame.display.update()
        # puis on incrémente pour simuler les frames
        n += 1
          
    if sprite.SInput:
        #Si l'animation est en cours
        if sprite.animation_get():
            #on active le processus de passage
            sprite.passer = True
            #si le processus de fin est activé
        elif sprite.finir:
            #on réinitialise les variables
            n = 0
            string = ""
            sprite.finir = False
            screen.fill(black)
            dialogue_x = first_x
            dialogue_y = first_y
            #et on désactive les dialogues et active les commandes
            sprite.set_dialogue(False)
            sprite.set_commande(True)
            level.draw(screen)
            sprite.walking(screen)
        sprite.SInput = False
    
    
    #si processus de passage activé
    if sprite.passer:
        #on affiche le texte en entier
        i = font.render(text, False, white)
        screen.blit(i,(first_x,first_y))
        #on désactive l'animation
        sprite.set_animation(False) 
        #et on désactive le processus de passage et active le processus de fin
        sprite.passer = False
        sprite.finir = True

    # si le processus d'animation est activé    
    if sprite.animation_get():

        #puis on fait afficher les lettres déjà passées
        j = font.render(string,False,white) 
        screen.blit(j,(first_x,first_y))
        #puis on ajoute la lettre suivante à string pour la réafficher à la prochaine frame
        string += text[n]
        #puis on affiche la prochaine lettre au coordonnées données
        i = font.render(text[n],False,white)
        screen.blit(i,(dialogue_x,dialogue_y))
        #une frame sur quatre
        if n%4 == 0:
            #jouer le son de texte
            sfx_dialogue.play()
        #on ajoute la taille d'un caractère pour donner l'impression
        #que c'est comme dans un logiciel de traitement de texte
        dialogue_x += font.size(text)[0] / len(text) 
        if dialogue_x >= 980:
            dialogue_y += font.size(text)[1] + 2
            dialogue_x = first_x
        #puis on incrémente pour simuler les frames
        n += 1
    #si la dernière lettre a été affichée
    if n == len(text) - 1:
        #on désactive le processus d'animation et on active le processus de fin
        sprite.set_animation(False)
        sprite.finir = True
    # si animation désactivée
    
