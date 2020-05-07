# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 12:24:56 2019

@author: youss
"""
import pygame


# variable utiles pour les algorithmes plus bas qui sont réinitialisé
class Option:

    def __init__(self):
        self.w = 1280
        self.h = 720
        self.mw = int(self.w / 2)
        self.mh = int(self.h / 2)

    # Pour redimensionner la fenêtre
    def dimension(self, screen):
        if screen.get_flags() & pygame.RESIZABLE:
            screen = pygame.display.set_mode((self.w, self.h), pygame.FULLSCREEN)

        else:
            screen = pygame.display.set_mode((self.w, self.h), pygame.RESIZABLE)

        return screen


option = Option()

nP = 0

frameP = 0

pygame.display.init()

# ratio qui aide à redimensionner tous les éléments graphiques
# si égal à 1, veut dire que le jeu est dans les dimensions de base c'est à dire 1920*1080    ratiox = width/1920

# coordonnées du texte dans les dialogues
loading = pygame.image.load


class Chara(pygame.sprite.Sprite):  # Classe pour définir les attributs d'un sprite rapidement

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
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = widthP
        self.height = heightP
        self.speed = speed
        self.VelY = 0
        self.VelX = 0

        self.front = True
        self.back = False
        self.right = False
        self.left = False
        self.walk = False

        self.dialogue = False
        self.commande = True
        self.animation = False
        self.passer = False
        self.finir = False
        self.SInput = False

        self.cameraX = self.x
        self.cameraY = self.y

        self.picfront = front
        self.picback = back
        self.picright = right
        self.picleft = left
        self.picWfront = Wfront
        self.picWright = Wright
        self.picWleft = Wleft
        self.picRfront = Rfront
        self.picRback = Rback
        self.picRright = Rright
        self.picRleft = Rleft
        self.picRWfront = RWfront
        self.picRWright = RWright
        self.picRWleft = RWleft

        self.rect = front[0].get_rect()
        self.uprect = pygame.Rect(self.x, self.y, widthP, 2*int(heightP/3))
        self.downrect = pygame.Rect(self.x, self.y + 2*int(heightP/3), widthP, int(heightP/3))
        self.rect.x = self.x
        self.rect.y = self.y
        self.bounce = bounce

    def __iter__(self):
        return self

    def standing(self, screen):  # frame à l'image quand il marche sur la carte
        global frameP, nP

        # affiche le sprite de face et etc grâce aux valeurs
        # données par la rubriques Commandes dans PopsBizarreAdventure.py

        nP = nP % 208  # toutes les 208 frames

        if nP % 52 < 11:
            frameP = 0
        elif nP % 52 >= 12 and nP % 52 < 23:
            frameP = 1
        elif nP % 52 >= 24 and nP % 52 < 29:
            frameP = 2
        elif nP % 52 >= 30 and nP % 52 < 35:
            frameP = 3
        elif nP % 52 >= 36 and nP % 52 < 41:
            frameP = 4
        elif nP % 52 >= 42 and nP % 52 < 53:
            frameP = 5
        nP += 1

        if self.front:
            if nP <= 156:
                screen.blit(self.picfront[frameP], (self.cameraX, self.cameraY))
            else:
                screen.blit(self.picWfront[frameP], (self.cameraX, self.cameraY))

        elif self.right:
            if nP <= 156:
                screen.blit(self.picright[frameP], (self.cameraX, self.cameraY))
            else:
                screen.blit(self.picWright[frameP], (self.cameraX, self.cameraY))

        elif self.back:
            screen.blit(self.picback[frameP], (self.cameraX, self.cameraY))

        elif self.left:
            if nP <= 156:
                screen.blit(self.picleft[frameP], (self.cameraX, self.cameraY))
            else:
                screen.blit(self.picWleft[frameP], (self.cameraX, self.cameraY))
                if nP == 208:
                    nP = 0

    def walking(self, screen):
        global nP, frameP
        nP = nP % 216  # toutes les 208 frames

        if nP % 54 < 9:
            frameP = 0
        elif nP % 54 >= 9 and nP % 54 < 18:
            frameP = 1
        elif nP % 54 >= 18 and nP % 54 < 27:
            frameP = 2
        elif nP % 54 >= 27 and nP % 54 < 36:
            frameP = 3
        elif nP % 54 >= 36 and nP % 54 < 45:
            frameP = 4
        elif nP % 54 >= 45 and nP % 54 < 54:
            frameP = 5
        nP += 1

        if self.front:
            if nP <= 156:
                screen.blit(self.picRfront[frameP], (self.cameraX, self.cameraY))
            else:
                screen.blit(self.picRWfront[frameP], (self.cameraX, self.cameraY))

        elif self.right:
            if nP <= 156:
                screen.blit(self.picRright[frameP], (self.cameraX, self.cameraY))
            else:
                screen.blit(self.picRWright[frameP], (self.cameraX, self.cameraY))

        elif self.back:
            screen.blit(self.picRback[frameP], (self.cameraX, self.cameraY))

        elif self.left:
            if nP <= 156:
                screen.blit(self.picRleft[frameP], (self.cameraX, self.cameraY))
            else:
                screen.blit(self.picRWleft[frameP], (self.cameraX, self.cameraY))
                if nP == 208:
                    nP = 0
        self.rect.x = self.x
        self.rect.y = self.y
        self.uprect.x, self.uprect.y = self.x, self.y
        self.downrect.x, self.downrect.y = self.x, self.y + 2*int(self.height/3)

    # Pour aller plus vite, j'ai créé des méthodes qui tournent le sprite
    def set_right(self):
        self.right = True
        self.left = False
        self.front = False
        self.back = False

    def set_left(self):
        self.right = False
        self.left = True
        self.front = False
        self.back = False

    def set_front(self):
        self.right = False
        self.left = False
        self.front = True
        self.back = False

    def set_back(self):
        self.right = False
        self.left = False
        self.front = False
        self.back = True

    # Je vais mettre des accesseurs et des mutateurs maintenant
    def dialogue_get(self):
        return self.dialogue

    def commande_get(self):
        return self.commande

    def animation_get(self):
        return self.animation

    # mutateurs
    def set_dialogue(self, state):
        self.dialogue = state

    def set_commande(self, state):
        self.commande = state

    def set_animation(self, state):
        self.animation = state

    def collision(self, furnitures, scrolling, scrollingX, scrollingY):
        collision = False
        # pour chaque objet sur la carte
        for elt in furnitures:
            if not collision:
                if elt.rect.center[1] <= self.downrect.top:
                    rect = self.downrect
                else:
                    rect = self.uprect
                # on vérifie les collisions
                if elt.rect.colliderect(rect):
                    # si l'axe en question est celle horizontale
                    if self.VelX != 0:
                        # s'il est à gauche de l'objet
                        if elt.rect.left < rect.right < elt.rect.right:
                            # on pousse le joueur au bord de l'objet et on arrête le scrolling et la marche
                            self.x = elt.rect.left - rect.w
                            rect.right = elt.rect.left
                            self.walk = False
                            scrolling.stateEvent = False
                            # s'il est à droite
                        if rect.left < elt.rect.right < rect.right:
                            # idem
                            self.x = rect.left = elt.rect.right
                            self.walk = False
                            scrolling.stateEvent = False
                    # si l'axe en question est celle verticale
                    if self.VelY != 0:
                        # s'il est en haut
                        if rect.bottom >= elt.rect.top and self.x + rect.w > elt.rect.left:
                            self.y = elt.rect.top - rect.w
                            rect.bottom = elt.rect.top
                            self.walk = False
                            scrolling.stateEvent = False
                        # s'il est en bas
                        if rect.top <= elt.rect.bottom:
                            self.y = elt.rect.bottom
                            rect.top = elt.rect.bottom
                            self.walk = False
                            scrolling.stateEvent = False
                    collision = True
                # si le joueur se situe sur les bords de l'objet à gauche ou à droite
                if elt.rect.bottom >= rect.top and rect.bottom >= elt.rect.top:
                    # s'il bouge horizontalement
                    if self.VelX != 0 and rect.right <= elt.rect.left or self.VelX != 0 \
                            and rect.left >= elt.rect.right:
                        # s'il est à gauche de l'objet
                        if self.VelX > 0 and rect.right + self.VelX >= elt.rect.left >= self.x:
                            print("miaou")
                            self.walk = False
                            scrolling.stateEvent = False
                            self.x = elt.rect.left - rect.w
                            collision = True
                        # s'il est à droite
                        elif self.VelX < 0 and rect.left + self.VelX <= elt.rect.right and self.x >= elt.rect.left:
                            self.walk = False
                            scrolling.stateEvent = False
                            self.x = elt.rect.right
                            collision = True
                        # s'il n'est pas proche de l'objet on ne fait rien
                        else:
                            self.walk = True
                            scrolling.stateEvent = True
                    # si on bouge verticalement sur les bords verticaux
                    if self.VelY != 0 and rect.right <= elt.rect.left:

                        # si on bouge à gauche
                        if self.VelX >= 0 and rect.right + abs(self.VelX) >= elt.rect.left >= self.right:
                            self.walk = True
                            scrolling.stateEvent = True
                            scrollingX.stateEvent = False
                            collision = True
                            rect.right = elt.rect.left
                        else:
                            scrollingX.stateEvent = True
                    if self.VelY != 0 and rect.left >= elt.rect.right:
                        # si on bouge à droite
                        if self.VelX <= 0 and rect.left - abs(self.VelX) <= elt.rect.right <= self.x:
                            self.walk = True
                            scrolling.stateEvent = True
                            scrollingX.stateEvent = False
                            collision = True
                            self.x = elt.rect.right
                        else:
                            scrollingX.stateEvent = True
                else:
                    scrollingX.stateEvent = True
                # si on se situe en dessous ou au dessus de l'objet
                if elt.rect.left <= rect.right and rect.left <= elt.rect.right:
                    # si on bouge verticalement
                    if self.VelY != 0 and rect.bottom <= elt.rect.top or self.VelY != 0 \
                            and rect.top >= elt.rect.bottom:
                        # si on bouge en haut de l'objet
                        if self.VelY > 0 and rect.bottom + self.VelY >= elt.rect.top > self.y:
                            self.walk = False
                            scrolling.stateEvent = False
                            self.y = elt.rect.top - rect.h
                            collision = True
                        # sinon si on bouge en dessous de l'objet
                        elif self.VelY < 0 and rect.top + self.VelY <= elt.rect.bottom < rect.bottom:
                            self.walk = False
                            scrolling.stateEvent = False
                            collision = True
                            if elt.rect.center[1] <= rect.top:
                                self.y = rect.top - 2 * rect.h
                            else:
                                self.y = elt.rect.bottom
                        # si pas assez proche on ne fait rien
                        else:
                            self.walk = True
                            scrolling.stateEvent = True
                    # si on bouge horizontalement sur les bords horizontaux
                    if self.VelX != 0 and rect.bottom <= elt.rect.top:
                        # si c'est en haut
                        if self.VelY >= 0 and rect.bottom + abs(self.VelY) >= elt.rect.top >= rect.bottom:
                            self.walk = True
                            scrolling.stateEvent = True
                            scrollingY.stateEvent = False
                            self.y = elt.rect.top - rect.h
                            collision = True
                        else:
                            scrollingY.stateEvent = True
                    if self.VelX != 0 and rect.top >= elt.rect.bottom:
                        # si c'est en bas
                        if self.VelY <= 0 and rect.top - abs(self.VelY) <= elt.rect.bottom < rect.bottom:
                            self.walk = True
                            scrolling.stateEvent = True
                            scrollingY.stateEvent = False
                            collision = True
                            if elt.rect.center[1] <= rect.top:
                                self.y = rect.top - 2 * rect.h
                            else:
                                self.y = elt.rect.bottom
                        else:
                            scrollingY.stateEvent = True
                else:
                    scrollingY.stateEvent = True


class Event:

    def __init__(self):
        self.stateEvent = False

    def get_state(self):
        return self.stateEvent

    def set_state(self, state):
        self.stateEvent = state


class Scene:

    def __init__(self, picture, PosX, PosY):
        self.picture = picture
        self.PosX = PosX
        self.PosY = PosY
        self.width, self.height = picture.get_rect().size

        self.initialPosX = PosX
        self.initialPosY = PosY
        self.furnitures = []
        self.VelX = 0
        self.VelY = 0

    def __iter__(self):
        return self

    def draw(self, screen):
        screen.blit(self.picture, (self.PosX, self.PosY))
        for elt in self.furnitures:
            elt.level = self

    def addFurnitures(self, furniture):
        self.furnitures.append(furniture)


class Object(Scene, pygame.sprite.Sprite):

    def __init__(self, picture, level, ownX, ownY):
        pygame.sprite.Sprite.__init__(self)
        self.picture = picture
        self.fakerect = self.picture.get_rect()
        self.level = level
        self.ownX = ownX
        self.ownY = ownY
        self.PosX = self.level.PosX + self.ownX
        self.PosY = self.level.PosY + self.ownY
        self.fakerect.x = self.PosX
        self.fakerect.y = self.PosY
        self.rect = picture.get_rect()
        self.rect.x = self.PosX
        self.rect.y = self.PosY

    def draw(self, screen):
        self.PosX = self.level.PosX + self.ownX
        self.PosY = self.level.PosY + self.ownY
        self.fakerect.x, self.fakerect.y = self.PosX, self.PosY
        screen.blit(self.picture, (self.PosX, self.PosY))

class Inventory:
    def __init__(self):
        self.inventory = []


class Item:
    def __init__(self,picture,description):
        self.picture