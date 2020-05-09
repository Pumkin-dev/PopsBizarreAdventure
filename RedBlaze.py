# -*- coding: utf-8 -*-

# enlève le message welcome from pygame
import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# règle le problème de l'icône dans la barre des tâches
import ctypes

myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import pygame
from ressource import Chara, Event, Option, Scene, Object
from DialogueBox import animation_text


# définition d'une fonction qui lance le menu principal au lancement du jeu
def main():
    option = Option()

    width = option.w  # caractéristiques de la fenêtre
    height = option.h
    black = pygame.Color(0, 0, 0)  # crée un objet couleur  en ayant référence RGB du noir
    fade = pygame.Surface((width, height))
    fade.fill((0, 0, 0))
    bisfade = pygame.Surface((width, height))
    bisfade.fill((0, 0, 0))
    fade.set_alpha(0)
    bisfade.set_alpha(255)
    white = pygame.Color(255, 255, 255)  # crée un objet couleur  en ayant référence RGB du blanc
    red = pygame.Color(255, 0, 0)  # de même
    blue = pygame.Color(0, 0, 255)
    green = pygame.Color(0, 255, 0)

    loading = pygame.image.load  # pour que ce soit plus rapide pour charger des images
    icon = loading("images/logo.png")
    # le titre en fenêtre de jeu
    pygame.display.set_caption("Red Blaze")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((width, height),
                                     pygame.RESIZABLE)  # pour ouvrir une fenêtre aux dimensions height width

    frontpops = []
    backpops = []
    rightpops = []
    leftpops = []
    Wfrontpops = []
    Wrightpops = []
    Wleftpops = []
    Rfrontpops = []
    Rbackpops = []
    Rrightpops = []
    Rleftpops = []
    RWfrontpops = []
    RWrightpops = []
    RWleftpops = []
    bouncepops = []
    dubitatifpops = []
    dubitatif_bispops = []
    for i in range(6):
        frontpops.append(loading("images/sprite_standing/front/normal/front{}.png".format(i + 1)).convert_alpha())

        backpops.append(loading("images/sprite_standing/back/back{}.png".format(i + 1)).convert_alpha())

        rightpops.append(loading("images/sprite_standing/right/normal/right{}.png".format(i + 1)).convert_alpha())

        leftpops.append(loading("images/sprite_standing/left/normal/left{}.png".format(i + 1)).convert_alpha())

        Wfrontpops.append(loading("images/sprite_standing/front/wink/front{}.png".format(i + 1)).convert_alpha())

        Wrightpops.append(loading("images/sprite_standing/right/wink/right{}.png".format(i + 1)).convert_alpha())

        Wleftpops.append(loading("images/sprite_standing/left/wink/left{}.png".format(i + 1)).convert_alpha())

        Rfrontpops.append(loading("images/sprite_walking/front/normal/front{}.png".format(i + 1)).convert_alpha())

        Rbackpops.append(loading("images/sprite_walking/back/back{}.png".format(i + 1)).convert_alpha())

        Rrightpops.append(loading("images/sprite_walking/right/normal/right{}.png".format(i + 1)).convert_alpha())

        Rleftpops.append(loading("images/sprite_walking/left/normal/left{}.png".format(i + 1)).convert_alpha())

        RWfrontpops.append(loading("images/sprite_walking/front/wink/front{}.png".format(i + 1)).convert_alpha())

        RWrightpops.append(loading("images/sprite_walking/right/wink/right{}.png".format(i + 1)).convert_alpha())

        RWleftpops.append(loading("images/sprite_walking/left/wink/left{}.png".format(i + 1)).convert_alpha())

    for i in range(4):
        bouncepops.append(loading("images/dialogue/face_discussion/bounce/bounce{}.png ".format(i + 1)).convert_alpha())
        dubitatifpops.append(loading("images/dialogue/face_discussion"
                                     +"/dubitatif/dubitatif{}.png ".format(i + 1)).convert_alpha())
        dubitatif_bispops.append(loading("images/dialogue/face_discussion"
                                          + "/dubitatif2/dubitatif_bis{}.png ".format(i + 1)).convert_alpha())

    bar = loading("images/level/background/bar.png").convert_alpha()
    dialogue_box = loading("images/dialogue/dialogue_box.png").convert()

    curseur = [loading("images/dialogue/curseur/Sprite-0001.png").convert_alpha(),
               loading("images/dialogue/curseur/Sprite-0002.png").convert_alpha()]

    initialPosX = 600
    initialPosY = 400

    widthPops, heightPops = backpops[0].get_rect().size
    velPops = 5

    Pops = Chara(initialPosX, initialPosY, widthPops, heightPops, velPops, frontpops,
                 backpops,
                 rightpops,
                 leftpops,
                 Wfrontpops,
                 Wrightpops,
                 Wleftpops,
                 Rfrontpops,
                 Rbackpops,
                 Rrightpops,
                 Rleftpops,
                 RWfrontpops,
                 RWrightpops,
                 RWleftpops,
                 bouncepops,
                 dubitatifpops,
                 dubitatif_bispops)  # toutes les caractéristiques de Pops

    # toutes les caractéristiques pour le scrolling
    # on prend la moitié de l'écran pour le début du scrolling 
    startScrollingX = option.mw
    startScrollingY = option.mh

    Bar = Scene(bar, 500, -300)
    table1 = loading("images/level/objects/table1.png")
    Table1 = Object(table1, Bar, 256, 716)
    Table2 = Object(table1, Bar, 256*2, 716)
    Table3 = Object(table1, Bar, 256*3, 716)
    Bar.addFurnitures(Table1)
    Bar.addFurnitures(Table2)
    Bar.addFurnitures(Table3)
    # initialize the pygame module
    pygame.init()
    # On initialise le son (si jamais)
    pygame.mixer.init()

    startScrollingX = option.mw
    startScrollingY = option.mh

    # active le module de texte
    pygame.font.init()

    # La police d'écriture du jeu
    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf", 30)

    # define a variable to control the main loop
    running = True

    # Textes pour tester les boites de dialogues
    text = "Mais comment veux-tu que je rentre chez moi ? J'ai pété ma voiture lol me faudra au moins 2 mois."
    # Objet qui permet de contrôler le nombre de frame et le temps
    clock = pygame.time.Clock()

    Menu = Event()
    Menu.stateEvent = True
    Fading = Event()
    Game = Event()
    Scrolling = Event()
    Scrolling.stateEvent = True
    ScrollingX = Event()
    ScrollingY = Event()
    ScrollingX.stateEvent = True
    ScrollingY.stateEvent = True

    save = {}
    save["paramètres"] = option
    save["joueur"] = Pops
    nb_dialogue = 0

    # définiton d'une fonction pour le menu principal au lancement du jeu
    def game_intro():
        # def pour vérifier le temps écoulé entre deux évents
        def time(old_time, time_wanted):
            # on actualise le temps
            time = pygame.time.get_ticks()
            # puis on calcule la durée
            time = time - old_time

            # si elle correspond à la durée voulue
            if time == time_wanted:
                # la vérification est vraie
                return True
            # sinon non
            else:
                return False

        intro = True
        first_time = pygame.time.get_ticks()
        while intro:
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    intro = False
                    pygame.quit()
            istime = time(first_time, 3000)
            istime1 = time(first_time, 6000)
            if istime:
                fadetoblack(3, screen, [], (font.render("Un jeu par Hidéo Kojima", False, white), 400, 400))

    def menu(font):
        key = pygame.key.get_pressed()
        screen.fill(black)
        # remplir le fond de la couleur
        hitbox_lancerjeu = pygame.Rect(800, 400, 200, 50)
        mousepos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        if hitbox_lancerjeu.collidepoint(mousepos[0], mousepos[1]) or key[pygame.K_UP]:
            screen.blit(font.render("Lancer jeu", False, red), (800, 400))
            if click:
                Fading.stateEvent = True
                Menu.stateEvent = False

        else:
            screen.blit(font.render("Lancer jeu", False, white), (800, 400))

        pygame.display.update()

        # def d'une fonction qui permet de faire un fondu en noir

    def fadetoblack(speed, screen, ancient, new, event, bisevent):
        nonlocal fade, bisfade
        pygame.event.set_blocked(pygame.KEYDOWN)
        if fade.get_alpha() < 255:
            for elt in ancient:
                if isinstance(elt, (Scene, Object)):
                    elt.draw(screen)
                elif isinstance(elt, Chara):
                    elt.standing(screen)
                else:
                    screen.blit(elt[0], (elt[1], elt[2]))
            screen.blit(fade, (0, 0))

            # si la valeur alpha du noir est en dessous de 255

            fade.set_alpha(fade.get_alpha() + speed)

            # on  active le processus inverse
        # si processus inverse activé
        elif bisfade.get_alpha() > 0 and fade.get_alpha() == 255:
            # on baisse alpha
            for elt in new:
                if isinstance(elt, (Scene, Object)):
                    elt.draw(screen)
                elif isinstance(elt, Chara):
                    elt.standing(screen)
                else:
                    screen.blit(elt[0], (elt[1], elt[2]))
            screen.blit(bisfade, (0, 0))

            bisfade.set_alpha(bisfade.get_alpha() - speed)
            # si alpha est égale à 0
            if bisfade.get_alpha() <= 0:
                # on désactive le processus
                event.stateEvent = False
                bisevent.stateEvent = True
                fade.set_alpha(0)
                bisfade.set_alpha(255)
        pygame.display.update()
        return event, bisevent

    # définition de la fonction du jeu principal
    def controles(level, chara):
        global velX, velY
        pygame.event.set_allowed(pygame.KEYDOWN)
        # On associe keys pour gérer les touches plus efficacement
        key = pygame.key.get_pressed()

        # Commandes
        # Si les commandes sont activées
        if chara.commande_get():
            if key[pygame.K_UP] and key[pygame.K_RIGHT]:
                chara.VelX = chara.speed
                chara.VelY = -chara.speed
            elif key[pygame.K_RIGHT] and key[pygame.K_DOWN]:
                chara.VelX = chara.speed
                chara.VelY = chara.speed
            # Gauche
            if key[pygame.K_LEFT] and chara.x - chara.width / 2 > level.PosX:
                chara.x -= chara.speed
                chara.VelX = -chara.speed
                chara.set_left()  # permet de figer le perso dans la dernière pose qu'il faisait
                # Si jamais d'autres touches sont pressées
                # Bas
                if key[pygame.K_DOWN] and chara.y + chara.height < level.PosY + level.height:
                    chara.y += chara.speed
                    chara.VelY = chara.speed
                    chara.set_front()
                    chara.VelY = chara.speed
                # Haut
                elif key[pygame.K_UP] and chara.y > level.PosY:
                    chara.y -= chara.speed
                    chara.set_back()
                    chara.VelY = -chara.speed
                chara.walk = True
            # Droite
            elif key[pygame.K_RIGHT] and chara.x < level.initialPosX + level.width - (chara.width + chara.width / 2):
                chara.x += chara.speed
                chara.VelX = chara.speed
                chara.set_right()  # Aussi
                if key[pygame.K_DOWN] and chara.y + chara.height < level.PosY + level.height:
                    chara.y += chara.speed
                    chara.velY = chara.speed
                    chara.set_front()

                # Haut
                elif key[pygame.K_UP] and chara.y > level.PosY:
                    chara.y -= chara.speed
                    chara.velY = -chara.speed
                    chara.set_back()
                chara.walk = True
            # Bas
            elif key[pygame.K_DOWN] and chara.y + chara.height < level.PosY + level.height:
                chara.y += chara.speed
                chara.VelY = chara.speed
                chara.set_front()
                chara.walk = True
            # Haut
            elif key[pygame.K_UP] and chara.y > level.PosY:
                chara.y -= chara.speed
                chara.VelY = -chara.speed
                chara.set_back()
                chara.walk = True
            else:
                chara.walk = False

            if not key[pygame.K_RIGHT] and not key[pygame.K_LEFT]:
                chara.VelX = 0
            if not key[pygame.K_DOWN] and not key[pygame.K_UP]:
                chara.VelY = 0
            # Scrolling horizontal
            if chara.x < startScrollingX:
                chara.cameraX = chara.x
                level.PosX = level.initialPosX

            elif chara.x > level.lengthX - startScrollingX:
                chara.cameraX = chara.x - level.lengthX + option.w

            elif chara.x >= startScrollingX:
                chara.cameraX = startScrollingX
                if Scrolling.stateEvent:
                    if ScrollingX.stateEvent:
                        if key[pygame.K_LEFT]:
                            velX = -chara.speed
                        elif key[pygame.K_RIGHT]:
                            velX = chara.speed
                        else:
                            velX = 0
                        level.PosX -= velX

            if chara.y > startScrollingY:
                chara.cameraY = chara.y
                level.PosY = level.initialPosY
            elif level.initialPosY < chara.y < level.initialPosY + startScrollingY:
                chara.cameraY = chara.y - level.initialPosY
            else:
                chara.cameraY = startScrollingY
                if Scrolling.stateEvent:
                    if ScrollingY.stateEvent:
                        if key[pygame.K_UP]:
                            velY = -chara.speed
                        elif key[pygame.K_DOWN]:
                            velY = chara.speed
                        else:
                            velY = 0
                        level.PosY -= velY
        else:
            chara.walk = False
            Scrolling.stateEvent = False
        while chara.x % chara.speed != 0:
            chara.x -= 1
        while chara.y % chara.speed != 0:
            chara.y -= 1

    # fonction qui permet d'afficher la carte
    def printlevel(screen, level, characters):
        level.draw(screen)

        for chara in characters:
            chara.collision(level.furnitures, Scrolling, ScrollingX, ScrollingY)

        for elt in level.furnitures:
            for chara in characters:
                if elt.rect.center[1] <= chara.downrect.top:
                    elt.draw(screen)

        for chara in characters:
            if chara.walk:
                chara.walking(screen)
            else:
                chara.standing(screen)

        for elt in level.furnitures:
            for chara in characters:
                if elt.rect.center[1] >= chara.uprect.bottom:
                    elt.draw(screen)

    # boucle principale
    while running:

        # Je bloque tous les évenements avec la souris car ils m'ont bien fait chier
        clock.tick_busy_loop(60)  # contrôle le nombre de frame du jeu
        characters = pygame.sprite.Group(Pops)
        # event handling, gets all event from the event queue
        pygame.event.pump()
        for event in pygame.event.get():

            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            # Si une touche est pressée ...
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F4:
                    screen = option.dimension(screen)
                for sprite in characters:
                    # Si c'est pendant un dialogue :
                    if sprite.dialogue_get() or Fading.stateEvent:
                        # On bloque les commandes
                        sprite.set_commande(False)
                    else:
                        Scrolling.stateEvent = True

                    if sprite.detection and event.unicode == "z":
                        sprite.set_dialogue(True)
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key not in (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT) and (
                            sprite.animation_get() or Pops.finir):
                        sprite.SInput = True
                    else:
                        sprite.SInput = False

        if Menu.stateEvent:
            menu(font)

        elif Fading.stateEvent:
            charger = [Bar, *Bar.furnitures, Pops]
            fadetoblack(5, screen, [(font.render("Lancer jeu", False, red), 800, 400)], charger, Fading, Game)
        elif Game.stateEvent:
            controles(Bar, Pops)
            # puis on affiche le sprite
            if not Pops.dialogue_get():
                screen.fill(black)
            printlevel(screen, Bar, [Pops])

            # si on actives les dialogues
            if Pops.dialogue_get():
                if Pops.informationDetection in (Table1, Table3, Table2):
                    if nb_dialogue == 0:
                        nb_dialogue = animation_text("Une simple banquette rouge avec une table.", screen, Pops,
                                                     dialogue_box, curseur, Bar, nb_dialogue, 4, None)
                    if nb_dialogue == 1:
                        nb_dialogue = animation_text("... Hein ? Pourquoi des tasses sont servies s'il y a personne ?"
                                                     + " \n "
                                                     + "En plus elles sont vides ...", screen, Pops, dialogue_box,
                                                     curseur, Bar, nb_dialogue, 4, None)
                    if nb_dialogue == 2:
                        nb_dialogue = animation_text("Que c'est stupide.", screen, Pops, dialogue_box,curseur, Bar, nb_dialogue, 4,
                                                     None)
                    if nb_dialogue == 3:
                        nb_dialogue = animation_text("...", screen, Pops, dialogue_box,curseur, Bar, nb_dialogue, 4,
                                                     "dubitatif")

            else:
                nb_dialogue = 0

        # puis on met à jour l'écran
        pygame.display.update()

    pygame.quit()


# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__ == "__main__":
    # call the main function
    main()
