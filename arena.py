import pygame
from pygame.locals import *
from sys import exit

from Actions.gameActions import ShowStatus, ColdownPassing
from debug import endgame

from VisualGame import width, height, create_character
from Actions.chooseActions import ChoiceAction

pygame.init()

screen = pygame.display.set_mode((width, height), pygame.DOUBLEBUF, pygame.HWSURFACE)
background = pygame.image.load("./Recursos/Images/background.png")
clock = pygame.time.Clock()

# pygame.mixer.music.set_volume(0.1) #valor entre 0 e 1
# music = pygame.music.load('name_of_music.extension')
# pygame.mixer.music.play(-1) # -1 roda eternamente

# sound = pygame.mixer.Sound('name_of_file.wav') #sempre wav
# sound.set_volume(0)
# sound.play() # roda

player = create_character()
enemy = create_character(flip = True)

all_sprites = pygame.sprite.Group()
all_sprites.add(player.Spr,enemy.Spr)

cont = True

while cont:
    while True:
        clock.tick(30)
        screen.fill((0,0,0))
        #background image
        screen.blit(background, (0,0))

        all_sprites.draw(screen)

        for event in pygame.event.get():
            if (event.type == QUIT):
                pygame.quit()
                exit()
            
            

            if (event.type == KEYDOWN):
                ChoiceAction(player.Char, enemy.Char, chr(event.key).upper())
                ColdownPassing(player.Char, enemy.Char)
                ShowStatus(enemy.Char)
        all_sprites.update()
        pygame.display.update()
