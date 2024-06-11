import threading
import pygame

hilo_activo = True

def usuario():
    global hilo_activo  # Declara hilo_activo como global
    entrada = input()
    if entrada == 'True':  # Compara con el string 'True', no el booleano True
        hilo_activo = False

def programador():
    while True:
        pygame.time.wait(4000)
        print(0)
        if not hilo_activo:
            break

threading.Thread(target = usuario).start()
threading.Thread(target = programador).start()


