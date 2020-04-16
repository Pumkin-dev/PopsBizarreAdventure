# -*- coding: utf-8 -*-

# enlève le message welcome from pygame
import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"

# règle le problème de l'icône dans la barre des tâches
import ctypes
myappid = 'mycompany.myproduct.subproduct.version'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

import pygame
from ressource import Chara,Event,Option,Scene,Object
from animation import animation_text

# définition d'une fonction qui lance le menu principal au lancement du jeu 
def main():
    option = Option() 
    
    width   = option.w  # caractéristiques de la fenêtre
    height  = option.h
    black = pygame.Color(0,0,0) # crée un objet couleur  en ayant référence RGB du noir
    fade  = pygame.Surface((width,height)) 
    fade.fill((0,0,0))
    bisfade = pygame.Surface((width,height))
    bisfade.fill((0,0,0))
    fade.set_alpha(0)
    bisfade.set_alpha(255)
    white = pygame.Color(255,255,255) # crée un objet couleur  en ayant référence RGB du blanc
    red   = pygame.Color(255,0,0) # de même
    blue  = pygame.Color(0,0,255)
    green = pygame.Color(0,255,0)
    
    loading = pygame.image.load # pour que ce soit plus rapide pour charger des images  
    icon = loading("images/logo.png")
    # le titre en fenêtre de jeu
    pygame.display.set_caption("Pops' Bizarre Adventure")
    pygame.display.set_icon(icon)
    screen  = pygame.display.set_mode((width,height),pygame.RESIZABLE) # pour ouvrir une fenêtre aux dimensions height width
    
    
  
    
   
    frontpops   = []
    backpops    = [] 
    rightpops   = []
    leftpops    = []
    Wfrontpops  = []
    Wrightpops  = []
    Wleftpops   = []
    Rfrontpops   = []
    Rbackpops    = [] 
    Rrightpops   = []
    Rleftpops    = []
    RWfrontpops   = [] 
    RWrightpops   = []
    RWleftpops    = []
    bouncepops =[]
    for i in range(6):
       
        frontpops.append(loading("images/sprite_standing/front/normal/front{}.png".format(i+1)).convert_alpha())
        
        backpops.append(loading("images/sprite_standing/back/back{}.png".format(i+1)).convert_alpha())
        
        rightpops.append(loading("images/sprite_standing/right/normal/right{}.png".format(i+1)).convert_alpha())
        
        leftpops.append(loading("images/sprite_standing/left/normal/left{}.png".format(i+1)).convert_alpha())
        
        Wfrontpops.append(loading("images/sprite_standing/front/wink/front{}.png".format(i+1)).convert_alpha())
    
        Wrightpops.append(loading("images/sprite_standing/right/wink/right{}.png".format(i+1)).convert_alpha())
        
        Wleftpops.append(loading("images/sprite_standing/left/wink/left{}.png".format(i+1)).convert_alpha())
        
        Rfrontpops.append(loading("images/sprite_walking/front/normal/front{}.png".format(i+1)).convert_alpha())
              
        Rbackpops.append(loading("images/sprite_walking/back/back{}.png".format(i+1)).convert_alpha())
        
        Rrightpops.append(loading("images/sprite_walking/right/normal/right{}.png".format(i+1)).convert_alpha())     
    
        Rleftpops.append(loading("images/sprite_walking/left/normal/left{}.png".format(i+1)).convert_alpha())      
        
        RWfrontpops.append(loading("images/sprite_walking/front/wink/front{}.png".format(i+1)).convert_alpha())
        
        RWrightpops.append(loading("images/sprite_walking/right/wink/right{}.png".format(i+1)).convert_alpha())     
    
        RWleftpops.append(loading("images/sprite_walking/left/wink/left{}.png".format(i+1)).convert_alpha())      
    
    for i in range(4):
        
        bouncepops.append(loading("images/dialogue/face_discussion/bounce/bounce{}.png ".format(i+1)).convert_alpha())
    
    maps = loading("images/map.png").convert_alpha()
    dialogue_box = loading("images/dialogue/dialogue_box.png").convert()
    move = loading("images/move.png")

    curseur = [loading("images/dialogue/curseur/Sprite-0001.png").convert_alpha(),loading("images/dialogue/curseur/Sprite-0002.png").convert_alpha()]
    
    initialPosX = 600
    initialPosY = 400
    
    widthPops, heightPops  = backpops[0].get_rect().size
    velPops     = 5
    
    Pops        = Chara(initialPosX,initialPosY,widthPops,heightPops,velPops,frontpops,
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
    bouncepops) # toutes les caractéristiques de Pops
    
    startScrollingX = option.mw
    startScrollingY = option.mh
    initialSPosX = 500
    initialSPosY = -300
    
    Bar          = Scene(maps,initialSPosX,initialSPosY)
    stageLengthX = Bar.width + 2*initialSPosX
    stageLengthY = Bar.height + abs(initialSPosY)* 2
    # initialize the pygame module
    pygame.init()
    # On initialise le son (si jamais)
    pygame.mixer.init()
    stageWidth, stageHeight = maps.get_rect().size
    startScrollingX = option.mw
    startScrollingY = option.mh
    
    stageLengthX = stageWidth + 2*initialSPosX
    stageLengthY = stageHeight + abs(initialSPosY)* 2
    
    #active le module de texte
    pygame.font.init()
    
    #La police d'écriture du jeu
    font = pygame.font.Font("VCR_OSD_MONO_1.001.ttf",30)   
    
    # define a variable to control the main loop
    running = True
    
    # Textes pour tester les boites de dialogues
    text        = "Mais comment veux-tu que je rentre chez moi ?"
    
    #Objet qui permet de contrôler le nombre de frame et le temps
    clock = pygame.time.Clock()
    
    Menu            = Event()
    Menu.stateEvent = True
    Fading          = Event()
    Game            = Event() 
    
    Bar = Scene(maps,initialSPosX,initialSPosY)
    
    save = {}
    save["paramètres"] = option
    save["joueur"] = Pops
    finir = False
        
    # définiton d'une fonction pour le menu principal au lancement du jeu
    def menu(font):  
        key = pygame.key.get_pressed()
        screen.fill(black)
        #remplir le fond de la couleur
        hitbox_lancerjeu = pygame.Rect(800,400,200,50)
        mousepos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        if hitbox_lancerjeu.collidepoint(mousepos[0],mousepos[1]) or key[pygame.K_UP]: 
            screen.blit(font.render("Lancer jeu",False,red),(800,400))
            if click:
                Fading.stateEvent = True
                Menu.stateEvent   = False
                
        else:
            screen.blit(font.render("Lancer jeu",False,white),(800,400))
            

        pygame.display.update()    
   
    # def d'une fonction qui permet de faire un fondu en noir
  
    def fadetoblack(speed,screen,ancient,new,event,bisevent):
        nonlocal fade, bisfade
        pygame.event.set_blocked(pygame.KEYDOWN)
        if fade.get_alpha() < 255:
            for elt in ancient:
                if isinstance(elt,(Scene,Object)):
                    elt.draw(screen)
                elif isinstance(elt,Chara):
                    elt.standing(screen)
                else:
                    screen.blit(elt[0],(elt[1],elt[2]))
            screen.blit(fade,(0,0))
            
            # si la valeur alpha du noir est en dessous de 255
            
            fade.set_alpha(fade.get_alpha() + speed)
                    
                    # on  active le processus inverse
        # si processus inverse activé
        elif bisfade.get_alpha() > 0 and fade.get_alpha() == 255:
            #on baisse alpha
            for elt in new:
                if isinstance(elt,(Scene,Object)):
                    elt.draw(screen)
                elif isinstance(elt,Chara):
                    elt.standing(screen)
                else:
                    screen.blit(elt[0],(elt[1],elt[2]))
            screen.blit(bisfade,(0,0))
            
            bisfade.set_alpha(bisfade.get_alpha() - speed)
            # si alpha est égale à 0
            if bisfade.get_alpha() <= 0:
                # on désactive le processus
                event.stateEvent = False
                bisevent.stateEvent = True
                fade.set_alpha(0)
                bisfade.set_alpha(255)
        pygame.display.update()
    # définition de la fonction du jeu principal
    def controles(level):
        global velX, velY
        pygame.event.set_allowed(pygame.KEYDOWN)
         # On associe keys pour gérer les touches plus efficacement
        key = pygame.key.get_pressed()
        #Commandes
        #Si les commandes sont activées
        if Pops.commande_get():
            #Gauche    
            if key[pygame.K_LEFT] and Pops.x - Pops.width/2 > level.PosX:
                Pops.x -= Pops.speed
                Pops.set_left()  # permet de figer le perso dans la dernière pose qu'il faisait
                # Si jamais d'autres touches sont pressées
                 #Bas
                if key[pygame.K_DOWN] and Pops.y + Pops.height < level.PosY + level.height:
                    Pops.y += Pops.speed
                    Pops.set_front()
            
                #Haut
                elif key[pygame.K_UP] and Pops.y > level.PosY:
                    Pops.y -= Pops.speed
                    Pops.set_back()
                Pops.walk = True
            #Droite    
            elif key[pygame.K_RIGHT] and Pops.x < stageLengthX - initialSPosX - (Pops.width + Pops.width/2):
                Pops.x += Pops.speed
                Pops.set_right()  # Aussi
                if key[pygame.K_DOWN] and Pops.y + Pops.height < level.PosY + level.height:
                    Pops.y += Pops.speed
                    Pops.set_front()
              
                #Haut
                elif key[pygame.K_UP] and Pops.y > level.PosY:
                    Pops.y -= Pops.speed
                    Pops.set_back()
                Pops.walk = True
            #Bas
            elif key[pygame.K_DOWN] and Pops.y + Pops.height < level.PosY + level.height:
                Pops.y += Pops.speed
                Pops.set_front()
                Pops.walk = True
            #Haut
            elif key[pygame.K_UP] and Pops.y > level.PosY:
                Pops.y -= Pops.speed
                Pops.set_back()
                Pops.walk = True
            else:
                Pops.walk = False
            #Scrolling horizontal
            if Pops.x < startScrollingX:
                Pops.cameraX = Pops.x
            
            elif Pops.x > stageLengthX - startScrollingX:
                Pops.cameraX = Pops.x - stageLengthX + option.w
            elif Pops.x >= startScrollingX:
                Pops.cameraX = startScrollingX
                if key[pygame.K_LEFT]:
                    velX = -Pops.speed
                elif key[pygame.K_RIGHT]:
                    velX = Pops.speed
                else:
                    velX = 0
                level.PosX -= velX
            
            if Pops.y > startScrollingY:
                Pops.cameraY = Pops.y
            elif initialSPosY < Pops.y < initialSPosY + startScrollingY:
                Pops.cameraY = Pops.y - initialSPosY 
            else:
                Pops.cameraY = startScrollingY 
                if key[pygame.K_UP]:
                    velY = -Pops.speed
                elif key[pygame.K_DOWN]:
                    velY = Pops.speed
                else:
                    velY = 0
                level.PosY -= velY     
        else:
            Pops.walk = False
        # puis on affiche le sprite
    
    # boucle principale
    while running:
        
        # Je bloque tous les évenements avec la souris car ils m'ont bien fait chier
        clock.tick_busy_loop(60) # contrôle le nombre de frame du jeu
        
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
                # Si c'est pendant un dialogue :
                if Pops.dialogue_get() or Fading.stateEvent:
                    # On bloque les commandes
                    Pops.set_commande(False) 
                if event.key == pygame.K_SPACE:
                #on active les dialogues45
                    Pops.set_dialogue(True)
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key not in (pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT) and (Pops.animation_get() or Pops.finir):
                    Pops.SInput = True
                else:
                    Pops.SInput = False
        
        if Menu.stateEvent:
            menu(font)
         
        elif Fading.stateEvent:
            charger = [Bar,Pops]
            fadetoblack(5,screen,[(font.render("Lancer jeu",False,red),800,400)],charger,Fading,Game)
        elif Game.stateEvent:
            controles(Bar)
              # puis on affiche le sprite
            screen.fill(black)
            Bar.draw(screen)
            if Pops.walk:
                Pops.walking(screen)

            else:
                Pops.standing(screen)

            
            # si on actives les dialogues
            if Pops.dialogue_get():
                # on active l'animation du texte avec pour paramètre le texte que l'on veut
                animation_text(text,screen,Pops,dialogue_box,curseur,Bar)
                #puis on met à jour l'écran
            pygame.display.update()
        
    pygame.quit()            
 
   
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
    # call the main function
    main()
