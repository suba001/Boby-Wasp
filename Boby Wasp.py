import pygame
import sys
import random
import time
from pygame.locals import *

pygame.init()

FPS = 60
FPSCLOCK = pygame.time.Clock()
moove = 0

font=pygame.font.Font(None, 50)
pillar_image = pygame.image.load('C:\Jeu personnages\pilier.off.png')
pillar_image_upside_down = pygame.image.load('C:\Jeu personnages\pilier.off.upside_down.png')
bg = pygame.image.load('C:\Jeu personnages\OIP (42).png')
bird_image = pygame.image.load('C:\Jeu personnages\OIP (44).png')
bee_image = pygame.image.load('C:\Jeu personnages\OIP (45).png')

window = pygame.display.set_mode((1400,670))

class pillar () :
    def __init__ (self) :
        self.image = pillar_image
        self.image_upside_down = pillar_image_upside_down
        self.x = 0
        self.y = 0
        self.velocity = 10

    def display(self) :
        window.blit(self.image,(self.x, self.y))

    def moove(self) :
        self.x -= self.velocity

class Bee () :
    def __init__ (self) :
        self.image = bee_image
        self.x = 300
        self.y = 300
        self.velocity = 10

    def display(self) :
        window.blit(self.image,(self.x, self.y))

    def moove_fall(self) :
        self.y += self.velocity

    def moove_up(self) :
        self.y -= self.velocity

player = Bee()

pillar1ground = pillar()
pillar2ground = pillar()

pillar1ground.image = pillar1ground.image
pillar2ground.image = pillar2ground.image

pillar1ground.x = 2625
pillar1ground.y = random.randint(425,600)

pillar2ground.x = 3375
pillar2ground.y = random.randint(425,600)

############

pillar1up = pillar()
pillar2up = pillar()

pillar1up.image = pillar1up.image_upside_down
pillar2up.image = pillar2up.image_upside_down

pillar1up.x = 2400
pillar1up.y = random.randint(-125, 0)

pillar1up.x = 3050
pillar1up.y = random.randint(-125, 0)

pygame.key.set_repeat(1,20)
start_ticks=pygame.time.get_ticks()

while True :
    seconds=(pygame.time.get_ticks()-start_ticks)/1000
    if seconds >= 30 :
        pillar1ground.velocity = 12
        pillar2ground.velocity = 12
        pillar1up.velocity = 12
        pillar2up.velocity = 12

    if seconds >= 50 :
        pillar1ground.velocity = 15
        pillar2ground.velocity = 15
        pillar1up.velocity = 15
        pillar2up.velocity = 15

    if seconds >= 100 :
        pillar1ground.velocity = 18
        pillar2ground.velocity = 18
        pillar1up.velocity = 18
        pillar2up.velocity = 18
        
    secondes = str(seconds)
    texte2 = font.render(secondes,1,(255,255,0))
    
    moove = 0
    pillar1ground_rect = pillar_image.get_rect(topleft = (pillar1ground.x,pillar1ground.y-70))
    pillar2ground_rect = pillar_image.get_rect(topleft = (pillar2ground.x,pillar2ground.y-70))

    pillar1up_rect = pillar_image_upside_down.get_rect(topleft = (pillar1up.x,pillar1up.y))
    pillar2up_rect = pillar_image_upside_down.get_rect(topleft = (pillar2ground.x,pillar2up.y))
    
    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN :
            moove = 1
            if (event.key == K_SPACE or event.key == K_UP) and player.y > 0 and not pillar1up_rect.collidepoint(player.x, player.y) and not pillar2up_rect.collidepoint(player.x, player.y) :
                player.velocity = 14
                player.moove_up()

            if event.key == K_DOWN and player.y < 590 and not pillar1ground_rect.collidepoint(player.x, player.y-20) and not pillar2ground_rect.collidepoint(player.x, player.y-20) :
                player.velocity = 14
                player.moove_fall()

            if event.key == K_ESCAPE :
                pygame.quit()
                sys.exit()

    if moove == 0 and player.y < 590 and not pillar1ground_rect.collidepoint(player.x, player.y-20) and not pillar2ground_rect.collidepoint(player.x, player.y-20) :
        player.velocity = 7
        player.moove_fall()
            
    if pillar1ground.x <= -150 and pillar2ground.x <= 1950 :
        pillar1ground.x = 1625
        pillar1ground.y = random.randint(300,500)
        
    if pillar2ground.x <= -150 and pillar2ground.x <= 1300 :
        pillar2ground.x = pillar1ground.x+750 #2275
        pillar2ground.y = random.randint(300,500)

    if pillar1up.x <= -150 : 
        pillar1up.x = pillar1ground.x-425 #1300
        pillar1up.y = random.randint(-175,-100)
      
    if pillar2up.x <= -150 and pillar1up.x <= 1625 :
        pillar2up.x = pillar1ground.x+425 #1950
        pillar2up.y = random.randint(-175,-100)
        
    window.blit(bg,(0,0))
    pillar1ground.moove()
    pillar2ground.moove()
    pillar1up.moove()
    pillar2up.moove()
    
    pillar1ground.display()
    pillar2ground.display()
    pillar1up.display()
    pillar2up.display()
    player.display()
    window.blit(texte2,(0,0))
    pygame.display.flip()
    FPSCLOCK.tick(FPS)
