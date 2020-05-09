# -*- coding: utf-8 -*-

# Module pour toutes les animations en tout genre
import pygame
from ressource import Option

n = 0
p = 0
frame = 0
option = Option()

width = option.w  # caractéristiques de la fenêtre
height = option.h
# ratio qui aide à redimensionner tous les éléments graphiques
# si égal à 1, veut dire que le jeu est dans les dimensions de base c'est à dire 1920*1080

dialogue_x = 50
dialogue_y = 520
pygame.display.init()
# on crée une chaîne vide pour  conserver les anciennes lettres dans animation_text
string = ""
# les processus de passage et de fin sont de base désactivés

white = pygame.Color(255, 255, 255)  # référence RGB du blanc
black = pygame.Color(0, 0, 0)  # référence RGB du noir
red = pygame.Color(255, 0, 0)

# Prédisposition pour que le son marche bien
pygame.mixer.pre_init(44100, -16, 1, 512)
# on démarre le module de l'écran
pygame.display.init()
# on démarre le son
pygame.mixer.init()

# on charge le son de lecture des textes
sfx_dialogue = pygame.mixer.Sound("text.wav")
# et on baisse le son
sfx_dialogue.set_volume(0.2)
loading = pygame.image.load  # pour que ce soit plus rapide pour charger des images
# et on charge les images nécessaires
rememberStrings = []
factor = 0
spaces = 0
testline = ""


# imprime la totalité du texte avec la syntaxe
def structuration(text, font, first_x, first_y):
    dialogue_x, dialogue_y = first_x, first_y
    listword = text.split(" ")
    string = ""
    newtext = []
    for i, elt in enumerate(listword):
        string += elt + " "
        if font.size(string)[0] >= 980:
            string = string.replace(elt, "")
            newtext.append((font.render(string, False, white), (dialogue_x, dialogue_y)))
            string = elt + " "
            dialogue_x = first_x
            dialogue_y += font.size(text)[1] + 2

        if i == len(listword) - 1:
            newtext.append((font.render(string, False, white), (dialogue_x, dialogue_y)))

    return newtext


def animation_text(text, screen, sprite, dialogue_box, curseur, level, nb_dialogue, nb_final, emotion):
    global dialogue_x, dialogue_y, rememberStrings, font
    global string
    global n, frame, p, factor, spaces, testline
    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf", 30)
    frameP = 0
    listwords = text.split(" ")

    def face(screen, n, frame, face, frame_nb, PosX, PosY, emotion):
        if emotion is None:
            pass
        else:
            i = n % frame_nb
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

            screen.blit(face[frame], (PosX, PosY))

    DposX  = 33
    if sprite.y < int(option.h/2):
        DposY = 500
    else:
        DposY = 500
    first_x, first_y = DposX + 17, DposY + 20

    # on affiche la boite de dialogue
    screen.blit(dialogue_box, (DposX, DposY))
    # et le texte qui a déjà été affiché
    for elt in rememberStrings:
        screen.blit(font.render(elt, False, white), (first_x, first_y + (font.size(text)[1] + 2) * factor))
        factor += 1
        if factor == len(rememberStrings):
            factor = 0

    face(screen, n, frameP, sprite.bounce, 42, DposX + 947, DposY - 152, emotion)
    # si les commandes sont actives
    if sprite.commande_get():
        # On les désactive et on active l'animation du texte
        sprite.set_commande(False)
        sprite.set_animation(True)
        dialogue_x = first_x
        dialogue_y = first_y

    if not sprite.animation_get() and not sprite.passer:
        # si c'est la 60ème frame
        p = n % 60
        # on affiche tout le texte
        for elt in structuration(text, font, first_x, first_y):
            screen.blit(elt[0], elt[1])
        # puis on fait l'animation en 4 images
        if p < 15 or p >= 30 and p < 45:
            frame = 0
        elif p >= 15 and p < 30 or p >= 45:
            frame = 1
        screen.blit(curseur[frame], (DposX + 585, DposY + 150))
        # puis on incrémente pour simuler les frames
        n += 1

    if sprite.SInput:
        # Si l'animation est en cours
        if sprite.animation_get():
            # on active le processus de passage
            sprite.passer = True
            # si le processus de fin est activé
        elif sprite.finir:
            # on réinitialise les variables
            n = 0
            string = ""
            testline = ""
            rememberStrings = []
            spaces = 0
            sprite.finir = False
            dialogue_x = first_x
            dialogue_y = first_y
            # et on désactive les dialogues et active les commandes
            if nb_dialogue + 1 == nb_final:
                sprite.set_dialogue(False)
                sprite.set_commande(True)
            else:
                sprite.set_commande(True)
            nb_dialogue += 1
        sprite.SInput = False

    # si processus de passage activé
    if sprite.passer:
        # on affiche le texte en entier
        for elt in structuration(text, font, first_x, first_y):
            screen.blit(elt[0], elt[1])

        # on désactive l'animation
        sprite.set_animation(False)
        # et on désactive le processus de passage et active le processus de fin
        sprite.passer = False
        sprite.finir = True

    # si le processus d'animation est activé    
    if sprite.animation_get():
        print("lol",string, text[n], text)
        # puis on fait afficher les lettres déjà passées
        j = font.render(string, False, white)
        screen.blit(j, (first_x, dialogue_y))
        # puis on ajoute la lettre suivante à string pour la réafficher à la prochaine frame
        string += text[n]
        # puis on affiche la prochaine lettre au coordonnées données
        i = font.render(text[n], False, white)
        screen.blit(i, (dialogue_x, dialogue_y))
        if text[n] == " ":
            if testline == "" and rememberStrings == []:
                testline += listwords[0] + " "
            spaces += 1
            testline += listwords[spaces] + " "
        # une frame sur quatre
        if n % 4 == 0:
            # jouer le son de texte
            sfx_dialogue.play()
        # on ajoute la taille d'un caractère pour donner l'impression
        # que c'est comme dans un logiciel de traitement de texte
        dialogue_x += font.size(text)[0] / len(text)

        if font.size(testline)[0] >= 980:
            dialogue_y += font.size(text)[1] + 2
            dialogue_x = first_x
            rememberStrings.append(string)
            string = ""
            testline = listwords[spaces] + " "
            # puis on incrémente pour simuler les frames
        n += 1

    # si la dernière lettre a été affichée
    if n == len(text):
        # on désactive le processus d'animation et on active le processus de fin
        sprite.set_animation(False)
        sprite.finir = True
    # si animation désactivée
    return nb_dialogue
