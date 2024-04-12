
#Importamos las librerías necesarias
import pygame
import sys
import threading


from Módulos import Escape_Island as EI

#Inicializamos pygame
pygame.init()

#Inicializamos el módulo de sonido de pygame
pygame.mixer.init()

#Cargamos la música

pygame.mixer.music.load('Música\ST.mp3')

#Reproducimos la música en bucle 
pygame.mixer.music.play(-1)

pantalla_de_carga_ajustada =  pygame.transform.scale(EI.pantalla_de_carga, (EI.ancho, EI.alto)) #Ajustamos portada al tamaño de la pantalla


#Pantalla de carga
posicionx_barra = EI.ancho * 0.1
posiciony_barra = EI.alto * 0.92
ancho_barra_maximo = EI.ancho * 0.8
alto_barra = 0.05 * EI.alto
progreso_carga = 0
portada_ajustada =  pygame.transform.scale(EI.portada, (EI.ancho*0.8, EI.alto)) #Ajustamos portada al tamaño de la pantalla
fuente = pygame.font.Font("Fuentes\Fortune.otf", int(EI.ancho * 0.04)) #Fuente del texto de la pantalla de carga
EI.PANTALLA.fill(EI.FONDO) #Rellenamos el fondo
EI.PANTALLA.blit(portada_ajustada, (EI.ancho*0.1, 0)) #Mostramos portada
texto = fuente.render("Cargando", True, (EI.ROJO)) 
tiempo_espera = 1000
EI.PANTALLA.blit(texto, (int((EI.ancho//2)- 4 * (EI.ancho * 0.02)), EI.alto * 0.81) ) #Mostramos "Cargando" en la pantalla de carga
hilo_activo = True


def animar_puntos():
        """Esta función imprime en pantalla los puntos suspensivos de la palabra cargando, con un tiempo de espera entre cada punto de 1 segundo """
        global hilo_activo 
        for i in range(1, 7):
                pygame.time.wait(tiempo_espera)
                texto1 = fuente.render("." * i, True, (EI.ROJO))
                EI.PANTALLA.blit(texto1, (EI.ancho * 0.59, EI.alto * 0.81))
                pygame.display.update()
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        hilo_activo = False
                if not hilo_activo:
                     break
                
threading.Thread(target=animar_puntos).start() #Ejecutamos la función animar_puntos al mismo tiempo que el bucle principal del juego (esto se hace para evitar que tiempo_espera afecte a la barra de carga)

#Pantalla de inicio
fuente_2 = pygame.font.Font("Fuentes\\Nicolast.otf", int(EI.ancho * 0.03)) #Fuente del texto de la pantalla de inicio
texto_2 = fuente_2.render('Presiona "Enter" para iniciar', True, (EI.ROJO)) 
portada2_ajustada =  pygame.transform.scale(EI.portada_2, (EI.ancho, EI.alto)) #Ajustamos portada 2 al tamaño de la pantalla

#Bucle principal del juego
romper_carga = True
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
                #Si se presiona enter, se abre la pantalla de inicio
                if (evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER) and progreso_carga >= 1:
                    EI.transicion_desvanecimiento(portada2_ajustada, pantalla_de_carga_ajustada, 2000)  #Transición de desvanecimiento de 2 segundos entre la pantalla de carga y de inicio
                    romper_carga = False
                    break
        if romper_carga == False:
            break

        progreso_carga += 0.0002
        progreso_carga = min(1.0, max(0.0, progreso_carga)) #Limitamos el progreso de la barra de carga entre cero y uno
        ancho_barra_actual = int(ancho_barra_maximo*progreso_carga) #Actualizamos el ancho de la barra de carga
        pygame.draw.rect(EI.PANTALLA, EI.NEGRO, (posicionx_barra, posiciony_barra, ancho_barra_maximo, alto_barra) ) #Dibujamos el fondo de la barra de carga
        pygame.draw.rect(EI.PANTALLA, EI.H14AD8F, (posicionx_barra, posiciony_barra, ancho_barra_actual, alto_barra)) #Dibujamos la barra de carga actual
        if progreso_carga >= 1: #Limitamos el tiempo que aparece "Cargando" y los puntos suspensivos
                EI.PANTALLA.fill(EI.FONDO, ((int((EI.ancho//2)- 4 * (EI.ancho * 0.02)), EI.alto * 0.82, texto.get_width() *1.5, (texto.get_height()) * 0.8)))
                EI.PANTALLA.blit(texto_2, (int((EI.ancho//2)- 4 * (EI.ancho * 0.02))-EI.ancho*0.17, EI.alto * 0.85) ) #Mostramos 'Presiona "Enter" para iniciar' en la pantalla de inicio
                hilo_activo = False
        pygame.display.update()


EI.PANTALLA.blit(portada2_ajustada, (0, 0)) #Mostramos portada 2
pygame.draw.rect(EI.PANTALLA, EI.FONDO, (0, 0, EI.ancho * 0.2, EI. alto))

#Botones
boton_nueva_partida = EI.Boton(EI.ancho * 0.025, EI.alto * 0.15, EI.ancho * 0.15, EI.alto * 0.1, "Nueva partida", 45)
boton_cargar_partida = EI.Boton(EI.ancho * 0.025, EI.alto * 0.35, EI.ancho * 0.15, EI.alto * 0.1, "Cargar partida", 45)
boton_creditos = EI.Boton(EI.ancho * 0.025, EI.alto * 0.55, EI.ancho * 0.15, EI.alto * 0.1, "Créditos", 45)
boton_configuracion = EI.Boton(EI.ancho * 0.025, EI.alto * 0.75, EI.ancho * 0.15, EI.alto * 0.1, "Configuración", 45)

#Mostramos inicialmente los botones
boton_nueva_partida.dibujar(EI.PANTALLA)
boton_cargar_partida.dibujar(EI.PANTALLA)
boton_creditos.dibujar(EI.PANTALLA)
boton_configuracion.dibujar(EI.PANTALLA)

cerrar = True

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
                    EI.PANTALLA.blit(portada_ajustada, (0, 0))
                    cerrar = False
            if evento.type == pygame.MOUSEMOTION:
                #Si el cursor del mouse pasa por encima de algún  botón, entonces su color cambia
                boton_nueva_partida.color_normal = EI.AZUL if not boton_nueva_partida.esta_encima(evento.pos) else EI.ROJO
                boton_cargar_partida.color_normal = EI.AZUL if not boton_cargar_partida.esta_encima(evento.pos) else EI.ROJO
                boton_creditos.color_normal = EI.AZUL if not boton_creditos.esta_encima(evento.pos) else EI.ROJO
                boton_configuracion.color_normal = EI.AZUL if not boton_configuracion.esta_encima(evento.pos) else EI.ROJO
            if cerrar:
                #Mostramos los botones
                boton_nueva_partida.dibujar(EI.PANTALLA)
                boton_cargar_partida.dibujar(EI.PANTALLA)
                boton_creditos.dibujar(EI.PANTALLA)
                boton_configuracion.dibujar(EI.PANTALLA)

        pygame.display.update()
