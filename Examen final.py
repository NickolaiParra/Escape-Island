import pygame
import sys
import random
from Módulos import Escape_Island as EI

#Inicialización de Pygame
pygame.init()


fuente_codigo = pygame.font.Font("Fuentes\\FiraCode.otf", int(EI.ancho * 0.02)) 
tamaño_fuente = int(EI.ancho * 0.02)
lines = [""]
cursor_pos = [0, 0]  #Posición del cursor


num_dialog = -1
dialog_continue = True

#personajes
muerte = pygame.transform.scale(EI.muerte, (EI.ancho*0.2, EI.alto*0.3))
muerte_rect = muerte.get_rect()
muerte_rect.bottomleft = (EI.ancho*0.01, EI.alto*0.7)

#Imágenes
fondo_guerra = pygame.transform.scale(EI.fondo_guerra, (EI.ancho, EI.alto))
fondo_final = pygame.transform.scale(EI.fondo_final, (EI.ancho, EI.alto))

# Bucle principal del juego
while True:
    if num_dialog == -1:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        t1 = "Este lugar está en ruinas."
        t2 = "Pero es la única manera de escapar..."
        EI.mostrar_texto("Examen final",t1,t2,color=EI.ROJO)
    elif num_dialog == 0:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "Es increíble que hayas podido llegar hasta aquí."
        t2 = "Lamentablemente, hasta acá llegó tu aventura."
        t3 = "La única manera de salir con vida es superando el siguiente desafío."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 1:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "Esta vez, no será de opción múltiple."
        t2 = "Deberás escribir tu propio código."
        EI.mostrar_texto("Muerte",t1,t2,color=EI.MORADO)
    elif num_dialog == 2:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "Necesitas encontrar la salida para ser rescatado."
        t2 = "La isla está representada como una cuadrícula de 100 x 100."
        t3 = "Cada celda tiene coordenadas (x, y) que van desde (1, 1) hasta (100, 100)."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 3:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "La salida está ubicada en una celda aleatoria de esta cuadrícula."
        t2 = "Tu objetivo será crear la función 'escape_island'."
        t3 = "Esta función debe recibir cuatro argumentos: 'x', 'y', 'salida_x', 'salida_y'. (en ese orden)."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 4:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "La posición 'x' de la salida está representada por la variable 'salida_x'."
        t2 = "La posición 'y' de la salida está representada por la variable 'salida_y'."
        t3 = "La función debe retornar 'salida' si los valores (x, y) coinciden con los de la salida."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 5:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "En caso contrario, la función debe retornar:"
        t2 = "'x' si la distancia en 'x' entre ambos puntos es menor a la distancia en 'y'."
        t3 = "'y' si la distancia en 'y' entre ambos puntos es menor a la distancia en 'x'."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 6:
        EI.PANTALLA.blit(fondo_guerra, (0, 0))
        EI.PANTALLA.blit(muerte, muerte_rect)
        t1 = "'igual' si la distancia en 'x' e 'y' entre ambos puntos es igual."
        t2 = "Ten cuidado con el nombre de la función."
        t3 = "Si lo logras, serás libre."
        EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 8:
        EI.PANTALLA.blit(fondo_final, (0, 0))
        t1 = "¡Felicidades, has logrado escapar de la isla!"
        t2 = "Has demostrado gran ingenio en cada desafío."
        t3 = "¡Ahora eres libre!"
        EI.mostrar_texto("Escape Island",t1,t2,t3,color=EI.ROJO)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            #Si se presiona la flecha izquierda o derecha, se avanza en los diálogos
            elif event.key == pygame.K_RIGHT and dialog_continue:
                #Avanzar el diálogo
                num_dialog += 1
            elif num_dialog >= 0 and event.key == pygame.K_LEFT and dialog_continue:
                #Retroceder el diálogo
                num_dialog -= 1
            elif num_dialog == 7: 
                dialog_continue = False
                t1 = "Desafío final: Crea la función 'escape_island' (x, y, salida_x, salida_y)."
                t2 = "Debes retornar 'x', 'y', 'igual' o 'salida'."
                t3 = "Presiona 'Ctrl' para ejecutar tu código."
                EI.keydown(cursor_pos, lines, event)
                EI.mostrar_texto(t1,t2,t3,EI.t,color=EI.ROJO)
    if num_dialog == 7:  
        t1 = "Desafío final: Crea la función 'escape_island' (x, y, salida_x, salida_y)."
        t2 = "Debes retornar 'x', 'y', 'igual' o 'salida'."
        t3 = "Presiona 'Ctrl' para ejecutar tu código."
        dialog_continue = False  
        EI.render_text(cursor_pos, lines, fuente_codigo, tamaño_fuente)
        EI.mostrar_texto(t1, t2, t3,EI.t,color=EI.ROJO)
        if EI.correcto:  
            pygame.time.wait(1000)
            num_dialog += 1
    pygame.display.flip()
