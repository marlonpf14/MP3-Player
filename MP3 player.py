import pygame
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021.flac')
pygame.mixer.music.play()
pygame.event.wait()
