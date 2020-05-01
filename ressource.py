# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:24:56 2019

@author: youss
"""
import pygame
#variable utiles pour les algorithmes plus bas qui sont réinitialisé
class Option:
    
    def __init__(self):
        self.w  = 1280
        self.h  = 720
        self.mw = int(self.w/2)
        self.mh = int(self.h/2)
    # Pour redimensionner la fenêtre
    def dimension(self,screen):
        if screen.get_flags() & pygame.RESIZABLE:
            screen = pygame.display.set_mode((self.w,self.h),pygame.FULLSCREEN)
        
        else:
            screen = pygame.display.set_mode((self.w,self.h),pygame.RESIZABLE)
        
        return screen
option = Option()

nP = 0

frameP = 0

pygame.display.init()

#ratio qui aide à redimensionner tous les éléments graphiques
#si égal à 1, veut dire que le jeu est dans les dimensions de base c'est à dire 1920*1080    ratiox = width/1920

#coordonnées du texte dans les dialogues
loading = pygame.image.load

class Chara: #Classe pour définir les attributs d'un sprite rapidement
    
    
    def __init__(self, x, y, widthP, heightP, speed,
    front,
    back, 
    right,
    left,
    Wfront,
    Wright,
    Wleft,
    Rfront,
    Rback,
    Rright,
    Rleft,
    RWfront, 
    RWright,
    RWleft,
    bounce):
        self.x = x
        self.y = y 
        self.width = widthP 
        self.height= heightP 
        self.speed = speed 
        self.VelX  = 0
        self.VelY  = 0
        
        
        self.front = True
        self.back  = False
        self.right = False
        self.left  = False
        self.walk  = False
        
        
        self.dialogue = False
        self.commande = True
        self.animation = False
        self.passer    = False
        self.finir     = False
        self.SInput    = False
        
        self.cameraX = self.x
        self.cameraY = self.y
        
        
        self.picfront   = front
        self.picback    = back
        self.picright   = right
        self.picleft    = left
        self.picWfront  = Wfront
        self.picWright  = Wright
        self.picWleft   = Wleft
        self.picRfront  = Rfront
        self.picRback   = Rback
        self.picRright  = Rright
        self.picRleft   = Rleft
        self.picRWfront = RWfront
        self.picRWright = RWright
        self.picRWleft  = RWleft
        
        self.hitbox     = pygame.Rect((self.x,self.y),front[0].get_rect().size)
        self.uphitbox   = pygame.Rect((self.x,self.y),(int(front[0].get_rect().size[0]/2),int(front[0].get_rect().size[1]/2)))
        self.downhitbox = pygame.Rect((self.x + int(front[0].get_rect().size[0]/2),self.y + int(front[0].get_rect().size[1]/2)),(int(front[0].get_rect().size[0]/2),int(front[0].get_rect().size[1]/2)))
       
        self.bounce     = bounce        
        
        
    def __iter__(self):
        return self
   
    
    def standing(self,screen): #frame à l'image quand il marche sur la carte
        global frameP,nP
            
       
            #affiche le sprite de face et etc grâce aux valeurs
            #données par la rubriques Commandes dans PopsBizarreAdventure.py
            
        nP = nP % 208 # toutes les 208 frames
            
        if nP%52 < 11:
            frameP = 0
        elif nP%52 >= 12 and nP%52 < 23:
            frameP = 1
        elif nP%52 >= 24 and nP%52 < 29:
            frameP = 2
        elif nP%52 >= 30 and nP%52 < 35:
            frameP = 3
        elif nP%52 >= 36 and nP%52 < 41:
            frameP = 4
        elif nP%52 >= 42 and nP%52 < 53:
            frameP = 5
        nP += 1
        
        if self.front:
            if nP <= 156:
                screen.blit(self.picfront[frameP], (self.cameraX,self.cameraY))
            else:
                screen.blit(self.picWfront[frameP], (self.cameraX,self.cameraY))
            
        elif self.right:
            if nP <= 156:
                screen.blit(self.picright[frameP], (self.cameraX,self.cameraY))
            else:
                screen.blit(self.picWright[frameP], (self.cameraX,self.cameraY))
            
        elif self.back:    
            screen.blit(self.picback[frameP], (self.cameraX,self.cameraY))
        
        elif self.left:
            if nP <= 156:
                screen.blit(self.picleft[frameP], (self.cameraX,self.cameraY)) 
            else:
                screen.blit(self.picWleft[frameP], (self.cameraX,self.cameraY))
                if nP == 208:
                    nP = 0
        self.hitbox.move(self.x,self.y)
        self.uphitbox.move(self.x,self.y)
        self.downhitbox.move(self.x + int(self.picfront[0].get_rect().size[0]/2),self.y + int(self.picfront[0].get_rect().size[1]/2))
    def walking(self, screen):
        global nP, frameP
        nP = nP % 216 # toutes les 208 frames
            
        if nP%54 < 9:
            frameP = 0
        elif nP%54 >= 9 and nP%54 < 18:
            frameP = 1
        elif nP%54 >= 18 and nP%54 < 27:
            frameP = 2
        elif nP%54 >= 27 and nP%54 < 36:
            frameP = 3
        elif nP%54 >= 36 and nP%54 < 45:
            frameP = 4
        elif nP%54 >= 45 and nP%54 < 54:
            frameP = 5
        nP += 1
        
        if self.front:
            if nP <= 156:
                screen.blit(self.picRfront[frameP], (self.cameraX,self.cameraY))
            else:
                screen.blit(self.picRWfront[frameP], (self.cameraX,self.cameraY))
            
        elif self.right:
            if nP <= 156:
                screen.blit(self.picRright[frameP], (self.cameraX,self.cameraY))
            else:
                screen.blit(self.picRWright[frameP], (self.cameraX,self.cameraY))
            
        elif self.back:    
            screen.blit(self.picRback[frameP], (self.cameraX,self.cameraY))
        
        elif self.left:
            if nP <= 156:
                screen.blit(self.picRleft[frameP], (self.cameraX,self.cameraY)) 
            else:
                screen.blit(self.picRWleft[frameP], (self.cameraX,self.cameraY))
                if nP == 208:
                    nP = 0
        self.hitbox.move(self.x,self.y)
        self.uphitbox.move(self.x,self.y)
        self.downhitbox.move(self.x + int(self.picfront[0].get_rect().size[0]/2),self.y + int(self.picfront[0].get_rect().size[1]/2))
    #Pour aller plus vite, j'ai créé des méthodes qui tournent le sprite
    def set_right(self):
        self.right = True
        self.left  = False
        self.front = False
        self.back  = False
        
    def set_left(self):
        self.right = False
        self.left  = True
        self.front = False
        self.back  = False
        
    def set_front(self):
        self.right = False
        self.left  = False
        self.front = True
        self.back  = False
        
    def set_back(self):
        self.right = False
        self.left  = False
        self.front = False
        self.back  = True
    
    #Je vais mettre des accesseurs et des mutateurs maintenant
    def dialogue_get(self):
        return self.dialogue
    
    def commande_get(self):
        return self.commande
    
    def animation_get(self):
        return self.animation
    # mutateurs
    def set_dialogue(self,state):
        self.dialogue = state
    
    def set_commande(self,state):
       self.commande = state
        
    def set_animation(self,state):
        self.animation = state

class Event:
    
    def __init__(self):
        self.stateEvent = False
    
    def get_state(self):
        return self.stateEvent
    def set_state(self,state):
        self.stateEvent = state
   

        

    

class Scene:
    
    def __init__(self,picture,PosX,PosY):
        
        self.picture = picture
        self.PosX = PosX
        self.PosY = PosY
        self.width, self.height = picture.get_rect().size
        
        self.initialPosX = PosX
        self.initialPosY = PosY
        self.furnitures = []
    
    def __iter__(self):
        return self
    
    def draw(self,screen):
        
        screen.blit(self.picture,(self.PosX,self.PosY))
    
    def addFurnitures(self,furniture):
        self.furnitures.append(furniture)
    
class Object(Scene):
    
    def __init__(self,picture,PosX,PosY,ownX,ownY):
        Scene.__init__(self,picture,PosX,PosY)
        self.hitbox = pygame.Rect((self.PosX,self.PosY),(self.width,self.height))
        self.ownX = ownX
        self.ownY = ownY


    def newPosition(self,x,y):
        self.PosX = x
        self.PosY = y
    
    def draw(self,screen):
        Scene.draw(self,screen)
        self.hitbox.move(self.PosX,self.PosY)
        
        
    
        
        
