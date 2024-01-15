#codigo q faz tocar uma musica
import pygame

pygame.init()
pygame.mixer.music.load('musica_ex23/ex023.mp3')
pygame.mixer.music.play()

# Espera até que a música termine de tocar
while pygame.mixer.music.get_busy():
    pass
