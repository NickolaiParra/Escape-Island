from Módulos import Escape_Island as EI
import pygame
import sys

pygame.init()

mapa_avion_ajustado =  pygame.transform.scale(EI.mapa_avion, (EI.ancho, EI.alto)) #Ajustamos el mapa al tamaño de la pantalla
EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Mostramos el mapa
while True:
    for evento in pygame.event.get():
        if evento.type ==  pygame.QUIT:
            pygame.quit()
            sys.exit()
        if evento.type == pygame.KEYDOWN:
            #Si se presiona la tecla "Esc", entonces se sale de la pantalla completa
            if evento.key == pygame.K_ESCAPE:
                EI.PANTALLA = pygame.display.set_mode((500, 400))
                portada_ajustada = pygame.transform.scale(EI.portada, (500, 400))
                EI.PANTALLA.blit(portada_ajustada, (0, 0)) #Mostramos portada
    pygame.display.update()