import pygame
from pygame import mixer_music
pygame.init()
pygame.mixer.music.load('vintage.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
