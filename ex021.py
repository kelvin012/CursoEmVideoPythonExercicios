import pygame

# mixer PyGame
pygame.mixer.init()
# Pygame
pygame.init()

pygame.mixer.music.load('Yng Hstlr - Hope You Die.mp3')
pygame.mixer.music.play(loops=0, start=0.0)
while(pygame.mixer.music.get_busy()): pass