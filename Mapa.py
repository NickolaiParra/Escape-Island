import pygame
import sys
import threading
import json

pygame.init()

from Módulos import Escape_Island as EI

#Inicializamos el módulo de sonido de pygame
pygame.mixer.init()

#Cargamos la música

pygame.mixer.music.load('Música/ST.mp3')

#Reproducimos la música en bucle 
#Configuración de la música
pygame.mixer.music.load('Música/ST.mp3') #Cargamos la música
pygame.mixer.music.set_volume(0.5)  #Configuramos el volumen inicial
pygame.mixer.music.play(-1) #Reproducimos la música en bucle 

pantalla_de_carga_ajustada =  pygame.transform.scale(EI.pantalla_de_carga, (EI.ancho, EI.alto)) #Ajustamos portada al tamaño de la pantalla

#Pantalla de configuración
#Textos
fuente_2 = pygame.font.Font("Fuentes/Nicolast.otf", int(EI.ancho * 0.04)) #Fuente del texto de la pantalla de inicio
texto_musica = fuente_2.render('Music', True, (EI.ROJO)) 
fuente_salida = pygame.font.Font("Fuentes/Nicolast.otf", int(EI.ancho * 0.025))
texto_brillo = fuente_2.render('Brillo', True, (EI.ROJO)) 
texto_salida = fuente_salida.render("Confirma que deseas salir", True, (EI.ROJO)) 

#Botones
boton_cancelar = EI.Boton(EI.ancho * 0.1, EI.alto * 0.8, EI.ancho * 0.2, EI.alto * 0.1, "Cancelar", int(EI.ancho * 0.05), int(EI.ancho * 0.015))
boton_aceptar = EI.Boton(EI.ancho * 0.5, EI.alto * 0.8, EI.ancho * 0.2, EI.alto * 0.1, "Aceptar", int(EI.ancho * 0.05), int(EI.ancho * 0.015))
boton_salida = EI.Boton(EI.ancho * 0.30, EI.alto * 0.5, EI.ancho * 0.2, EI.alto * 0.08, "Guardar y salir", int(EI.ancho * 0.03), int(EI.ancho * 0.01))
boton_salida2 = EI.Boton(EI.ancho * 0.55, EI.alto * 0.5, EI.ancho * 0.15, EI.alto * 0.08, "Regresar", int(EI.ancho * 0.03), int(EI.ancho * 0.01))

#Imágenes
iconosonido_ajustado = pygame.transform.scale(EI.icono_sonido, (EI.ancho * 0.07, EI.alto * 0.1)) 
iconosinsonido_ajustado = pygame.transform.scale(EI.icono_sinsonido, (EI.ancho * 0.07, EI.alto * 0.1))
iconobrillo_ajustado = pygame.transform.scale(EI.icono_brillo, (EI.ancho * 0.07, EI.alto * 0.1)) 
iconosinbrillo_ajustado = pygame.transform.scale(EI.icono_sinbrillo, (EI.ancho * 0.07, EI.alto * 0.1))
dialogo = pygame.transform.scale(EI.dialogo, (EI.ancho * 0.5, EI.alto * 0.4))

posicion_relativa = 0.5
brillo = 1
mouseantiguo_x = EI.ancho * 0.34
mouseantiguo_x_brillo = EI.ancho * 0.489
Gris = True
Gris_brillo = True


#Pantalla de carga
posicionx_barra = EI.ancho * 0.1
posiciony_barra = EI.alto * 0.92
ancho_barra_maximo = EI.ancho * 0.8
alto_barra = 0.05 * EI.alto
progreso_carga = 0
portada_ajustada =  pygame.transform.scale(EI.portada, (EI.ancho*0.8, EI.alto)) #Ajustamos portada al tamaño de la pantalla
fuente = pygame.font.Font("Fuentes/Fortune.otf", int(EI.ancho * 0.04)) #Fuente del texto de la pantalla de carga
EI.PANTALLA.fill(EI.FONDO) #Rellenamos el fondo
EI.PANTALLA.blit(portada_ajustada, (EI.ancho*0.1, 0)) #Mostramos portada
texto = fuente.render("Cargando", True, (EI.ROJO)) 
tiempo_espera = 1000
EI.PANTALLA.blit(texto, (int((EI.ancho//2)- 4 * (EI.ancho * 0.02)), EI.alto * 0.81) ) #Mostramos "Cargando" en la pantalla de carga
hilo_activo = True


def animar_puntos():
        """Esta función imprime en pantalla los puntos suspensivos de la palabra cargando, con un tiempo de espera entre cada punto de 1 segundo."""
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
fuente_2 = pygame.font.Font("Fuentes/Nicolast.otf", int(EI.ancho * 0.03)) #Fuente del texto de la pantalla de inicio
texto_2 = fuente_2.render('Presiona "Enter" para iniciar', True, (EI.ROJO)) 
portada2_ajustada =  pygame.transform.scale(EI.portada_2, (EI.ancho, EI.alto)) #Ajustamos portada 2 al tamaño de la pantalla

#Bucle principal del juego
romper_carga = True
while True:
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                #Si se presiona 'escape', se termina el programa
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
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
boton_nueva_partida = EI.Boton(EI.ancho * 0.025, EI.alto * 0.15, EI.ancho * 0.15, EI.alto * 0.1, "Nueva partida", int(EI.ancho * 0.026), int(EI.ancho * 0.015))
boton_cargar_partida = EI.Boton(EI.ancho * 0.025, EI.alto * 0.35, EI.ancho * 0.15, EI.alto * 0.1, "Cargar partida", int(EI.ancho * 0.026), int(EI.ancho * 0.015))
boton_creditos = EI.Boton(EI.ancho * 0.025, EI.alto * 0.55, EI.ancho * 0.15, EI.alto * 0.1, "Créditos", int(EI.ancho * 0.026), int(EI.ancho * 0.015))
boton_configuracion = EI.Boton(EI.ancho * 0.025, EI.alto * 0.75, EI.ancho * 0.15, EI.alto * 0.1, "Configuración", int(EI.ancho * 0.026), int(EI.ancho * 0.015))

#Mostramos inicialmente los botones
boton_nueva_partida.dibujar(EI.PANTALLA)
boton_cargar_partida.dibujar(EI.PANTALLA)
boton_creditos.dibujar(EI.PANTALLA)
boton_configuracion.dibujar(EI.PANTALLA)
ciclo = False
cerrar = True
controlar_bucle = False

#Variables para cargar la partida
nueva = False
cargar = False

while True:
        if controlar_bucle:
            break
        while ciclo:
            EI.PANTALLA.blit(portada2_ajustada, (0, 0)) #Mostramos portada 2
            pygame.draw.rect(EI.PANTALLA, EI.FONDO, (0, 0, EI.ancho * 0.2, EI. alto))
            ciclo = False
            break

        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
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
            if evento.type == pygame.MOUSEBUTTONDOWN and boton_nueva_partida.esta_encima(evento.pos):
                controlar_bucle = True
                nueva = True
                break
            if evento.type == pygame.MOUSEBUTTONDOWN and boton_cargar_partida.esta_encima(evento.pos):
                controlar_bucle = True
                cargar = True
                break
            if evento.type == pygame.MOUSEBUTTONDOWN and boton_configuracion.esta_encima(evento.pos):
                controlar_bucle_2 = False
                while True:
                    if controlar_bucle_2:
                        break
                    for evento in pygame.event.get():
                        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()
                        if evento.type == pygame.MOUSEMOTION:
                            #Si el cursor del mouse pasa por encima de algún  botón, entonces su color cambia
                            boton_aceptar.color_normal = EI.AZUL if not boton_aceptar.esta_encima(evento.pos) else EI.ROJO
                            boton_cancelar.color_normal = EI.AZUL if not boton_cancelar.esta_encima(evento.pos) else EI.ROJO
                        if evento.type == pygame.MOUSEBUTTONDOWN and boton_aceptar.esta_encima(evento.pos):
                            controlar_bucle_2 = True
                            ciclo = True
                            break
                        elif evento.type == pygame.MOUSEBUTTONDOWN and boton_cancelar.esta_encima(evento.pos):
                            #Valores iniciales
                            posicion_relativa = 0.5
                            brillo = 1
                            mouseantiguo_x = EI.ancho * 0.34
                            mouseantiguo_x_brillo = EI.ancho * 0.489
                            Gris = True
                            Gris_brillo = True
                            pygame.mixer.music.set_volume(0.5)  #Configuramos el volumen inicial
                            pygame.display.set_gamma(1) #Se aplica el brillo a la pantalla
                            controlar_bucle_2 = True
                            ciclo = True
                            break
                        
                    EI.PANTALLA.fill(EI.FONDO) #Se limpia la pantalla

                    #Se comprueba si el control deslizante está a la izquierda
                    if posicion_relativa != 0:
                        EI.PANTALLA.blit(iconosonido_ajustado, (EI.ancho * 0.07, EI.alto * 0.06)) #Se imprime el icono del sonido
                        Gris = True
                    else: 
                        EI.PANTALLA.blit(iconosinsonido_ajustado, (EI.ancho * 0.07, EI.alto * 0.06)) #Se imprime el icono de que no hay sonido
                        Gris = False
                    if brillo != 0:
                        EI.PANTALLA.blit(iconobrillo_ajustado, (EI.ancho * 0.07, EI.alto * 0.36)) #Se imprime el icono del brillo
                        Gris_brillo = True
                    else: 
                        EI.PANTALLA.blit(iconosinbrillo_ajustado, (EI.ancho * 0.07, EI.alto * 0.36)) #Se imprime el icono de que no hay brillo
                        Gris_brillo = False

                    EI.PANTALLA.blit(texto_musica, (EI.ancho * 0.55, EI.alto * 0.085)) #Se imprime el texto "Music"
                    EI.PANTALLA.blit(texto_brillo, (EI.ancho * 0.55, EI.alto * 0.38)) #Se imprime el texto "Brillo"

                    mouse_x, mouse_y = pygame.mouse.get_pos() #Obtenemos la posición del mouse

                    #Dibujamos barra con control desplazable para el sonido
                    if EI.alto * 0.09 <= mouse_y <= EI.alto * 0.09 + EI.alto * 0.05 and EI.ancho * 0.195 <= mouse_x <= EI.ancho * 0.489:  #Verificamos si el mouse está dentro de los límites de la barra 
                        posicion_relativa = (mouse_x - (EI.ancho * 0.2)) / (EI.ancho * 0.3) #Calculamos la posición relativa del control deslizante azul en la barra 
                        posicion_relativa = max(0, min(1, posicion_relativa)) #Asegurarse de que la posición relativa esté en el rango [0, 1]
                        volumen = posicion_relativa

                        pygame.mixer.music.set_volume(volumen) #Establecer volumen de la música
                        if Gris:
                            EI.dibujar_barra(mouse_x, EI.NEGRO, EI.AZUL, EI.AZUL, EI.ancho * 0.2, EI.alto * 0.1, EI.ancho * 0.3, EI.alto * 0.03, EI.ancho * 0.02, EI.alto * 0.05) #Dibujar barra desplazable
                        else: EI.dibujar_barra(mouse_x, EI.GRIS, EI.AZUL, EI.GRIS, EI.ancho * 0.2, EI.alto * 0.1, EI.ancho * 0.3, EI.alto * 0.03, EI.ancho * 0.02, EI.alto * 0.05) #Dibujar barra desplazable
                        mouseantiguo_x = mouse_x
                    else:
                        if Gris:
                            EI.dibujar_barra(mouseantiguo_x, EI.NEGRO, EI.AZUL, EI.AZUL, EI.ancho * 0.2, EI.alto * 0.1, EI.ancho * 0.3, EI.alto * 0.03, EI.ancho * 0.02, EI.alto * 0.05) #Dibujar barra desplazable
                        else: EI.dibujar_barra(mouseantiguo_x, EI.GRIS, EI.AZUL, EI.GRIS, EI.ancho * 0.2, EI.alto * 0.1, EI.ancho * 0.3, EI.alto * 0.03, EI.ancho * 0.02, EI.alto * 0.05) #Dibujar barra desplazable
                    
                    #Dibujamos barra con control desplazable para el brillo
                    if EI.alto * 0.4 <= mouse_y <= EI.alto * 0.4 + EI.alto * 0.05 and EI.ancho * 0.195 <= mouse_x <= EI.ancho * 0.489:  #Verificamos si el mouse está dentro de los límites de la barra 
                        brillo = (mouse_x - (EI.ancho * 0.2)) / (EI.ancho * 0.3) #Calculamos la posición relativa del control deslizante azul en la barra 
                        brillo = max(0, min(1, brillo)) #Asegurarse de que la posición relativa esté en el rango [0, 1]
                        pygame.display.set_gamma(brillo) #Se aplica el brillo a la pantalla

                        if Gris_brillo:
                            EI.dibujar_barra(mouse_x, EI.NEGRO, EI.AZUL, EI.AZUL, EI.ancho * 0.2, EI.alto * 0.4, EI.ancho * 0.3, EI.alto * 0.03, EI.ancho * 0.02, EI.alto * 0.05) #Dibujar barra desplazable 
                        else: EI.dibujar_barra(mouse_x, EI.GRIS, EI.AZUL, EI.GRIS, EI.ancho * 0.2, EI.alto * 0.4, EI.ancho * 0.3, EI.alto * 0.03, EI.ancho * 0.02, EI.alto * 0.05) #Dibujar barra desplazable
                        mouseantiguo_x_brillo = mouse_x
                    else:
                        if Gris_brillo:
                            EI.dibujar_barra(mouseantiguo_x_brillo, EI.NEGRO, EI.AZUL, EI.AZUL, EI.ancho * 0.2, EI.alto * 0.4, EI.ancho * 0.3, EI.alto * 0.03, EI.ancho * 0.02, EI.alto * 0.05) #Dibujar barra desplazable
                        else: EI.dibujar_barra(mouseantiguo_x_brillo, EI.GRIS, EI.AZUL, EI.GRIS, EI.ancho * 0.2, EI.alto * 0.4, EI.ancho * 0.3, EI.alto * 0.03, EI.ancho * 0.02, EI.alto * 0.05) #Dibujar barra desplazable
                    
                    #Mostramos los botones
                    boton_cancelar.dibujar(EI.PANTALLA)
                    boton_aceptar.dibujar(EI.PANTALLA)

                    pygame.display.flip() #Actualizar la pantalla
        pygame.display.update()

#Texto
fuente_2 = pygame.font.Font("Fuentes/Nicolast.otf", int(EI.ancho * 0.04)) 
texto_seleccionar = fuente_2.render('Selecciona   tu   personaje', True, (EI.ROJO))

#Botones
boton_personaje1 = EI.Boton(EI.ancho * 0.25, EI.alto * 0.27, EI.ancho * 0.2, EI.alto * 0.5, "", 0, 0)
boton_personaje2 = EI.Boton(EI.ancho * 0.55, EI.alto * 0.27, EI.ancho * 0.2, EI.alto * 0.5, "", 0, 0)
boton_aceptar = EI.Boton(EI.ancho * 0.6, EI.alto * 0.85, EI.ancho * 0.2, EI.alto * 0.1, "Aceptar", int(EI.ancho * 0.05), int(EI.ancho * 0.015))

#Imágenes
#Personaje 1
quieto_derecha1 = pygame.image.load("Imagenes/Sprites/Personaje_1/quieto_derecha.png")
quieto_derecha1 = pygame.transform.scale(quieto_derecha1, (EI.ancho * 0.09, EI.alto * 0.4)) #Se adecua el sprite a un tamaño específico
#Personaje 2
quieto_derecha2 = pygame.image.load("Imagenes/Sprites/Personaje_2/quieto_derecha.png")
quieto_derecha2 = pygame.transform.scale(quieto_derecha2, (EI.ancho * 0.1, EI.alto * 0.4)) #Se adecua el sprite a un tamaño específico

#Booleanos
p1 = False
p2 = False
controlar_bucle = False
dialog_continue = True
num_dialog = -1

if cargar:
    #Cargar los datos guardados
    loaded_data = EI.cargar_informacion()

    if loaded_data:
        completar_variables = loaded_data["completar_variables"]
        completar_condicionales = loaded_data["completar_condicionales"]
        completar_ciclos = loaded_data["completar_ciclos"]
        completar_funciones = loaded_data["completar_funciones"]
        completar_examen_final = loaded_data["completar_examen_final"]
    else:
        completar_variables = False
        completar_condicionales = False
        completar_ciclos = False
        completar_funciones = False
        completar_examen_final = False
if nueva:
    completar_variables = False
    completar_condicionales = False
    completar_ciclos = False
    completar_funciones = False
    completar_examen_final = False

#Personajes
variably = pygame.transform.scale(EI.variably,(EI.ancho*0.2,EI.alto*0.3))
variably_rect = variably.get_rect()
variably_rect.bottomleft = (EI.ancho*0.01,EI.alto*0.7)

#Fondos
fondo_aldea = pygame.transform.scale(EI.fondo_aldea,(EI.ancho*0.8,EI.alto*0.7))
fondo_aldea_rect = fondo_aldea.get_rect()
fondo_aldea_rect.midtop = (EI.ancho//2, 0)

boton_aceptar = EI.Boton(EI.ancho * 0.4, EI.alto * 0.85, EI.ancho * 0.2, EI.alto * 0.1, "Aceptar", int(EI.ancho * 0.05), int(EI.ancho * 0.015)) #Actualizamos la posición del botón 

while True:
    if controlar_bucle:
        break
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                romper = False
            #Si se presiona la tecla "Esc", entonces aparece un cuadro de dialogo para confirmar la salida
                while True:
                    if romper == True:
                        break
                    EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
                    EI.PANTALLA.blit(texto_salida, (EI.ancho * 0.3, EI.alto * 0.4))
                    boton_salida.dibujar(EI.PANTALLA)
                    boton_salida2.dibujar(EI.PANTALLA)
                    for evento in pygame.event.get():
                        if evento.type == pygame.MOUSEMOTION:
                            #Si el cursor del mouse pasa por encima de algún botón, entonces su color cambia
                            boton_salida.color_normal = EI.AZUL if not boton_salida.esta_encima(evento.pos) else EI.ROJO
                            boton_salida2.color_normal = EI.AZUL if not boton_salida2.esta_encima(evento.pos) else EI.ROJO
                        if evento.type == pygame.MOUSEBUTTONDOWN:
                            #Si se presiona 'Regresar', entonces se rompe el ciclo
                            if boton_salida2.esta_encima(evento.pos):
                                romper = True
                                break
                            #Si se presiona 'Guardar y salir', entonces se guarda el progreso y se termina el programa
                            if boton_salida.esta_encima(evento.pos):
                                EI.guardar_informacion({"completar_variables": completar_variables,"completar_condicionales": completar_condicionales,"completar_ciclos": completar_ciclos,"completar_funciones": completar_funciones, "completar_examen_final": completar_examen_final})
                                pygame.quit()
                                sys.exit()
                        pygame.display.update()
        #Si se da click con el mouse encima de algún botón, entonces su color cambia
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_personaje1.esta_encima(evento.pos):
            boton_personaje1.color_normal = EI.ROJO 
            boton_personaje2.color_normal = EI.AZUL
            p1 = True
            p2 = False
            
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_personaje2.esta_encima(evento.pos):
            boton_personaje2.color_normal = EI.ROJO
            boton_personaje1.color_normal = EI.AZUL 
            p2 = True
            p1 = False

        if evento.type == pygame.MOUSEMOTION:
            #Si el cursor del mouse pasa por encima de algún  botón, entonces su color cambia
            boton_personaje1.color_normal = EI.AZUL if not boton_personaje1.esta_encima(evento.pos) and not p1 else EI.ROJO
            boton_personaje2.color_normal = EI.AZUL if not boton_personaje2.esta_encima(evento.pos) and not p2 else EI.ROJO
            boton_aceptar.color_normal = EI.AZUL if not boton_aceptar.esta_encima(evento.pos) else EI.ROJO
        
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_aceptar.esta_encima(evento.pos) and (p1 or p2):
            if p1:
                seleccion = 1 
            elif p2:
                seleccion = 2
            else: seleccion = 3
            controlar_bucle = True
            break

    EI.PANTALLA.fill(EI.FONDO) #Se limpia la pantalla
    #Mostramos los botones
    boton_personaje1.dibujar(EI.PANTALLA)
    boton_personaje2.dibujar(EI.PANTALLA)
    boton_aceptar.dibujar(EI.PANTALLA)
    
    EI.PANTALLA.blit(quieto_derecha1, (EI.ancho * 0.30, EI.alto * 0.32)) #Se imprime la imágen del personaje 1
    EI.PANTALLA.blit(quieto_derecha2, (EI.ancho * 0.60, EI.alto * 0.32)) #Se imprime la imágen del personaje 2

    EI.PANTALLA.blit(texto_seleccionar, (EI.ancho * 0.2, EI.alto * 0.1)) #Se imprime el texto "Selecciona tu personaje"
    

    pygame.display.flip() #Actualizar la pantalla

if seleccion == 1:
    #Cargamos las hojas de sprites del personaje 1
    quieto_derecha = pygame.image.load("Imagenes/Sprites/Personaje_1/quieto_derecha.png")
    quieto_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_1/quieto_izquierda.png")
    correr_derecha = pygame.image.load("Imagenes/Sprites/Personaje_1/correr_derecha.png")
    caminar_derecha = pygame.image.load("Imagenes/Sprites/Personaje_1/caminar_derecha.png")
    caminar_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_1/caminar_izquierda.png")
    correr_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_1/correr_izquierda.png")
    ataque1_derecha = pygame.image.load("Imagenes/Sprites/Personaje_1/ataque1_derecha.png")
    ataque1_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_1/ataque1_izquierda.png")
    ataque3_derecha = pygame.image.load("Imagenes/Sprites/Personaje_1/ataque3_derecha.png")
    ataque3_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_1/ataque3_izquierda.png")
    saltar_derecha = pygame.image.load("Imagenes/Sprites/Personaje_1/saltar_derecha.png")
    saltar_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_1/saltar_izquierda.png")
    #Extraemos los sprites individuales del personaje 1
    sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//10, 87, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//10, 87, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//4, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//4, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
elif seleccion == 2:
    #Cargamos las hojas de sprites del personaje 2
    quieto_derecha = pygame.image.load("Imagenes/Sprites/Personaje_2/quieto_derecha.png")
    quieto_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_2/quieto_izquierda.png")
    correr_derecha = pygame.image.load("Imagenes/Sprites/Personaje_2/correr_derecha.png")
    caminar_derecha = pygame.image.load("Imagenes/Sprites/Personaje_2/caminar_derecha.png")
    caminar_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_2/caminar_izquierda.png")
    correr_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_2/correr_izquierda.png")
    ataque1_derecha = pygame.image.load("Imagenes/Sprites/Personaje_2/ataque1_derecha.png")
    ataque1_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_2/ataque1_izquierda.png")
    ataque3_derecha = pygame.image.load("Imagenes/Sprites/Personaje_2/ataque3_derecha.png")
    ataque3_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_2/ataque3_izquierda.png")
    saltar_derecha = pygame.image.load("Imagenes/Sprites/Personaje_2/saltar_derecha.png")
    saltar_izquierda = pygame.image.load("Imagenes/Sprites/Personaje_2/saltar_izquierda.png")
    #Extraemos los sprites individuales del personaje 2
    sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//12, 85, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//12, 85, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 75, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 75, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//5, 80, 128, EI.ancho * 0.2, EI.alto * 0.22)
    sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//5, 80, 128, EI.ancho * 0.2, EI.alto * 0.22)



altura = EI.alto * 0.3
velocidad_personaje = EI.ancho * 0.4
estado_caminar_derecha = None
estado_caminar_izquierda = None
estado_correr_derecha = None
estado_correr_izquierda = None
saltando = None
anterior = 'derecha'
ataque1 = None
ataque3 = None
posx_hitbox_derecha = EI.ancho * 0.43
posy_hitbox_derecha = EI.alto * 0.3
posx_hitbox_izquierda = EI.ancho * 0.44

#Iconos
numero_dialogos = 0 
quieto_derecha = pygame.transform.scale(quieto_derecha, (EI.ancho * 0.05, EI.alto * 0.22)) #Se adecua el sprite a un tamaño específico
quieto_izquierda = pygame.transform.scale(quieto_izquierda, (EI.ancho * 0.05, EI.alto * 0.22)) #Se adecua el sprite a un tamaño específico
flechas = pygame.transform.scale(EI.flechas, (EI.ancho * 0.25, EI.alto * 0.2))
flecha_izquierda = pygame.transform.scale(EI.flecha_izquierda, (EI.ancho * 0.25, EI.alto * 0.2))
flecha_derecha = pygame.transform.scale(EI.flecha_derecha, (EI.ancho * 0.25, EI.alto * 0.2))
flecha_abajo = pygame.transform.scale(EI.flecha_abajo, (EI.ancho * 0.25, EI.alto * 0.2))
flecha_arriba = pygame.transform.scale(EI.flecha_arriba, (EI.ancho * 0.25, EI.alto * 0.2))
fondo1 = pygame.transform.scale(EI.fondo_1, (EI.ancho, EI.alto))
fondo2 = pygame.transform.scale(EI.fondo_2, (EI.ancho, EI.alto))
fondo3 = pygame.transform.scale(EI.fondo_3, (EI.ancho, EI.alto))
shift = pygame.transform.scale(EI.shift, (EI.ancho * 0.15, EI.alto * 0.2))
shift_flechaizquierda = pygame.transform.scale(EI.shift_flechaizquierda, (EI.ancho * 0.15, EI.alto * 0.2))
shift_flechaderecha = pygame.transform.scale(EI.shift_flechaderecha, (EI.ancho * 0.15, EI.alto * 0.2))
shift_izquierda = pygame.transform.scale(EI.shift_izquierda, (EI.ancho * 0.15, EI.alto * 0.2))
shift_derecha = pygame.transform.scale(EI.shift_derecha, (EI.ancho * 0.15, EI.alto * 0.2))
espacio_sinpresionar = pygame.transform.scale(EI.espacio_sinpresionar, (EI.ancho * 0.3, EI.alto * 0.1))
espacio_presionado = pygame.transform.scale(EI.espacio_presionado, (EI.ancho * 0.3, EI.alto * 0.1))
tecla_x = pygame.transform.scale(EI.tecla_x, (EI.ancho * 0.08, EI.alto * 0.1))
tecla_xpresionada = pygame.transform.scale(EI.tecla_xpresionada, (EI.ancho * 0.08, EI.alto * 0.1))
tecla_z = pygame.transform.scale(EI.tecla_z, (EI.ancho * 0.08, EI.alto * 0.1))
tecla_zpresionada = pygame.transform.scale(EI.tecla_zpresionada, (EI.ancho * 0.08, EI.alto * 0.1))

if nueva:
    while True:

        #Se crea un rectangulo que corresponde a la hitbox del personaje
        if anterior == "derecha":
            hitbox = pygame.Rect(posx_hitbox_derecha, posy_hitbox_derecha, EI.ancho * 0.05, EI.alto * 0.22)
        elif anterior == "izquierda":
            hitbox = pygame.Rect(posx_hitbox_izquierda, posy_hitbox_derecha, EI.ancho * 0.05, EI.alto * 0.22)
        
        #Se imprimen los fondos
        if numero_dialogos == 0 or numero_dialogos >= 5:
            EI.PANTALLA.blit(fondo3, (0, 0))
        else: EI.PANTALLA.blit(fondo1, (0, 0))

        for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    romper = False
                    #Si se presiona la tecla "Esc", entonces aparece un cuadro de dialogo para confirmar la salida
                    while True:
                        if romper == True:
                            break
                        EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
                        EI.PANTALLA.blit(texto_salida, (EI.ancho * 0.3, EI.alto * 0.4))
                        boton_salida.dibujar(EI.PANTALLA)
                        boton_salida2.dibujar(EI.PANTALLA)
                        for evento in pygame.event.get():
                            if evento.type == pygame.MOUSEMOTION:
                                #Si el cursor del mouse pasa por encima de algún botón, entonces su color cambia
                                boton_salida.color_normal = EI.AZUL if not boton_salida.esta_encima(evento.pos) else EI.ROJO
                                boton_salida2.color_normal = EI.AZUL if not boton_salida2.esta_encima(evento.pos) else EI.ROJO
                            if evento.type == pygame.MOUSEBUTTONDOWN:
                                #Si se presiona 'Regresar', entonces se rompe el ciclo
                                if boton_salida2.esta_encima(evento.pos):
                                    romper = True
                                    break
                                #Si se presiona 'Guardar y salir', entonces se guarda el progreso y se termina el programa
                                if boton_salida.esta_encima(evento.pos):
                                    EI.guardar_informacion({"completar_variables": completar_variables,"completar_condicionales": completar_condicionales,"completar_ciclos": completar_ciclos,"completar_funciones": completar_funciones, "completar_examen_final": completar_examen_final})
                                    pygame.quit()
                                    sys.exit()
                            pygame.display.update()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
                        numero_dialogos += 1
                
                    #Si se presiona la tecla "espacio", entonces el personaje salta
                    if evento.key == pygame.K_SPACE and numero_dialogos >= 3:
                        saltando = True

                    #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1
                    if evento.key == pygame.K_x and numero_dialogos >= 4:
                        ataque1 = True

                    #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3
                    if evento.key == pygame.K_z and numero_dialogos >= 4:
                        ataque3 = True

        teclas = pygame.key.get_pressed()
        
        if numero_dialogos == 0:
            EI.mostrar_texto("Tutorial", "Bienvenid@ al tutorial básico.", "¿Estás list@ para iniciar esta nueva aventura?", "Presiona 'Enter' para continuar.", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
        
        #Primera parte del tutorial
        if numero_dialogos == 1:
            EI.mostrar_texto("Movimientos", "Para comenzar, usa las flechas para desplazarte:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(flechas, (EI.ancho * 0.65, EI.alto * 0.75))
            #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
            if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
            if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))

            #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
            if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "derecha" or anterior == None) and posy_hitbox_derecha < EI.alto * 0.48:
                altura += EI.alto * 0.01
                posy_hitbox_derecha += EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Para comenzar, usa las flechas para desplazarte:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(flecha_abajo, (EI.ancho * 0.65, EI.alto * 0.75))

            #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
            if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "izquierda") and posy_hitbox_derecha < EI.alto * 0.48:
                altura += EI.alto * 0.01
                posy_hitbox_derecha += EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Para comenzar, usa las flechas para desplazarte:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(flecha_abajo, (EI.ancho * 0.65, EI.alto * 0.75))

            #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
            if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "derecha" or anterior == None):
                if posy_hitbox_derecha > 0:
                    altura -= EI.alto * 0.01
                    posy_hitbox_derecha -= EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Para comenzar, usa las flechas para desplazarte:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(flecha_arriba, (EI.ancho * 0.65, EI.alto * 0.75))
            
            #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
            if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "izquierda"):
                if posy_hitbox_derecha > 0:
                    altura -= EI.alto * 0.01
                    posy_hitbox_derecha -= EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Para comenzar, usa las flechas para desplazarte:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(flecha_arriba, (EI.ancho * 0.65, EI.alto * 0.75))
            
            #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Para comenzar, usa las flechas para desplazarte:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(flecha_derecha, (EI.ancho * 0.65, EI.alto * 0.75))
                if posx_hitbox_derecha < EI.ancho * 0.95:
                    velocidad_personaje += EI.ancho * 0.002 
                    posx_hitbox_derecha += EI.ancho * 0.002
                    posx_hitbox_izquierda += EI.ancho * 0.002
                sumar = - EI.ancho * 0.04
                anterior = "derecha"

                if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                    EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 0
                elif estado_caminar_derecha == 0:
                    EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 1
                elif estado_caminar_derecha == 1:
                    EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 2
                elif estado_caminar_derecha == 2:
                    EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 3
                elif estado_caminar_derecha == 3:
                    EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 4
                elif estado_caminar_derecha == 4:
                    EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 5
                elif estado_caminar_derecha == 5:
                    EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 6
                elif estado_caminar_derecha == 6:
                    EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 7

            #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
            if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Para comenzar, usa las flechas para desplazarte:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(flecha_izquierda, (EI.ancho * 0.65, EI.alto * 0.75))
                if posx_hitbox_izquierda > 0:
                    velocidad_personaje -= EI.ancho * 0.002 
                    posx_hitbox_derecha -= EI.ancho * 0.002
                    posx_hitbox_izquierda -= EI.ancho * 0.002

                sumar = - EI.ancho * 0.05
                anterior = "izquierda"
                
                if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 0
                elif estado_caminar_izquierda == 0:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 1
                elif estado_caminar_izquierda == 1:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 2
                elif estado_caminar_izquierda == 2:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 3
                elif estado_caminar_izquierda == 3:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 4
                elif estado_caminar_izquierda == 4:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 5
                elif estado_caminar_izquierda == 5:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 6
                elif estado_caminar_izquierda == 6:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 7

        #Segunda parte del tutorial (shift + flechas)

        if numero_dialogos == 2:
            EI.mostrar_texto("Movimientos", "Puedes presionar las flechas + shift para correr:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(shift, (EI.ancho * 0.7, EI.alto * 0.75))
            #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
            if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
            if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))

            #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
            if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "derecha" or anterior == None) and posy_hitbox_derecha < EI.alto * 0.48:
                altura += EI.alto * 0.01
                posy_hitbox_derecha += EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar las flechas + shift para correr:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(shift, (EI.ancho * 0.7, EI.alto * 0.75))

            #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
            if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "izquierda") and posy_hitbox_derecha < EI.alto * 0.48:
                altura += EI.alto * 0.01
                posy_hitbox_derecha += EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar las flechas + shift para correr:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(shift, (EI.ancho * 0.7, EI.alto * 0.75))

            #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
            if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "derecha" or anterior == None):
                if posy_hitbox_derecha > 0:
                    altura -= EI.alto * 0.01
                    posy_hitbox_derecha -= EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar las flechas + shift para correr:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(shift, (EI.ancho * 0.7, EI.alto * 0.75))
            
            #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
            if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "izquierda"):
                if posy_hitbox_derecha > 0:
                    altura -= EI.alto * 0.01
                    posy_hitbox_derecha -= EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar las flechas + shift para correr:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(shift, (EI.ancho * 0.7, EI.alto * 0.75))
            
            #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar las flechas + shift para correr:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(shift_flechaderecha, (EI.ancho * 0.7, EI.alto * 0.75))
                if posx_hitbox_derecha < EI.ancho * 0.95:
                    velocidad_personaje += EI.ancho * 0.002 
                    posx_hitbox_derecha += EI.ancho * 0.002
                    posx_hitbox_izquierda += EI.ancho * 0.002
                sumar = - EI.ancho * 0.04
                anterior = "derecha"

                if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                    EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 0
                elif estado_caminar_derecha == 0:
                    EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 1
                elif estado_caminar_derecha == 1:
                    EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 2
                elif estado_caminar_derecha == 2:
                    EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 3
                elif estado_caminar_derecha == 3:
                    EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 4
                elif estado_caminar_derecha == 4:
                    EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 5
                elif estado_caminar_derecha == 5:
                    EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 6
                elif estado_caminar_derecha == 6:
                    EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 7

            #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
            if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar las flechas + shift para correr:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(shift_flechaizquierda, (EI.ancho * 0.7, EI.alto * 0.75))
                if posx_hitbox_izquierda > 0:
                    velocidad_personaje -= EI.ancho * 0.002 
                    posx_hitbox_derecha -= EI.ancho * 0.002
                    posx_hitbox_izquierda -= EI.ancho * 0.002

                sumar = - EI.ancho * 0.05
                anterior = "izquierda"
                
                if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 0
                elif estado_caminar_izquierda == 0:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 1
                elif estado_caminar_izquierda == 1:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 2
                elif estado_caminar_izquierda == 2:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 3
                elif estado_caminar_izquierda == 3:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 4
                elif estado_caminar_izquierda == 4:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 5
                elif estado_caminar_izquierda == 5:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 6
                elif estado_caminar_izquierda == 6:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 7

            #Si la tecla derecha o "d" y shift están siendo presionadas, entonces el personaje corre hacia la derecha
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar las flechas + shift para correr:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(shift_derecha, (EI.ancho * 0.7, EI.alto * 0.75))
                if posx_hitbox_derecha < EI.ancho * 0.9:
                    velocidad_personaje += EI.ancho * 0.003
                    posx_hitbox_derecha += EI.ancho * 0.003
                    posx_hitbox_izquierda += EI.ancho * 0.003
                sumar = -EI.ancho * 0.05
                anterior = "derecha"
                if estado_correr_derecha == None or estado_correr_derecha == 7:
                    EI.PANTALLA.blit(sprites_correr_derecha[0], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 0
                elif estado_correr_derecha == 0:
                    EI.PANTALLA.blit(sprites_correr_derecha[1], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 1
                elif estado_correr_derecha == 1:
                    EI.PANTALLA.blit(sprites_correr_derecha[2], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 2
                elif estado_correr_derecha == 2:
                    EI.PANTALLA.blit(sprites_correr_derecha[3], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 3
                elif estado_correr_derecha == 3:
                    EI.PANTALLA.blit(sprites_correr_derecha[4], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 4
                elif estado_correr_derecha == 4:
                    EI.PANTALLA.blit(sprites_correr_derecha[5], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 5
                elif estado_correr_derecha == 5:
                    EI.PANTALLA.blit(sprites_correr_derecha[6], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 6
                elif estado_correr_derecha == 6:
                    EI.PANTALLA.blit(sprites_correr_derecha[7], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 7

            #Si la tecla izquierda o "a" y shift están siendo presionadas, entonces el personaje corre hacia la izquierda
            if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar las flechas + shift para correr:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(shift_izquierda, (EI.ancho * 0.7, EI.alto * 0.75))
                if posx_hitbox_izquierda > EI.ancho * 0.05:
                    velocidad_personaje -= EI.ancho * 0.003
                    posx_hitbox_derecha -= EI.ancho * 0.003
                    posx_hitbox_izquierda -= EI.ancho * 0.003
                anterior = "izquierda"
                if estado_correr_izquierda == None or estado_correr_izquierda == 7:
                    EI.PANTALLA.blit(sprites_correr_izquierda[7], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 0
                elif estado_correr_izquierda == 0:
                    EI.PANTALLA.blit(sprites_correr_izquierda[6], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 1
                elif estado_correr_izquierda == 1:
                    EI.PANTALLA.blit(sprites_correr_izquierda[5], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 2
                elif estado_correr_izquierda == 2:
                    EI.PANTALLA.blit(sprites_correr_izquierda[4], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 3
                elif estado_correr_izquierda == 3:
                    EI.PANTALLA.blit(sprites_correr_izquierda[3], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 4
                elif estado_correr_izquierda == 4:
                    EI.PANTALLA.blit(sprites_correr_izquierda[2], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 5
                elif estado_correr_izquierda == 5:
                    EI.PANTALLA.blit(sprites_correr_izquierda[1], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 6
                elif estado_correr_izquierda == 6:
                    EI.PANTALLA.blit(sprites_correr_izquierda[0], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 7

        #Tercera parte del tutorial

        if numero_dialogos == 3:
            EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(espacio_sinpresionar, (EI.ancho * 0.6, EI.alto * 0.8))
            #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
            if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
            if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))

            #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
            if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "derecha" or anterior == None) and posy_hitbox_derecha < EI.alto * 0.48:
                altura += EI.alto * 0.01
                posy_hitbox_derecha += EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(espacio_sinpresionar, (EI.ancho * 0.6, EI.alto * 0.8))

            #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
            if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "izquierda") and posy_hitbox_derecha < EI.alto * 0.48:
                altura += EI.alto * 0.01
                posy_hitbox_derecha += EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(espacio_sinpresionar, (EI.ancho * 0.6, EI.alto * 0.8))

            #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
            if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "derecha" or anterior == None):
                if posy_hitbox_derecha > 0:
                    altura -= EI.alto * 0.01
                    posy_hitbox_derecha -= EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(espacio_sinpresionar, (EI.ancho * 0.6, EI.alto * 0.8))
            
            #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
            if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "izquierda"):
                if posy_hitbox_derecha > 0:
                    altura -= EI.alto * 0.01
                    posy_hitbox_derecha -= EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(espacio_sinpresionar, (EI.ancho * 0.6, EI.alto * 0.8))
            
            #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(espacio_sinpresionar, (EI.ancho * 0.6, EI.alto * 0.8))
                if posx_hitbox_derecha < EI.ancho * 0.95:
                    velocidad_personaje += EI.ancho * 0.002 
                    posx_hitbox_derecha += EI.ancho * 0.002
                    posx_hitbox_izquierda += EI.ancho * 0.002
                sumar = - EI.ancho * 0.04
                anterior = "derecha"

                if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                    EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 0
                elif estado_caminar_derecha == 0:
                    EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 1
                elif estado_caminar_derecha == 1:
                    EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 2
                elif estado_caminar_derecha == 2:
                    EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 3
                elif estado_caminar_derecha == 3:
                    EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 4
                elif estado_caminar_derecha == 4:
                    EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 5
                elif estado_caminar_derecha == 5:
                    EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 6
                elif estado_caminar_derecha == 6:
                    EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 7

            #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
            if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(espacio_sinpresionar, (EI.ancho * 0.6, EI.alto * 0.8))
                if posx_hitbox_izquierda > 0:
                    velocidad_personaje -= EI.ancho * 0.002 
                    posx_hitbox_derecha -= EI.ancho * 0.002
                    posx_hitbox_izquierda -= EI.ancho * 0.002

                sumar = - EI.ancho * 0.05
                anterior = "izquierda"
                
                if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 0
                elif estado_caminar_izquierda == 0:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 1
                elif estado_caminar_izquierda == 1:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 2
                elif estado_caminar_izquierda == 2:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 3
                elif estado_caminar_izquierda == 3:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 4
                elif estado_caminar_izquierda == 4:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 5
                elif estado_caminar_izquierda == 5:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 6
                elif estado_caminar_izquierda == 6:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 7

            #Si la tecla derecha o "d" y shift están siendo presionadas, entonces el personaje corre hacia la derecha
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(espacio_sinpresionar, (EI.ancho * 0.6, EI.alto * 0.8))
                if posx_hitbox_derecha < EI.ancho * 0.9:
                    velocidad_personaje += EI.ancho * 0.003
                    posx_hitbox_derecha += EI.ancho * 0.003
                    posx_hitbox_izquierda += EI.ancho * 0.003
                sumar = -EI.ancho * 0.05
                anterior = "derecha"
                if estado_correr_derecha == None or estado_correr_derecha == 7:
                    EI.PANTALLA.blit(sprites_correr_derecha[0], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 0
                elif estado_correr_derecha == 0:
                    EI.PANTALLA.blit(sprites_correr_derecha[1], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 1
                elif estado_correr_derecha == 1:
                    EI.PANTALLA.blit(sprites_correr_derecha[2], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 2
                elif estado_correr_derecha == 2:
                    EI.PANTALLA.blit(sprites_correr_derecha[3], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 3
                elif estado_correr_derecha == 3:
                    EI.PANTALLA.blit(sprites_correr_derecha[4], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 4
                elif estado_correr_derecha == 4:
                    EI.PANTALLA.blit(sprites_correr_derecha[5], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 5
                elif estado_correr_derecha == 5:
                    EI.PANTALLA.blit(sprites_correr_derecha[6], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 6
                elif estado_correr_derecha == 6:
                    EI.PANTALLA.blit(sprites_correr_derecha[7], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 7

            #Si la tecla izquierda o "a" y shift están siendo presionadas, entonces el personaje corre hacia la izquierda
            if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(espacio_sinpresionar, (EI.ancho * 0.6, EI.alto * 0.8))
                if posx_hitbox_izquierda > EI.ancho * 0.05:
                    velocidad_personaje -= EI.ancho * 0.003
                    posx_hitbox_derecha -= EI.ancho * 0.003
                    posx_hitbox_izquierda -= EI.ancho * 0.003
                anterior = "izquierda"
                if estado_correr_izquierda == None or estado_correr_izquierda == 7:
                    EI.PANTALLA.blit(sprites_correr_izquierda[7], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 0
                elif estado_correr_izquierda == 0:
                    EI.PANTALLA.blit(sprites_correr_izquierda[6], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 1
                elif estado_correr_izquierda == 1:
                    EI.PANTALLA.blit(sprites_correr_izquierda[5], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 2
                elif estado_correr_izquierda == 2:
                    EI.PANTALLA.blit(sprites_correr_izquierda[4], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 3
                elif estado_correr_izquierda == 3:
                    EI.PANTALLA.blit(sprites_correr_izquierda[3], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 4
                elif estado_correr_izquierda == 4:
                    EI.PANTALLA.blit(sprites_correr_izquierda[2], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 5
                elif estado_correr_izquierda == 5:
                    EI.PANTALLA.blit(sprites_correr_izquierda[1], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 6
                elif estado_correr_izquierda == 6:
                    EI.PANTALLA.blit(sprites_correr_izquierda[0], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 7
                
            #Si se presiona la tecla "espacio", entonces el personaje salta
            if saltando and (anterior == "derecha" or anterior == None):
                if posx_hitbox_derecha < EI.ancho * 0.9:
                    posx_hitbox_derecha += EI.ancho * 0.03
                    posx_hitbox_izquierda += EI.ancho * 0.03
                for sprite in sprites_saltar_derecha:
                    EI.PANTALLA.blit(fondo1, (0, 0))
                    EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                    EI.PANTALLA.blit(espacio_presionado, (EI.ancho * 0.6, EI.alto * 0.8))
                    if posx_hitbox_derecha < EI.ancho * 0.9:
                        velocidad_personaje += EI.ancho * 0.003
                    EI.PANTALLA.blit(sprite, (velocidad_personaje - EI.ancho * 0.045, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                    pygame.display.flip()  #Se actualiza la pantalla
                    pygame.time.delay(50)  #Se pausa la ejecución durante un breve período de tiempo
                saltando = False
            

            #Si se presiona la tecla "espacio", entonces el personaje salta
            if saltando and (anterior == "izquierda"):
                if posx_hitbox_izquierda > 0:
                    posx_hitbox_derecha -= EI.ancho * 0.031
                    posx_hitbox_izquierda -= EI.ancho * 0.031
                for sprite in sprites_saltar_izquierda[::-1]:
                    EI.PANTALLA.blit(fondo1, (0, 0))
                    EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                    EI.PANTALLA.blit(espacio_presionado, (EI.ancho * 0.6, EI.alto * 0.8))
                    if posx_hitbox_izquierda > 0:
                        velocidad_personaje -= EI.ancho * 0.003
                    EI.PANTALLA.blit(sprite, (velocidad_personaje - EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                    pygame.display.flip()  #Se actualiza la pantalla
                    pygame.time.delay(50)  #Se pausa la ejecución durante un breve período de tiempo
                saltando = False

        #Cuarta parte del tutorial

        if numero_dialogos == 4:
            EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
            EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
            #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
            if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
            if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))

            #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
            if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "derecha" or anterior == None) and posy_hitbox_derecha < EI.alto * 0.48:
                altura += EI.alto * 0.01
                posy_hitbox_derecha += EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))

                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))

            #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
            if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "izquierda") and posy_hitbox_derecha < EI.alto * 0.48:
                altura += EI.alto * 0.01
                posy_hitbox_derecha += EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))

            #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
            if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "derecha" or anterior == None):
                if posy_hitbox_derecha > 0:
                    altura -= EI.alto * 0.01
                    posy_hitbox_derecha -= EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
            
            #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
            if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "izquierda"):
                if posy_hitbox_derecha > 0:
                    altura -= EI.alto * 0.01
                    posy_hitbox_derecha -= EI.ancho * 0.0055
                EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
            
            #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
                if posx_hitbox_derecha < EI.ancho * 0.95:
                    velocidad_personaje += EI.ancho * 0.002 
                    posx_hitbox_derecha += EI.ancho * 0.002
                    posx_hitbox_izquierda += EI.ancho * 0.002
                sumar = - EI.ancho * 0.04
                anterior = "derecha"

                if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                    EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 0
                elif estado_caminar_derecha == 0:
                    EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 1
                elif estado_caminar_derecha == 1:
                    EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 2
                elif estado_caminar_derecha == 2:
                    EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 3
                elif estado_caminar_derecha == 3:
                    EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 4
                elif estado_caminar_derecha == 4:
                    EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 5
                elif estado_caminar_derecha == 5:
                    EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 6
                elif estado_caminar_derecha == 6:
                    EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje + sumar, altura))
                    estado_caminar_derecha = 7

            #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
            if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
                if posx_hitbox_izquierda > 0:
                    velocidad_personaje -= EI.ancho * 0.002 
                    posx_hitbox_derecha -= EI.ancho * 0.002
                    posx_hitbox_izquierda -= EI.ancho * 0.002

                sumar = - EI.ancho * 0.05
                anterior = "izquierda"
                
                if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 0
                elif estado_caminar_izquierda == 0:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 1
                elif estado_caminar_izquierda == 1:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 2
                elif estado_caminar_izquierda == 2:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 3
                elif estado_caminar_izquierda == 3:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 4
                elif estado_caminar_izquierda == 4:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 5
                elif estado_caminar_izquierda == 5:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 6
                elif estado_caminar_izquierda == 6:
                    EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje + sumar, altura))
                    estado_caminar_izquierda = 7

            #Si la tecla derecha o "d" y shift están siendo presionadas, entonces el personaje corre hacia la derecha
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
                if posx_hitbox_derecha < EI.ancho * 0.9:
                    velocidad_personaje += EI.ancho * 0.003
                    posx_hitbox_derecha += EI.ancho * 0.003
                    posx_hitbox_izquierda += EI.ancho * 0.003
                sumar = -EI.ancho * 0.05
                anterior = "derecha"
                if estado_correr_derecha == None or estado_correr_derecha == 7:
                    EI.PANTALLA.blit(sprites_correr_derecha[0], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 0
                elif estado_correr_derecha == 0:
                    EI.PANTALLA.blit(sprites_correr_derecha[1], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 1
                elif estado_correr_derecha == 1:
                    EI.PANTALLA.blit(sprites_correr_derecha[2], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 2
                elif estado_correr_derecha == 2:
                    EI.PANTALLA.blit(sprites_correr_derecha[3], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 3
                elif estado_correr_derecha == 3:
                    EI.PANTALLA.blit(sprites_correr_derecha[4], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 4
                elif estado_correr_derecha == 4:
                    EI.PANTALLA.blit(sprites_correr_derecha[5], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 5
                elif estado_correr_derecha == 5:
                    EI.PANTALLA.blit(sprites_correr_derecha[6], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 6
                elif estado_correr_derecha == 6:
                    EI.PANTALLA.blit(sprites_correr_derecha[7], (velocidad_personaje + sumar, altura))
                    estado_correr_derecha = 7

            #Si la tecla izquierda o "a" y shift están siendo presionadas, entonces el personaje corre hacia la izquierda
            if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
                EI.PANTALLA.blit(fondo1, (0, 0))
                EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
                if posx_hitbox_izquierda > EI.ancho * 0.05:
                    velocidad_personaje -= EI.ancho * 0.003
                    posx_hitbox_derecha -= EI.ancho * 0.003
                    posx_hitbox_izquierda -= EI.ancho * 0.003
                anterior = "izquierda"
                if estado_correr_izquierda == None or estado_correr_izquierda == 7:
                    EI.PANTALLA.blit(sprites_correr_izquierda[7], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 0
                elif estado_correr_izquierda == 0:
                    EI.PANTALLA.blit(sprites_correr_izquierda[6], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 1
                elif estado_correr_izquierda == 1:
                    EI.PANTALLA.blit(sprites_correr_izquierda[5], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 2
                elif estado_correr_izquierda == 2:
                    EI.PANTALLA.blit(sprites_correr_izquierda[4], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 3
                elif estado_correr_izquierda == 3:
                    EI.PANTALLA.blit(sprites_correr_izquierda[3], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 4
                elif estado_correr_izquierda == 4:
                    EI.PANTALLA.blit(sprites_correr_izquierda[2], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 5
                elif estado_correr_izquierda == 5:
                    EI.PANTALLA.blit(sprites_correr_izquierda[1], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 6
                elif estado_correr_izquierda == 6:
                    EI.PANTALLA.blit(sprites_correr_izquierda[0], (velocidad_personaje + sumar, altura))
                    estado_correr_izquierda = 7
                
            #Si se presiona la tecla "espacio", entonces el personaje salta
            if saltando and (anterior == "derecha" or anterior == None):
                if posx_hitbox_derecha < EI.ancho * 0.9:
                    posx_hitbox_derecha += EI.ancho * 0.03
                    posx_hitbox_izquierda += EI.ancho * 0.03
                for sprite in sprites_saltar_derecha:
                    EI.PANTALLA.blit(fondo1, (0, 0))
                    EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                    EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                    EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
                    if posx_hitbox_derecha < EI.ancho * 0.9:
                        velocidad_personaje += EI.ancho * 0.003
                    EI.PANTALLA.blit(sprite, (velocidad_personaje - EI.ancho * 0.045, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                    pygame.display.flip()  #Se actualiza la pantalla
                    pygame.time.delay(50)  #Se pausa la ejecución durante un breve período de tiempo
                saltando = False

            #Si se presiona la tecla "espacio", entonces el personaje salta
            if saltando and (anterior == "izquierda"):
                if posx_hitbox_izquierda > 0:
                    posx_hitbox_derecha -= EI.ancho * 0.031
                    posx_hitbox_izquierda -= EI.ancho * 0.031
                for sprite in sprites_saltar_izquierda[::-1]:
                    EI.PANTALLA.blit(fondo1, (0, 0))
                    EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                    EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                    EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
                    if posx_hitbox_izquierda > 0:
                        velocidad_personaje -= EI.ancho * 0.003
                    EI.PANTALLA.blit(sprite, (velocidad_personaje - EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                    pygame.display.flip()  #Se actualiza la pantalla
                    pygame.time.delay(50)  #Se pausa la ejecución durante un breve período de tiempo
                saltando = False
            
            #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
            if ataque1 and (anterior == "derecha" or anterior == None):
                restar = EI.ancho * 0.02
                if posx_hitbox_derecha < EI.ancho * 0.85:
                    posx_hitbox_izquierda += EI.ancho * 0.012
                    posx_hitbox_derecha += EI.ancho * 0.012
                for sprite in sprites_ataque1_derecha:
                    EI.PANTALLA.blit(fondo1, (0, 0))
                    EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                    EI.PANTALLA.blit(tecla_xpresionada, (EI.ancho * 0.6, EI.alto * 0.8))
                    EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
                    if posx_hitbox_derecha < EI.ancho * 0.85:
                        velocidad_personaje += EI.ancho * 0.003
                    EI.PANTALLA.blit(sprite, (velocidad_personaje - restar, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                    pygame.display.flip()  #Se actualiza la pantalla
                    pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                ataque1 = False

            #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
            if ataque1 and (anterior == "izquierda"):
                if posx_hitbox_izquierda > 0:
                    posx_hitbox_izquierda -= EI.ancho * 0.012
                    posx_hitbox_derecha -= EI.ancho * 0.012
                for sprite in sprites_ataque1_izquierda[::-1]:
                    EI.PANTALLA.blit(fondo1, (0, 0))
                    EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                    EI.PANTALLA.blit(tecla_xpresionada, (EI.ancho * 0.6, EI.alto * 0.8))
                    EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
                    if posx_hitbox_izquierda > 0:
                        velocidad_personaje -= EI.ancho * 0.003
                    EI.PANTALLA.blit(sprite, (velocidad_personaje - EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                    pygame.display.flip()  #Se actualiza la pantalla
                    pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                ataque1 = False

            #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
            if ataque3 and (anterior == "derecha" or anterior == None):
                restar = EI.ancho * 0.02
                if posx_hitbox_derecha < EI.ancho * 0.85:
                    posx_hitbox_izquierda += EI.ancho * 0.012
                    posx_hitbox_derecha += EI.ancho * 0.012
                for sprite in sprites_ataque3_derecha:
                    EI.PANTALLA.blit(fondo1, (0, 0))
                    EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                    EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                    EI.PANTALLA.blit(tecla_zpresionada, (EI.ancho * 0.7, EI.alto * 0.8))
                    if posx_hitbox_derecha < EI.ancho * 0.85:
                        velocidad_personaje += EI.ancho * 0.003
                    EI.PANTALLA.blit(sprite, (velocidad_personaje - restar, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                    pygame.display.flip()  #Se actualiza la pantalla
                    pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                ataque3 = False

            #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
            if ataque3 and (anterior == "izquierda"):
                if posx_hitbox_izquierda > 0:
                    posx_hitbox_izquierda -= EI.ancho * 0.012
                    posx_hitbox_derecha -= EI.ancho * 0.012
                for sprite in sprites_ataque3_izquierda[::-1]:
                    EI.PANTALLA.blit(fondo1, (0, 0))
                    EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
                    EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
                    EI.PANTALLA.blit(tecla_zpresionada, (EI.ancho * 0.7, EI.alto * 0.8))
                    if posx_hitbox_izquierda > 0:
                        velocidad_personaje -= EI.ancho * 0.003
                    EI.PANTALLA.blit(sprite, (velocidad_personaje - EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                    pygame.display.flip()  #Se actualiza la pantalla
                    pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                ataque3 = False

        if numero_dialogos == 5:
            EI.mostrar_texto("Tutorial", "¡Felicidades!", "Has terminado el tutorial.", "Presiona 'Enter' para continuar.", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
        
        #Se sale del tutorial
        if numero_dialogos == 6:
            break
        pygame.display.update()
    
if seleccion == 1:
    quieto_derecha = pygame.transform.scale(quieto_derecha, (EI.ancho * 0.022, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
    quieto_izquierda = pygame.transform.scale(quieto_izquierda, (EI.ancho * 0.022, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
    #Extraemos los sprites individuales del personaje 1
    sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 78, 128)
    sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 84, 128)
    sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//10, 87, 128)
    sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//10, 87, 128)
    sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 84, 128)
    sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 78, 128)
    sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 81, 128)
    sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 81, 128)
    sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//4, 84, 128)
    sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//4, 84, 128)
elif seleccion == 2:
    quieto_derecha = pygame.transform.scale(quieto_derecha, (EI.ancho * 0.022, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
    quieto_izquierda = pygame.transform.scale(quieto_izquierda, (EI.ancho * 0.022, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
    #Extraemos los sprites individuales del personaje 2
    sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 81, 128)
    sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 81, 128)
    sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//12, 85, 128)
    sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//12, 85, 128)
    sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 75, 128)
    sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 75, 128)
    sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 78, 128)
    sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 78, 128)
    sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//5, 80, 128)
    sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//5, 80, 128)

mapa_avion_ajustado = pygame.transform.scale(EI.mapa_avion, (EI.ancho, EI.alto)) #Ajustamos el mapa al tamaño de la pantalla
EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Mostramos el mapa

#Variables para calcular la hitbox del personaje
altura = EI.alto * 0.3
velocidad_personaje = EI.ancho * 0.6
estado_caminar_derecha = None
estado_caminar_izquierda = None
estado_correr_derecha = None
estado_correr_izquierda = None
saltando = None
anterior = None
ataque1 = None
ataque3 = None
posx_hitbox_derecha = EI.ancho * 0.63
posy_hitbox_derecha = EI.alto * 0.31
posx_hitbox_izquierda = EI.ancho * 0.64
hitbox = pygame.Rect(EI.ancho * 0.63, EI.alto * 0.31, EI.ancho * 0.017, EI.alto * 0.08)

#Variables para calcular las hitboxes de los niveles
hitbox_nivel_variables = pygame.Rect(EI.ancho * 0.74, EI.alto * 0.3, EI.ancho * 0.08, EI.alto * 0.1)
hitbox_nivel_condicionales = pygame.Rect(EI.ancho * 0.77, EI.alto * 0.12, EI.ancho * 0.07, EI.alto * 0.13)
hitbox_nivel_ciclos = pygame.Rect(EI.ancho * 0.205, EI.alto * 0.3, EI.ancho * 0.07, EI.alto * 0.12)
hitbox_nivel_funciones = pygame.Rect(EI.ancho * 0.22, EI.alto * 0.12, EI.ancho * 0.09, EI.alto * 0.1)
hitbox_examen_final = pygame.Rect(EI.ancho * 0.07, 0, EI.ancho * 0.07, EI.alto * 0.08)


#Variables para mostrar el texto
fuente_niveles = pygame.font.Font("Fuentes/Nicolast.otf", int(EI.ancho * 0.03))
texto_variables = fuente_niveles.render("Aldea de las variables", True, (EI.ROJO)) 
texto_condicionales = fuente_niveles.render("Cueva de condicionales", True, (EI.ROJO)) 
texto_ciclos = fuente_niveles.render("Bosque de ciclos", True, (EI.ROJO)) 
texto_funciones = fuente_niveles.render("Selva de funciones", True, (EI.ROJO)) 
texto_examen_final = fuente_niveles.render("Examen final", True, (EI.ROJO)) 
boton_niveles = EI.Boton(EI.ancho * 0.30, EI.alto * 0.5, EI.ancho * 0.15, EI.alto * 0.08, "Comenzar", int(EI.ancho * 0.04), int(EI.ancho * 0.01))
estrella_rellena_transformada = pygame.transform.scale(EI.estrella_rellena, (EI.ancho * 0.15, EI.alto * 0.2))
estrella_vacia_transformada = pygame.transform.scale(EI.estrella_vacia, (EI.ancho * 0.15, EI.alto * 0.2))

#Variables para implementar los niveles
variables = False
condicionales = False
ciclos = False
funciones = False
examen_final = False
mapa = True
var = True
con = True
cic = True
fun = True

while True: 
    #Examen final
    if examen_final:
        fuente_codigo = pygame.font.Font("Fuentes/FiraCode.otf", int(EI.ancho * 0.02)) 
        tamaño_fuente = int(EI.ancho * 0.02)
        lines = [[""]]
        cursor_pos= [[0, 0]]
        current_screen = 0
        num_screens = 3  # Número de pantallas
        for _ in range(num_screens - 1):
            lines.append([""])
        for _ in range(num_screens - 1):
            cursor_pos.append([0, 0])

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
                t1 = "Necesitas desplazarte hasta la salida para ser rescatado."
                t2 = "La isla está representada como una cuadrícula de 100 x 100."
                t3 = "Cada celda tiene coordenadas (x, y) que van desde (1, 1) hasta (100, 100)."
                EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
            elif num_dialog == 3:
                EI.PANTALLA.blit(fondo_guerra, (0, 0))
                EI.PANTALLA.blit(muerte, muerte_rect)
                t1 = "La salida está ubicada en una celda aleatoria de esta cuadrícula."
                t2 = "Tu objetivo será crear la función 'escape_island'."
                t3 = "Esta función debe recibir cuatro argumentos: 'x', 'y', 'salida_x', 'salida_y'. (En ese orden)."
                EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
            elif num_dialog == 4:
                EI.PANTALLA.blit(fondo_guerra, (0, 0))
                EI.PANTALLA.blit(muerte, muerte_rect)
                t1 = "La posición 'x' de la salida está representada por la variable 'salida_x'."
                t2 = "La posición 'y' de la salida está representada por la variable 'salida_y'."
                t3 = "Tú te encuentras en la posición (x, y) de la isla."
                EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
            elif num_dialog == 5:
                EI.PANTALLA.blit(fondo_guerra, (0, 0))
                EI.PANTALLA.blit(muerte, muerte_rect)
                t1 = "Para escapar de la isla, debes moverte paso a paso hacia la salida."
                t2 = "Solo puedes hacer movimientos horizontales y verticales."
                t3 = "Solo puedes hacer un movimiento por cada paso."
                EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
            elif num_dialog == 6:
                EI.PANTALLA.blit(fondo_guerra, (0, 0))
                EI.PANTALLA.blit(muerte, muerte_rect)
                t1 = "La función debe retornar la menor cantidad de pasos necesarios para llegar hasta la salida."
                t2 = "Por ejemplo, si la entrada es (5, 4, 1, 1). La función debe retornar: 7"
                t3 = "Por ejemplo, si la entrada es (100, 100, 100, 100). La función debe retornar: 0"
                EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
            elif num_dialog == 7:
                EI.PANTALLA.blit(fondo_guerra, (0, 0))
                EI.PANTALLA.blit(muerte, muerte_rect)
                t1 = "Por ejemplo, si la entrada es (2, 10, 2, 1). La función debe retornar: 9"
                t2 = "Ten cuidado con el nombre de la función."
                t3 = "Si lo logras, serás libre."
                EI.mostrar_texto("Muerte",t1,t2,t3,color=EI.MORADO)
            elif num_dialog == 9:
                examen_final = False
                EI.PANTALLA.blit(fondo_final, (0, 0))
                t1 = "¡Felicidades, has logrado escapar de la isla!"
                t2 = "Has demostrado gran ingenio en cada desafío."
                t3 = "¡Ahora eres libre!"
                EI.mostrar_texto("Escape Island",t1,t2,t3,color=EI.ROJO)
            for event in pygame.event.get():
                pygame.quit()
                sys.exit()
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                        romper = False
                        #Si se presiona la tecla "Esc", entonces aparece un cuadro de dialogo para confirmar la salida
                        while True:
                            if romper == True:
                                break
                            EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
                            EI.PANTALLA.blit(texto_salida, (EI.ancho * 0.3, EI.alto * 0.4))
                            boton_salida.dibujar(EI.PANTALLA)
                            boton_salida2.dibujar(EI.PANTALLA)
                            for evento in pygame.event.get():
                                if evento.type == pygame.MOUSEMOTION:
                                    #Si el cursor del mouse pasa por encima de algún botón, entonces su color cambia
                                    boton_salida.color_normal = EI.AZUL if not boton_salida.esta_encima(evento.pos) else EI.ROJO
                                    boton_salida2.color_normal = EI.AZUL if not boton_salida2.esta_encima(evento.pos) else EI.ROJO
                                if evento.type == pygame.MOUSEBUTTONDOWN:
                                    #Si se presiona 'Regresar', entonces se rompe el ciclo
                                    if boton_salida2.esta_encima(evento.pos):
                                        romper = True
                                        break
                                    #Si se presiona 'Guardar y salir', entonces se guarda el progreso y se termina el programa
                                    if boton_salida.esta_encima(evento.pos):
                                        EI.guardar_informacion({"completar_variables": completar_variables,"completar_condicionales": completar_condicionales,"completar_ciclos": completar_ciclos,"completar_funciones": completar_funciones, "completar_examen_final": completar_examen_final})
                                        pygame.quit()
                                        sys.exit()
                                pygame.display.update()
                if event.type == pygame.KEYDOWN:
                    #Si se presiona 'F1', 'F2' o 'F3' se cambia de pantalla
                    if event.key == pygame.K_F1:
                        current_screen = 0
                    elif event.key == pygame.K_F2:
                        current_screen = 1
                    elif event.key == pygame.K_F3:
                        current_screen = 2
                    #Si se presiona la flecha izquierda o derecha, se avanza en los diálogos
                    if event.key == pygame.K_RIGHT and dialog_continue:
                        #Avanzar el diálogo
                        num_dialog += 1
                    elif num_dialog >= 0 and event.key == pygame.K_LEFT and dialog_continue:
                        #Retroceder el diálogo
                        num_dialog -= 1
                    elif num_dialog == 8: 
                        dialog_continue = False
                        examen_final = True
                        t1 = "Desafío final: Crea la función 'escape_island' (x, y, salida_x, salida_y)."
                        t2 = "Debes retornar la menor cantidad de pasos para llegar a la salida."
                        t3 = "Presiona 'Ctrl' para ejecutar tu código. Utiliza 'F1', 'F2' y 'F3' si necesitas escribir más código."
                        EI.keydown(cursor_pos[current_screen], lines[current_screen], lines, event)
                        EI.mostrar_texto(t1,t2,t3,EI.t,color=EI.ROJO)
            if num_dialog == 8:  
                t1 = "Desafío final: Crea la función 'escape_island' (x, y, salida_x, salida_y)."
                t2 = "Debes retornar la menor cantidad de pasos para llegar a la salida."
                t3 = "Presiona 'Ctrl' para ejecutar tu código. Utiliza 'F1', 'F2' y 'F3' si necesitas escribir más código."
                dialog_continue = False
                examen_final = True  
                EI.render_text(cursor_pos[current_screen], lines[current_screen], fuente_codigo, tamaño_fuente)
                EI.mostrar_texto(t1, t2, t3,EI.t,color=EI.ROJO)
                if EI.correcto:  
                    pygame.time.wait(1000)
                    completar_examen_final = True
                    num_dialog = 9
            pygame.display.flip()
    #Nivel de ciclos
    if ciclos:
        if seleccion == 1:
            #Extraemos los sprites individuales del personaje 1 con las dimensiones ajustadas
            sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//10, 87, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//10, 87, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//4, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//4, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
        elif seleccion == 2:
            #Extraemos los sprites individuales del personaje 2 con las dimensiones ajustadas
            sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//12, 85, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//12, 85, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 75, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 75, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//5, 80, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//5, 80, 128, EI.ancho * 0.2, EI.alto * 0.22)
        #Booleanos
        running = True
        dialog_continue = True

        
        num_dialog = -1

        #personajes
        cicloso = pygame.transform.scale(EI.cicloso,(EI.ancho*0.2,EI.alto*0.3))
        cicloso_rect = cicloso.get_rect()
        cicloso_rect.bottomleft = (EI.ancho*0.01,EI.alto*0.7)

        #Fondos

        fondo_bosque = pygame.transform.scale(EI.fondo_bosque,(EI.ancho*0.8,EI.alto*0.7))
        fondo_bosque_rect = fondo_bosque.get_rect()
        fondo_bosque_rect.midtop = (EI.ancho//2, 0)

        #Cajas
        caja_a = pygame.transform.scale(EI.caja_a,(EI.ancho * 0.1,EI.alto * 0.15))
        caja_a_rect = caja_a.get_rect()
        caja_a_rect.bottomleft=(EI.ancho * 0.25, EI.alto * 0.69)
        caja_b = pygame.transform.scale(EI.caja_b,(EI.ancho * 0.1,EI.alto * 0.15))
        caja_b_rect = caja_b.get_rect()
        caja_b_rect.bottomleft=(EI.ancho * 0.4, EI.alto * 0.69)
        caja_c = pygame.transform.scale(EI.caja_c,(EI.ancho * 0.1,EI.alto * 0.15))
        caja_c_rect = caja_c.get_rect()
        caja_c_rect.bottomleft=(EI.ancho * 0.55, EI.alto * 0.69)
        caja_d = pygame.transform.scale(EI.caja_d,(EI.ancho * 0.1,EI.alto * 0.15))
        caja_d_rect = caja_d.get_rect()
        caja_d_rect.bottomleft=(EI.ancho * 0.7, EI.alto * 0.69)
        quieto_derecha = pygame.transform.scale(quieto_derecha, (EI.ancho * 0.05, EI.alto * 0.22)) #Se adecua el sprite a un tamaño específico
        quieto_izquierda = pygame.transform.scale(quieto_izquierda, (EI.ancho * 0.05, EI.alto * 0.22)) #Se adecua el sprite a un tamaño específico
        caja_a_rota_transformada = pygame.transform.scale(EI.caja_a_rota, (EI.ancho * 0.1, EI.alto * 0.15))
        caja_b_rota_transformada = pygame.transform.scale(EI.caja_b_rota, (EI.ancho * 0.1, EI.alto * 0.15))
        caja_c_rota_transformada = pygame.transform.scale(EI.caja_c_rota, (EI.ancho * 0.1, EI.alto * 0.15))
        caja_d_rota_transformada = pygame.transform.scale(EI.caja_d_rota, (EI.ancho * 0.1, EI.alto * 0.15))

        #Variables apra las preguntas
        num_dialog = -1

        #Variables para las respuestas
        caja_a_presionada = False
        caja_b_presionada = False
        caja_c_presionada = False
        caja_d_presionada = False
        prueba = True
        error = False

        #Variables para calcular la hitbox del personaje
        altura = EI.alto * 0.5
        altura_variables = EI.alto * 0.5
        velocidad_personaje_variables = EI.ancho * 0.8
        velocidad_personaje = EI.ancho * 0.8
        estado_caminar_derecha = None
        estado_caminar_izquierda = None
        estado_correr_derecha = None
        estado_correr_izquierda = None
        saltando = None
        anterior = 'derecha'
        ataque1 = None
        ataque3 = None
        posx_hitbox_derecha_variables = EI.ancho * 0.83
        posy_hitbox_derecha_variables = EI.alto * 0.5
        posx_hitbox_izquierda_variables = EI.ancho * 0.84
        posx_hitbox_derecha = EI.ancho * 0.63
        posy_hitbox_derecha = EI.alto * 0.31
        posx_hitbox_izquierda = EI.ancho * 0.64
        hitbox = pygame.Rect(EI.ancho * 0.63, EI.alto * 0.31, EI.ancho * 0.017, EI.alto * 0.08)
        mapa = False
        hitbox_variables = pygame.Rect(posx_hitbox_derecha_variables, posy_hitbox_derecha_variables, EI.ancho * 0.05, EI.alto * 0.25)
        rectangulo_caja_a = pygame.Rect(EI.ancho * 0.25, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)
        rectangulo_caja_b = pygame.Rect(EI.ancho * 0.4, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)
        rectangulo_caja_c = pygame.Rect(EI.ancho * 0.55, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)
        rectangulo_caja_d = pygame.Rect(EI.ancho * 0.7, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)

        #While principal
        while running:
            teclas = pygame.key.get_pressed()
            if anterior == "derecha":
                hitbox_variables = pygame.Rect(posx_hitbox_derecha_variables, posy_hitbox_derecha_variables, EI.ancho * 0.05, EI.alto * 0.3)
            elif anterior == "izquierda":
                hitbox_variables = pygame.Rect(posx_hitbox_derecha_variables, posy_hitbox_derecha_variables, EI.ancho * 0.05, EI.alto * 0.3)
            #Fondo
            EI.PANTALLA.fill((0,0,0))
            EI.PANTALLA.blit(fondo_bosque,fondo_bosque_rect)
            #Condicionales al romper las cajas

            #Caja a correcta
            if not caja_a_presionada and (caja_d_presionada or caja_b_presionada or caja_c_presionada) and prueba and num_dialog == 11:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -100
                    break

            if caja_a_presionada and (not (caja_d_presionada or caja_b_presionada or caja_c_presionada)) and prueba and num_dialog == 11:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 

            if not caja_a_presionada and (caja_d_presionada or caja_b_presionada or caja_c_presionada) and prueba and num_dialog == 41:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -300
                    break

            if caja_a_presionada and (not (caja_d_presionada or caja_b_presionada or caja_c_presionada)) and prueba and num_dialog == 41:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 

            #Caja b correcta

            if not caja_b_presionada and (caja_d_presionada or caja_a_presionada or caja_c_presionada) and prueba and (num_dialog == 39 or num_dialog == 43):
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -300
                    break

            if caja_b_presionada and (not (caja_d_presionada or caja_a_presionada or caja_c_presionada)) and prueba and (num_dialog == 39 or num_dialog == 43):
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 

            #Caja c correcta
            if not caja_c_presionada and (caja_a_presionada or caja_b_presionada or caja_d_presionada) and prueba and num_dialog == 40:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -300
                    break

            if caja_c_presionada and (not (caja_a_presionada or caja_b_presionada or caja_d_presionada)) and prueba and num_dialog == 40:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 

            #Caja d correcta
            if not caja_d_presionada and (caja_b_presionada or caja_a_presionada or caja_c_presionada) and prueba and num_dialog == 37:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -200
                    break

            if caja_d_presionada and (not (caja_b_presionada or caja_a_presionada or caja_c_presionada)) and prueba and num_dialog == 37:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 

            if not caja_d_presionada and (caja_a_presionada or caja_b_presionada or caja_c_presionada) and prueba and num_dialog == 42:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -300
                    break

            if caja_d_presionada and (not (caja_a_presionada or caja_b_presionada or caja_c_presionada)) and prueba and num_dialog == 42:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(cicloso,cicloso_rect)
                    EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 

            #Diálogos
            if num_dialog == -1:
                EI.mostrar_texto("Escape Island","Llegando al Bosque de ciclos.",color=EI.ROJO)
            elif num_dialog == 0:
                t1 = "Haz llegado a un bosque pegajoso."
                t2 = "Te motivas a seguir."
                EI.mostrar_texto("Bosque de ciclos",t1,t2,color=EI.MORADO)
            elif num_dialog == 1:
                t1 = "Al caminar durante un rato notas que el paisaje se empieza a repetir."
                t2 = "Crees que estas caminando en círculos."
                EI.mostrar_texto("Bosque de ciclos",t1,t2,color=EI.MORADO)
            elif num_dialog == 2:
                t1 = "¡Oye!"
                t2 = "¡Deja de caminar!"
                t3 = "Así no vas a llegar a ningún lado."
                EI.mostrar_texto("???",t1,t2)
            elif num_dialog == 3:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                t1 = "¡Hola!"
                t2 = "Yo soy el cicloso."
                t3 = "Habito estas tierras desde su nacimiento."
                EI.mostrar_texto("Cicloso",t1,t2,t3)
            elif num_dialog == 4:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                t1 = "Te puedo sacar de este ciclo infinito."
                t2 = "Pero para ello, debes dominar el uso de los ciclos."
                t3 = "¿Estás listo para aprender sobre ellos?"
                EI.mostrar_texto("Cicloso",t1,t2,t3)
            elif num_dialog == 5:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                t1 = "Bien. ¡Empecemos!"
                t2 = ""
                t3 = ""
                EI.mostrar_texto("Cicloso",t1,t2,t3)
            elif num_dialog == 6:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                t1 = "Imáginate que quieres sumar dos números,"
                t2 = "entonces escribes un código que hace eso."
                t3 = ""
                EI.mostrar_texto("Cicloso",t1,t2,t3)
            elif num_dialog == 7:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                t1 = "Pero ahora imáginate que necesitas sumar números varias veces."
                t2 = "No te vas a poner a escribir el mismo código esa cantidad de veces, ¿o sí?"
                t3 = ""
                EI.mostrar_texto("Cicloso",t1,t2,t3)
            elif num_dialog == 8:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                t1 = "No."
                t2 = "Por esa misma razón se usa una herramienta muy poderosa en programacion:"
                t3 = "Los ciclos."
                EI.mostrar_texto("Cicloso",t1,t2,t3)
            elif num_dialog == 9:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                t1 = "Estos ciclos te permiten repetir una cantidad de veces cierta parte de tu código."
                t2 = "Así, si tienes que hacer una operación múltiples veces, lo puedes hacer sin necesidad"
                t3 = "de escribir el código cientos de veces."
                EI.mostrar_texto("Cicloso",t1,t2,t3)
            elif num_dialog == 10:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                t1 = "Eso es básicamente lo que hacen los ciclos, su concepto más básico."
                t2 = "Bueno, creo que ahora es necesario ver si entendiste."
                t3 = "Este concepto es fundamental para poder continuar."
                EI.mostrar_texto("Cicloso",t1,t2,t3)
            elif num_dialog == 11:
                #Quiz de ciclos 1
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                t1 = "¿Para qué sirven los ciclos en programación?"
                a = "Para repetir un código una cierta cantidad de veces."
                b = "Para caminar en círculos."
                c = "Para guardar información."
                d = "Para ejecutar un código cuando se cumpla cierta condición."
                correcta = 2
                EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Quiz de ciclos 1
                        EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Quiz de ciclos 1
                        EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso, cicloso_rect)
                        EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Quiz de ciclos 1
                        EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Quiz de ciclos 1
                        EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

            elif num_dialog == -100: #Si se equivoca
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Eso está mal."
                t2 = "Vamos a tener que repetirlo."
                t3 = "Presiona 'Espacio' para continuar."
                EI.mostrar_texto(personaje,t1,t2,t3)
                error = True
                devolver = 6
            elif num_dialog == 12: #Si responde correctamente
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Perfecto."
                t2 = "¡Continuemos!"
                t3 = ""
                EI.mostrar_texto(personaje,t1,t2,t3)
                dialog_continue = True
            elif num_dialog == 13:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Ahora pasaremos a su ejecución en Python."
                t2 = "Así podrás aplicarlos."
                t3 = "¿Te parece?"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 14:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Listo."
                t2 = ""
                t3 = ""
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 15:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Hay dos tipos de ciclos muy importantes que vas a encontrar en todo lado."
                t2 = "Estos son el 'for' y el 'while'."
                t3 = "¿Cuál es su diferencia?"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 16: 
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "El 'for' se usa cuando necesitas que se repita el código una cantidad de veces específica,"
                t2 = "mientras que el 'while' se ejecuta hasta que una condición que le des no se cumpla."
                t3 = "Si sabes usar condiciones, podrás usar los 'while'."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 17:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Ahora, ¿cómo se programan en Python?"
                t2 = "Empecemos por el 'for'."
                t3 = ""
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 18:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "La sintaxis de un 'for' puede ser:"
                t2 = "'for elemento in elementos:'"
                t3 = "o también: 'for numero in range(rango):'"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 19:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "La palabra posterior a for es una variable arbitraria que va recorrer (iterar)"
                t2 = "a través de un string, una lista o cualquier otro arreglo que contenga elementos."
                t3 = "Por ejemplo, el 'for' puede recorrer los caracteres de una palabra."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 20:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Un ejemplo de esto sería:"
                t2 = "'for vocal in \"aeiou\":'"
                t3 = "'    {código}'"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 21:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "En este caso, el código se repite según la cantidad de vocales que hay en \"aeiou\"."
                t2 = "Cada vez que el código se repite, la variable 'vocal' almacena la vocal."
                t3 = "Recuerda que el código debe estar indentado."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 22:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Por otro lado, la segunda sintaxis repite el código la cantidad de veces específicada en el"
                t2 = "rango del ciclo. Este rango tiene que ser un número entero."
                t3 = ""
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 23:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Por ejemplo:"
                t2 = "'for i in range(5):' repetiría el código 5 veces, y guardaría el número"
                t3 = "del ciclo en la variable 'i', empezando por 0 y terminando en 4 (en este caso)."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 24:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Es importante notar es que si tienes una variable que contenga un número entero,"
                t2 = "puedes usar esa variable como rango para el 'for'."
                t3 = "Algo como: 'for numero in range(numeros)'."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 25:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "En este caso, el código se repetiría según el valor de 'números',"
                t2 = "y en cada repetición (también llamada iteración o ciclo) se guardaría en la variable 'número'."
                t3 = "El rango va desde 0 hasta el valor de 'números' menos 1."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 26:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Así es como funciona el 'for'."
                t2 = "Vamos por buen camino."
                t3 = "Recuerda que puedes regresar en mi explicación si se te complica algo."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 27:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Ahora pasemos con el 'while'."
                t2 = "Si has llegado hasta aquí asumiré que ya sabes sobre las condiciones."
                t3 = "Es importante que lo recuerdes."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 28:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Bien, si estás listo pasaré a mostrarte la estructura de un 'while'."
                t2 = "¿Preparado?"
                t3 = ""
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 29:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "'While {condición}:'"
                t2 = "'    {código}'"
                t3 = "Se ve más sencillo que el for, ¿no?"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 30:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Básicamente, todo lo que este dentro de ese while se va ejecutar mientras se cumpla esa condición."
                t2 = "Para que lo entiendas mejor, debes saber que lo que hace es que cada vez que inicia un nuevo ciclo"
                t3 = "verifica si se cumple esa condición, y si lo hace se sigue ejecutando."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 31:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Si lo entiendes, verás que es muy fácil que acabes en un ciclo infinito, por lo que ten cuidado."
                t2 = "Debes hacer que esa condición se deje de cumplir en algún momento si no"
                t3 = "quieres que el ciclo se ejecute para siempre."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 32:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "¿Necesitas un ejemplo?"
                t2 = "Dejame pensar..."
                t3 = "Bueno, aquí va:"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 33:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "numero = 1"
                t2 = "while numero < 10:"
                t3 = "    numero = numero + 1"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 34:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Este código empieza con el número 1 y verifica si es menor que 10,"
                t2 = "como eso es verdad, entonces le suma 1 al número y queda en 2. Luego vuelve a verificar y vuelve a sumar."
                t3 = "Eso ocurre hasta que el número queda en 10."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 35:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Como 10 no es menor que 10 entonces no le vuelve a sumar nada y el número se queda en 10."
                t2 = "Así puedes usar los ciclos, pero no es la única manera de hacerlo."
                t3 = "Tienes que ser creativo."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 36:
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Creo que eso es todo por ahora."
                t2 = "Con esto creo que serías capaz de salir de aquí."
                t3 = "Voy a ver si me pusiste atención."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 37:
                #Quiz de ciclos 2
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                t1 = "¿Cuáles son los dos tipos de ciclos que se pueden usar en Python?"
                a = "'if' y 'for'"
                b = "'range' y 'for'"
                c = "'if y 'while'"
                d = "'while' y 'for'"
                EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                correcta = 4
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Quiz de ciclos 2
                        EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Quiz de ciclos 2
                        EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso, cicloso_rect)
                        EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Quiz de ciclos 2
                        EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Quiz de ciclos 2
                        EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

            elif num_dialog == -200: # Si se equivoca
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Eso está mal."
                t2 = "Vamos a tener que repetirlo."
                t3 = "Presiona 'Espacio' para continuar."
                EI.mostrar_texto(personaje,t1,t2,t3)
                error = True
                devolver = 15
            elif num_dialog == 38: # Si responde correctamente
                EI.PANTALLA.blit(cicloso,cicloso_rect)
                personaje = "Cicloso"
                t1 = "Vale. Con este conocimiento podrás salir de este bosque."
                t2 = "Recuerda dar lo mejor de ti."
                t3 = "¡Nos vemos!"
                EI.mostrar_texto(personaje,t1,t2,t3)
                dialog_continue = True
            elif num_dialog == 39:
                #Examen de ciclos
                #Pregunta 1
                t1 = "¿Cuál de las siguientes tiene una estructura válida de un 'for' en Python?:"
                a = "for 'condición':"
                b = "for letra in 'palabra':"
                c = "for letra = 'palabra':"
                d = "for = 'condición'"
                correcta = 2
                EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso, cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == 40:
                #Pregunta 2
                t1 = "¿Cuál de las siguientes NO tiene una estructura válida de un 'while' en Python?"
                a = "while True:"
                b = "while a > b:"
                c = "while a = b:"
                d = "while a > b and b > c:"
                correcta = 3
                EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso, cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == 41:
                #Pregunta 3
                t1 = "¿Cuántas veces se repite el siguiente 'for'?:"
                t2 = "for i in range(10):"
                a = "10"
                b = "9"
                c = "11"
                d = "i"
                correcta = 1
                EI.pregunta("Examen de ciclos",[t1,t2,""],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso, cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == 42:
                #Pregunta 4
                t1 = "¿Cuántas veces se repite el siguiente 'while', si a = 0?:"
                t2 = "while a >= 10:"
                t3 = "    a = a + 1"
                a = "10"
                b = "9"
                c = "11"
                d = "0"
                correcta = 4
                EI.pregunta("Examen de ciclos",[t1,t2,t3],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso, cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == 43:
                #Pregunta 5
                t1 = "¿Cuántas veces se repite el siguiente 'while'?:"
                t2 = "while (True and ((not False and True) or True)):"
                a = "Ninguna"
                b = "Infinitas"
                c = "1"
                d = "1000"
                correcta = 2
                EI.pregunta("Examen de ciclos",[t1,t2,""],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso, cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de ciclos
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_bosque, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(cicloso,cicloso_rect)
                        EI.pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == -300: # Si no pasa
                t1 = "Continuas dando vueltas en círculos..."
                t2 = "Devuélvete y cumple la condición para salir de este bucle."
                t3 = "Presiona 'Espacio' para continuar."
                EI.mostrar_texto("Bosque de ciclos",t1,t2,t3,color=EI.MORADO)
                error = True
                devolver = 15
            elif num_dialog == 44: # Si pasa
                t1 = "Una salida se abre ante ti."
                t2 = "Avanzas hacia ella."
                t3 = ""
                EI.mostrar_texto("Bosque de ciclos",t1,t2,t3,color=EI.MORADO)
                dialog_continue = True
            elif num_dialog == 45: 
                t1 = "Has salido del bosque."
                t2 = "Te sientes aliviado de haber salido de ese ciclo infinito."
                t3 = "Ya falta poco."
                EI.mostrar_texto("Bosque de ciclos",t1,t2,t3,color=EI.MORADO)
            elif num_dialog == 46: 
                EI.mostrar_texto("Escape Island","Saliendo del Bosque de ciclos.",color=EI.ROJO)
                mapa = True
                ciclos = False
                cic = True
                completar_ciclos = True
                break
            else:
                EI.mostrar_texto("","")
            
            #Eventos    
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                        romper = False
                        #Si se presiona la tecla "Esc", entonces aparece un cuadro de dialogo para confirmar la salida
                        while True:
                            if romper == True:
                                break
                            EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
                            EI.PANTALLA.blit(texto_salida, (EI.ancho * 0.3, EI.alto * 0.4))
                            boton_salida.dibujar(EI.PANTALLA)
                            boton_salida2.dibujar(EI.PANTALLA)
                            for evento in pygame.event.get():
                                if evento.type == pygame.MOUSEMOTION:
                                    #Si el cursor del mouse pasa por encima de algún botón, entonces su color cambia
                                    boton_salida.color_normal = EI.AZUL if not boton_salida.esta_encima(evento.pos) else EI.ROJO
                                    boton_salida2.color_normal = EI.AZUL if not boton_salida2.esta_encima(evento.pos) else EI.ROJO
                                if evento.type == pygame.MOUSEBUTTONDOWN:
                                    #Si se presiona 'Regresar', entonces se rompe el ciclo
                                    if boton_salida2.esta_encima(evento.pos):
                                        romper = True
                                        break
                                    #Si se presiona 'Guardar y salir', entonces se guarda el progreso y se termina el programa
                                    if boton_salida.esta_encima(evento.pos):
                                        EI.guardar_informacion({"completar_variables": completar_variables,"completar_condicionales": completar_condicionales,"completar_ciclos": completar_ciclos,"completar_funciones": completar_funciones, "completar_examen_final": completar_examen_final})
                                        pygame.quit()
                                        sys.exit()
                                pygame.display.update()
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_RIGHT and dialog_continue:
                        #Avanzar el diálogo
                        num_dialog += 1
                    elif num_dialog >= 0 and evento.key == pygame.K_LEFT and dialog_continue:
                        #Retroceder el diálogo
                        num_dialog -= 1
                    #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1
                    if evento.key == pygame.K_x:
                        ataque1 = True
                    #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3
                    if evento.key == pygame.K_z:
                        ataque3 = True
                    if error and evento.key == pygame.K_SPACE:
                        num_dialog = devolver
                        dialog_continue = True
                        error = False
            
            pygame.display.update()

    #Nivel de condicionales
    if condicionales:
        if seleccion == 1:
            #Extraemos los sprites individuales del personaje 1 con las dimensiones ajustadas
            sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//10, 87, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//10, 87, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//4, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//4, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
        elif seleccion == 2:
            #Extraemos los sprites individuales del personaje 2 con las dimensiones ajustadas
            sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//12, 85, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//12, 85, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 75, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 75, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//5, 80, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//5, 80, 128, EI.ancho * 0.2, EI.alto * 0.22)

        
        quieto_derecha = pygame.transform.scale(quieto_derecha, (EI.ancho * 0.05, EI.alto * 0.22)) #Se adecua el sprite a un tamaño específico
        quieto_izquierda = pygame.transform.scale(quieto_izquierda, (EI.ancho * 0.05, EI.alto * 0.22)) #Se adecua el sprite a un tamaño específico
        caja_a_rota_transformada = pygame.transform.scale(EI.caja_a_rota, (EI.ancho * 0.1, EI.alto * 0.15))
        caja_b_rota_transformada = pygame.transform.scale(EI.caja_b_rota, (EI.ancho * 0.1, EI.alto * 0.15))
        caja_c_rota_transformada = pygame.transform.scale(EI.caja_c_rota, (EI.ancho * 0.1, EI.alto * 0.15))
        caja_d_rota_transformada = pygame.transform.scale(EI.caja_d_rota, (EI.ancho * 0.1, EI.alto * 0.15))

        #Variables apra las preguntas
        num_dialog = -1

        #Variables para las respuestas
        caja_a_presionada = False
        caja_b_presionada = False
        caja_c_presionada = False
        caja_d_presionada = False
        prueba = True
        error = False

        #personajes
        condi = pygame.transform.scale(EI.condi,(EI.ancho*0.2,EI.alto*0.3))
        condi_rect = condi.get_rect()
        condi_rect.bottomleft = (EI.ancho*0.01,EI.alto*0.7)

        #Variables para calcular la hitbox del personaje
        altura = EI.alto * 0.5
        altura_variables = EI.alto * 0.5
        velocidad_personaje_variables = EI.ancho * 0.8
        velocidad_personaje = EI.ancho * 0.8
        estado_caminar_derecha = None
        estado_caminar_izquierda = None
        estado_correr_derecha = None
        estado_correr_izquierda = None
        saltando = None
        anterior = 'derecha'
        ataque1 = None
        ataque3 = None
        posx_hitbox_derecha_variables = EI.ancho * 0.83
        posy_hitbox_derecha_variables = EI.alto * 0.5
        posx_hitbox_izquierda_variables = EI.ancho * 0.84
        posx_hitbox_derecha = EI.ancho * 0.63
        posy_hitbox_derecha = EI.alto * 0.31
        posx_hitbox_izquierda = EI.ancho * 0.64
        hitbox = pygame.Rect(EI.ancho * 0.63, EI.alto * 0.31, EI.ancho * 0.017, EI.alto * 0.08)
        mapa = False
        hitbox_variables = pygame.Rect(posx_hitbox_derecha_variables, posy_hitbox_derecha_variables, EI.ancho * 0.05, EI.alto * 0.25)
        rectangulo_caja_a = pygame.Rect(EI.ancho * 0.25, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)
        rectangulo_caja_b = pygame.Rect(EI.ancho * 0.4, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)
        rectangulo_caja_c = pygame.Rect(EI.ancho * 0.55, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)
        rectangulo_caja_d = pygame.Rect(EI.ancho * 0.7, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)

        #Fondos
        fondo_cueva = pygame.transform.scale(EI.fondo_cueva,(EI.ancho*0.8,EI.alto*0.7))
        fondo_cueva_rect = fondo_cueva.get_rect()
        fondo_cueva_rect.midtop = (EI.ancho//2, 0)

        while True:
            if anterior == "derecha":
                hitbox_variables = pygame.Rect(posx_hitbox_derecha_variables, posy_hitbox_derecha_variables, EI.ancho * 0.05, EI.alto * 0.3)
            elif anterior == "izquierda":
                hitbox_variables = pygame.Rect(posx_hitbox_derecha_variables, posy_hitbox_derecha_variables, EI.ancho * 0.05, EI.alto * 0.3)
            
            teclas = pygame.key.get_pressed()

            #Fondo
            EI.PANTALLA.fill((0,0,0))
            EI.PANTALLA.blit(fondo_cueva,fondo_cueva_rect)
            
            #Condicionales al romper las cajas
            #Caja a correcta
            if not caja_a_presionada and (caja_d_presionada or caja_b_presionada or caja_c_presionada) and prueba and num_dialog == 23:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(condi,condi_rect)
                    EI.pregunta("Quiz de condicionales 1",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -100
                    break

            if caja_a_presionada and (not (caja_d_presionada or caja_b_presionada or caja_c_presionada)) and prueba and num_dialog == 23:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(condi,condi_rect)
                    EI.pregunta("Quiz de condicionales 1",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 

            #Caja d correcta
            if not caja_d_presionada and (caja_a_presionada or caja_b_presionada or caja_c_presionada) and prueba and num_dialog == 40:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(condi,condi_rect)
                    EI.pregunta("Quiz de condicionales 2",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -200
                    break

            if caja_d_presionada and (not (caja_a_presionada or caja_b_presionada or caja_c_presionada)) and prueba and num_dialog == 40:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(condi,condi_rect)
                    EI.pregunta("Quiz de condicionales 2",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 
            
            #Caja b correcta
            if not caja_b_presionada and (caja_a_presionada or caja_d_presionada or caja_c_presionada) and prueba and num_dialog == 43:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(condi,condi_rect)
                    EI.pregunta("Examen de condicionales",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -300
                    break

            if caja_b_presionada and (not (caja_a_presionada or caja_d_presionada or caja_c_presionada)) and prueba and num_dialog == 43:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(condi,condi_rect)
                    EI.pregunta("Examen de condicionales",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 

            #Caja a correcta
            if not caja_a_presionada and (caja_b_presionada or caja_d_presionada or caja_c_presionada) and prueba and (num_dialog == 44 or num_dialog == 45 or num_dialog == 47):
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(condi,condi_rect)
                    EI.pregunta("Examen de condicionales",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -300
                    break

            if caja_a_presionada and (not (caja_b_presionada or caja_d_presionada or caja_c_presionada)) and prueba and (num_dialog == 44 or num_dialog == 45 or num_dialog == 47):
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(condi,condi_rect)
                    EI.pregunta("Examen de condicionales",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 
            
            #Caja c correcta
            if not caja_c_presionada and (caja_b_presionada or caja_d_presionada or caja_a_presionada) and prueba and num_dialog == 46:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(condi,condi_rect)
                    EI.pregunta("Examen de condicionales",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -300
                    break

            if caja_c_presionada and (not (caja_b_presionada or caja_d_presionada or caja_a_presionada)) and prueba and num_dialog == 46:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(condi,condi_rect)
                    EI.pregunta("Examen de condicionales",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 

            #Diálogos
            if num_dialog == -1:
                EI.mostrar_texto("Escape Island","Llegando a la Cueva de condicionales.",color=EI.ROJO)
            elif num_dialog == 0:
                t1 = "Haz llegado a una cueva intrigante."
                t2 = "El aire misterioso te condiciona a seguir."
                EI.mostrar_texto("Cueva de condicionales",t1,t2,color=EI.MORADO)
            elif num_dialog == 1:
                EI.mostrar_texto("Cueva de condicionales","Te tropiezas.","Haces un alboroto.","Si alguien te escuchara, estarías en problemas.",color=EI.MORADO)
            elif num_dialog == 2:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "???"
                EI.mostrar_texto(personaje,"¿¿¿Hay alguien ahí???", "Si es así...","¡Muéstrate!")
            elif num_dialog == 3:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Ah, pero sí eres un joven aventurero."
                t2 = "¿Qué te trae por estos lares tan silenciosos?"
                t3 = "Soy Condi, viejo maestro de las condiciones."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 4:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "¿Qué?"
                t2 = "Así que vienes de la aldea de las variables, ¿eh?"
                t3 = "En busca de llenar tu mente de sabiduría."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 5:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Si has venido a aprender, entonces estás en el lugar correcto."
                t2 = "Si no estoy mal, ya deberías saber sobre las variables."
                t3 = "Así que te podría enseñar mi especialidad: las condiciones."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 6:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Si estás listo..."
                t2 = "¡Comencemos de una vez!"
                EI.mostrar_texto(personaje,t1,t2)
            elif num_dialog == 7:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Los condicionales son una de las herramientas más importantes en programación."
                t2 = "Te serán de mucha utilidad."
                EI.mostrar_texto(personaje,t1,t2)
            elif num_dialog == 8:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Para ponerte en contexto, te voy a mostrar la estructura de un condicional:"
                t2 = "Si se cumple (condición) entonces:"
                t3 = "    se ejecuta (código)"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 9:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Básicamente, esto significa que si se cumple la condición que tú le pongas:"
                t2 = "Se ejecuta todo lo que tengas dentro de ese condicional."
                EI.mostrar_texto(personaje,t1,t2)
            elif num_dialog == 9:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Ahora te pregutarás"
                t2 = "¿Qué tipo de condiciones puedes poner?"
                t3 = "Bueno, es algo bastante sencillo."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 10:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Puedes comparar dos valores distintos."
                t2 = "Por ejemplo, puedes comparar 2 > 9 (2 es mayor que 9)."
                t3 = "Eso sería falso, por lo que no se ejecutaría la condición."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 11:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "También podemos poner:"
                t2 = "a = 10"
                t3 = "Y evaluar la condición a >= 10 (La variable a es mayor o igual a 10)."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 12:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Esto sería verdadero, ya que como a es 10 y 10 >= 10, entonces se cumple la condición."
                t2 = "Y todo lo que tengas dentro del condicional se ejecutaría."
                t3 = "No se te olvide que puedes comparar variables (lo que suele ser muy usado)."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 13:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Digamos que tienes dos variables a = 10 y b = 20"
                t2 = "a == b (a es igual a b) sería falso, porque 10 == 20 (10 es igual a 20) es falso."
                t3 = "Y así puedes comparar variables."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 14:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Pero no solo puedes comparar números."
                t2 = "También puedes comparar cadenas de texto (strings)."
                t3 = "Por ejemplo..."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 15:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Si tienes nombre = 'Variably' y jefe = 'Variably'."
                t2 = "Decir jefe == nombre es verdadero, ya que las dos contienen el mismo texto ('Variably')."
                t3 = "En Python, se diferencian mayúsculas de minúsculas. Además, puedes tener condiciones con booleanos."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 16:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Los booleanos son valores de Falso o Verdadero que se pueden usar en una condición."
                t2 = "Si tienes la variable condicion = True"
                t3 = "Cuando evalúes la condición en un condicional, el código se va a ejecutar."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 17:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Lo mismo sucede con False."
                t2 = "Si tienes condición = False"
                t3 = "No se va a ejecutar el código."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 18:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Algo interesante es que puedes poner varias condiciones en un mismo condicional."
                t2 = "Esto se hace con los operadores lógicos 'y' (and) y 'o' (or)."
                t3 = "Si has trabajado con lógica antes se te va a hacer un poco más fácil, ya que funcionan igual."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 19:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Si tenemos una variable a = True y otra variable b = False"
                t2 = "Al usar el operador de 'and', las dos condiciones tienen que ser verdadares para que se cumpla."
                t3 = "Por ejemplo: 'a and b' es falso, porque b es falso (False)."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 20:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Al igual que con 'and' se puede usar 'or'."
                t2 = "La diferencia es que 'or' solo necesita que una de las dos condiciones sea verdadera para funcionar."
                t3 = "Siguiendo el ejemplo anterior, 'a or b' sería verdadero, dado que a es verdadero (True)."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 21:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Cabe destacar que la condición puede ser una comparación de valores."
                t2 = "Si tomamos a = 10, b = 20 y c = 30, y tenemos 'a > b or c > b'"
                t3 = "Sería verdadero porque c > b es verdadero, aunque a > b no lo sea."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 22:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Eso sería la teoría de cómo funciona un condicional."
                t2 = "Si necesitas puedes volver para revisar algo de lo que dije. Es bastante información."
                t3 = "Bueno, veamos qué tanto aprendiste."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 23: #Quiz de condicionales 1
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Si tenemos: a = 50, b = 20, c = 70"
                t2 = "Y la condición 'a > b and c >= a'"
                t3 = "¿La condición se cumple?"
                a = "Sí, todo se cumple"
                b = "No, nada se cumple"
                c = "No, solo se cumple a > b"
                d = "No, solo se cumple c >= a"
                EI.pregunta("Quiz de condicionales 1",[t1,t2,t3],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Quiz de condicionales 1
                        EI.pregunta("Quiz de condicionales 1",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Quiz de condicionales 1",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Quiz de condicionales 1
                        EI.pregunta("Quiz de condicionales 1",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Quiz de condicionales 1",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Quiz de condicionales 1
                        EI.pregunta("Quiz de condicionales 1",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Quiz de condicionales 1",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Quiz de condicionales 1
                        EI.pregunta("Quiz de condicionales 1",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Quiz de condicionales 1",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == -100: # Si falla
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Eso está mal. Volvamos a ver."
                t2 = "Recuerda que no hay prisa."
                t3 = "Presiona 'Espacio' para continuar."
                EI.mostrar_texto(personaje,t1,t2,t3)
                error = True
                devolver = 7
            elif num_dialog == 24: # Si responde bien
                EI.PANTALLA.blit(condi,condi_rect)
                dialog_continue = True
                personaje = "Condi"
                t1 = "Muy bien, joven. Ya lo estás entendiendo."
                t2 = "Sigamos con la siguiente lección."
                t3 = "Cómo aplicarlo."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 25:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Para aplicar los condicionales en Python se usa la siguiente estructura:"
                t2 = "if (condición):"
                t3 = "    (código)"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 26:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Bastante sencillo, ¿no?"
                t2 = "Es lo mismo que aprendimos sobre las condiciones."
                t3 = "Solo que el código que se ejecuta dentro del condicional tiene que estar indentado."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 27:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "¿Que qué es indentado?"
                t2 = "Mira lo sencillo que es."
                t3 = "Significa que al principio de la línea tienes que dejar unos espacios."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 28:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Para hacerlo puedes dejar 4 espacios o presionar la tecla TAB."
                t2 = "Esto con el objetivo de indicar cuáles instrucciones se deben ejecutar si la condición es verdadera."
                t3 = "También, permite mejorar la organización y legibilidad del código."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 29:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Por ejemplo, si tienes la variable edad y tipo_persona puedes hacer lo siguiente:"
                t2 = "if edad < 18:"
                t3 = "    tipo_persona = 'Menor de edad'"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 30:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Pero, ¿qué pasa si en el ejemplo anterior también queremos considerar a las personas mayores de edad?"
                t2 = "Tendríamos qué hacer otro condicional, ¿cierto?"
                t3 = "Pero también existe otra forma de hacerlo."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 31:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Existe dos estructuras que son 'elif' y 'else'"
                t2 = "Estás se evalúan si la primera condición no se cumplió."
                t3 = "¿Pero cuál es la diferencia entre ellas?"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 32:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Básicamente, con 'elif' puedes escribir una segunda condición de la siguiente manera:"
                t2 = "elif (segunda condición):"
                t3 = "    (segundo código)"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 33:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Y lo interesante de esto es que 'elif' lo puedes usar cuantas veces quieras."
                t2 = "Una tercera, cuarta, décima vez o las veces que quieras."
                EI.mostrar_texto(personaje,t1,t2)
            elif num_dialog == 34:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "En cambio 'else' lo que hace es que si ninguna condición de las anteriores (incluyendo 'elif's)"
                t2 = "se ejecuta, entonces ejecuta lo que tiene el 'else'."
                t3 = "Volviendo al ejemplo de la edad, podríamos decir:"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 35:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "if 0 <= edad < 18: tipo_persona = 'Menor de edad'"
                t2 = "elif edad > 18: tipo_persona = 'Mayor de edad'"
                t3 = "else: tipo_persona = 'Inexistente'"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 36:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "En la primera condición evaluamos si la edad es menor a 18 y mayor o igual a cero."
                t2 = "Esto se hace para averiguar las personas menores de edad y verficar que la edad no sea negativa."
                t3 = "Una edad negativa no sería posible."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 37:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Luego, con el 'elif' evaluamos a las personas que tienen más de 18."
                t2 = "A estas les asignamos la mayoría de edad."
                t3 = ""
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 38:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Por último, si nada se cumple, significaría que tiene edad negativa."
                t2 = "Lo cual no es posible."
                t3 = "Por esto se le asigna la categoría de 'Inexistente'."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 39:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Con este ejemplo creo que puedes dar un vistazo de todas las cosas que se pueden hacer con"
                t2 = "los condicionales."
                t3 = "¡Vayamos a la pregunta de la lección!"
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 40: # Quiz de condicionales 2
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "¿Para qué sirve indentar?"
                t2 = ""
                t3 = ""
                a = "Para indicar qué parte del código se debe ejecutar si se cumple la condición."
                b = "Para indicar que el código no se tiene que ejecutar."
                c = "Para tener una mejor organización en el código."
                d = "La a y la c."
                EI.pregunta("Quiz de condicionales 2",[t1,t2,t3],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Quiz de condicionales 2
                        EI.pregunta("Quiz de condicionales 2",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Quiz de condicionales 2",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Quiz de condicionales 2
                        EI.pregunta("Quiz de condicionales 2",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Quiz de condicionales 2",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Quiz de condicionales 2
                        EI.pregunta("Quiz de condicionales 2",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Quiz de condicionales 2",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Quiz de condicionales 2
                        EI.pregunta("Quiz de condicionales 2",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Quiz de condicionales 2",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == 41: # Si responde bien
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Excelente, joven."
                t2 = "Haz adquirido un gran conocimiento."
                t3 = "Veamos cómo te enfrentas a lo siguiente."
                EI.mostrar_texto(personaje,t1,t2,t3)
                dialog_continue = True
            elif num_dialog == 42: 
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Aquí comienza tu prueba final."
                t2 = ""
                t3 = ""
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 43:
                #Examen de condicionales
                #Pregunta 1
                t1 = "¿Para qué sirve un condicional?"
                t2 = ""
                t3 = ""
                a = "Para guardar una parte del código."
                b = "Para ejecutar un código cuando se cumpla una condición específica."
                c = "Para almacenar información sobre las variables."
                d = "Para únicamente comparar dos números o cadenas."
                EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == 44:
                #Pregunta 2
                t1 = "¿Cuál es la estructura de un condicional en Python?"
                t2 = ""
                t3 = ""
                a = "if (condición): (código)"
                b = "(código): if (condición)"
                c = "(condición): if (código)"
                d = "if (código): (condición)"
                EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == 45:
                #Pregunta 3
                t1 = "Si tenemos a = True, b = 10 y c = 5,"
                t2 = "¿la siguiente condición se cumple?"
                t3 = "'a and b > c'."
                a = "Sí, todo se cumple."
                b = "No, porque solo 'a' es falso."
                c = "No, porque solo no se cumple 'b > c'."
                d = "No, todo es falso."
                EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == 46:
                #Pregunta 4
                t1 = "Si tenemos a = False, b = True, c = 'manzana' y d = 'Manzana',"
                t2 = "¿la siguiente condición se cumple?"
                t3 = "'(a or b) and (c == d)'"
                a = "Sí, todo se cumple."
                b = "No, porque solo '(a or b)' no se cumple."
                c = "No, porque solo '(c == d)' no se cumple."
                d = "No, porque ni '(a or b)' ni '(c == d)' se cumplen."
                EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
            elif num_dialog == 47:
                t1 = "¿Qué se usa para ejecutar un código, cuando la primera condición es falsa?"
                t2 = ""
                t3 = ""
                a = "'else' y 'elif'."
                b = "'print' y 'else'."
                c = "'if' y 'else'."
                d = "'print' e 'if'."
                EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                prueba = True
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de condicionales
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_cueva, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(condi,condi_rect)
                        EI.pregunta("Examen de condicionales",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False
                
            elif num_dialog == -200: # Si falla
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Eso no está bien."
                t2 = "Veamos qué pasó."
                t3 = "Presiona 'Espacio' para continuar."
                EI.mostrar_texto(personaje,t1,t2,t3)
                error = True
                devolver = 25
                #Vuelve a num_dialog = 25
            elif num_dialog == -300: # Si falla
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Tú puedes."
                t2 = "Vuelve a intentarlo."
                t3 = "Presiona 'Espacio' para continuar."
                EI.mostrar_texto(personaje,t1,t2,t3)
                error = True
                devolver = 25
                #Vuelve a num_dialog = 25
            elif num_dialog == 48: #Si pasa
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "Increíble, joven."
                t2 = "¡Has superado todas mis expectativas!"
                t3 = "Sigue tu camino."
                EI.mostrar_texto(personaje,t1,t2,t3)
                dialog_continue = True
            elif num_dialog == 49:
                EI.PANTALLA.blit(condi,condi_rect)
                personaje = "Condi"
                t1 = "¡Un futuro grandioso te espera!"
                t2 = ""
                t3 = ""
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 50:
                t1 = "Saliendo de la cueva de condicionales."
                t2 = ""
                t3 = ""
                EI.mostrar_texto("Escape Island",t1,t2,t3, color=EI.ROJO)

            elif num_dialog == 51:
                mapa = True
                condicionales = False
                con = True
                completar_condicionales = True
                break
            else:
                EI.mostrar_texto("","")

            #Eventos    
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    romper = False
                    #Si se presiona la tecla "Esc", entonces aparece un cuadro de dialogo para confirmar la salida
                    while True:
                        if romper == True:
                            break
                        EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
                        EI.PANTALLA.blit(texto_salida, (EI.ancho * 0.3, EI.alto * 0.4))
                        boton_salida.dibujar(EI.PANTALLA)
                        boton_salida2.dibujar(EI.PANTALLA)
                        for evento in pygame.event.get():
                            if evento.type == pygame.MOUSEMOTION:
                                #Si el cursor del mouse pasa por encima de algún botón, entonces su color cambia
                                boton_salida.color_normal = EI.AZUL if not boton_salida.esta_encima(evento.pos) else EI.ROJO
                                boton_salida2.color_normal = EI.AZUL if not boton_salida2.esta_encima(evento.pos) else EI.ROJO
                            if evento.type == pygame.MOUSEBUTTONDOWN:
                                #Si se presiona 'Regresar', entonces se rompe el ciclo
                                if boton_salida2.esta_encima(evento.pos):
                                    romper = True
                                    break
                                #Si se presiona 'Guardar y salir', entonces se guarda el progreso y se termina el programa
                                if boton_salida.esta_encima(evento.pos):
                                    EI.guardar_informacion({"completar_variables": completar_variables,"completar_condicionales": completar_condicionales,"completar_ciclos": completar_ciclos,"completar_funciones": completar_funciones, "completar_examen_final": completar_examen_final})
                                    pygame.quit()
                                    sys.exit()
                            pygame.display.update()
                if evento.type == pygame.KEYDOWN:
                    #Si se presiona la flecha izquierda o derecha, se avanza en los diálogos
                    if evento.key == pygame.K_RIGHT and dialog_continue:
                        #Avanzar el diálogo
                        num_dialog += 1
                    elif num_dialog >= 0 and evento.key == pygame.K_LEFT and dialog_continue:
                        #Retroceder el diálogo
                        num_dialog -= 1
                    #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1
                    if evento.key == pygame.K_x:
                        ataque1 = True
                    #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3
                    if evento.key == pygame.K_z:
                        ataque3 = True
                    if error and evento.key == pygame.K_SPACE:
                        num_dialog = devolver
                        dialog_continue = True
                        error = False
            
            pygame.display.update()

    #Nivel de variables
    if variables:
        
        if seleccion == 1:
            #Extraemos los sprites individuales del personaje 1 con las dimensiones ajustadas
            sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//10, 87, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//10, 87, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//4, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//4, 84, 128, EI.ancho * 0.2, EI.alto * 0.22)
        elif seleccion == 2:
            #Extraemos los sprites individuales del personaje 2 con las dimensiones ajustadas
            sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 81, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//12, 85, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//12, 85, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 75, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 75, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 78, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//5, 80, 128, EI.ancho * 0.2, EI.alto * 0.22)
            sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//5, 80, 128, EI.ancho * 0.2, EI.alto * 0.22)

        
        quieto_derecha = pygame.transform.scale(quieto_derecha, (EI.ancho * 0.05, EI.alto * 0.22)) #Se adecua el sprite a un tamaño específico
        quieto_izquierda = pygame.transform.scale(quieto_izquierda, (EI.ancho * 0.05, EI.alto * 0.22)) #Se adecua el sprite a un tamaño específico
        caja_a_rota_transformada = pygame.transform.scale(EI.caja_a_rota, (EI.ancho * 0.1, EI.alto * 0.15))
        caja_b_rota_transformada = pygame.transform.scale(EI.caja_b_rota, (EI.ancho * 0.1, EI.alto * 0.15))
        caja_c_rota_transformada = pygame.transform.scale(EI.caja_c_rota, (EI.ancho * 0.1, EI.alto * 0.15))
        caja_d_rota_transformada = pygame.transform.scale(EI.caja_d_rota, (EI.ancho * 0.1, EI.alto * 0.15))

        #Variables para las respuestas
        caja_a_presionada = False
        caja_b_presionada = False
        caja_c_presionada = False
        caja_d_presionada = False
        prueba = True
        error = False

        #Variables para calcular la hitbox del personaje
        altura = EI.alto * 0.5
        altura_variables = EI.alto * 0.5
        velocidad_personaje_variables = EI.ancho * 0.8
        velocidad_personaje = EI.ancho * 0.8
        estado_caminar_derecha = None
        estado_caminar_izquierda = None
        estado_correr_derecha = None
        estado_correr_izquierda = None
        saltando = None
        anterior = 'derecha'
        ataque1 = None
        ataque3 = None
        posx_hitbox_derecha_variables = EI.ancho * 0.83
        posy_hitbox_derecha_variables = EI.alto * 0.5
        posx_hitbox_izquierda_variables = EI.ancho * 0.84
        posx_hitbox_derecha = EI.ancho * 0.63
        posy_hitbox_derecha = EI.alto * 0.31
        posx_hitbox_izquierda = EI.ancho * 0.64
        hitbox = pygame.Rect(EI.ancho * 0.63, EI.alto * 0.31, EI.ancho * 0.017, EI.alto * 0.08)
        mapa = False
        hitbox_variables = pygame.Rect(posx_hitbox_derecha_variables, posy_hitbox_derecha_variables, EI.ancho * 0.05, EI.alto * 0.25)
        rectangulo_caja_a = pygame.Rect(EI.ancho * 0.25, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)
        rectangulo_caja_b = pygame.Rect(EI.ancho * 0.4, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)
        rectangulo_caja_c = pygame.Rect(EI.ancho * 0.55, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)
        rectangulo_caja_d = pygame.Rect(EI.ancho * 0.7, EI.alto * 0.55, EI.ancho * 0.1, EI.alto * 0.15)

        while True:
            if anterior == "derecha":
                hitbox_variables = pygame.Rect(posx_hitbox_derecha_variables, posy_hitbox_derecha_variables, EI.ancho * 0.05, EI.alto * 0.3)
            elif anterior == "izquierda":
                hitbox_variables = pygame.Rect(posx_hitbox_derecha_variables, posy_hitbox_derecha_variables, EI.ancho * 0.05, EI.alto * 0.3)
            
            teclas = pygame.key.get_pressed()
            #Fondo
            EI.PANTALLA.fill((0,0,0))
            EI.PANTALLA.blit(fondo_aldea,fondo_aldea_rect)

            #Condicionales para el momento en el que se rompe la caja

            #Caja b correcta
            if not caja_b_presionada and (caja_a_presionada or caja_c_presionada or caja_d_presionada) and prueba and num_dialog == 10:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(variably,variably_rect)
                    EI.pregunta("Quiz de variables 1",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -100
                    break

            if caja_b_presionada and (not (caja_a_presionada or caja_c_presionada or caja_d_presionada)) and prueba and num_dialog == 10:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(variably,variably_rect)
                    EI.pregunta("Quiz de variables 1",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break

            #Caja d correcta
            if not caja_d_presionada and (caja_a_presionada or caja_b_presionada or caja_c_presionada) and prueba and num_dialog == 19:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(variably,variably_rect)
                    EI.pregunta("Quiz de variables 2",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -200
                    break

            if caja_d_presionada and (not (caja_a_presionada or caja_b_presionada or caja_c_presionada)) and prueba and num_dialog == 19:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(variably,variably_rect)
                    EI.pregunta("Quiz de variables 2",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break

            #Caja a correcta
            if not caja_a_presionada and (caja_d_presionada or caja_b_presionada or caja_c_presionada) and prueba and (num_dialog == 23 or num_dialog == 24 or num_dialog == 26):
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(variably,variably_rect)
                    EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -300
                    break

            if caja_a_presionada and (not (caja_d_presionada or caja_b_presionada or caja_c_presionada)) and prueba and (num_dialog == 23 or num_dialog == 24 or num_dialog == 26):
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(variably,variably_rect)
                    EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 

            #Caja b correcta
            if not caja_b_presionada and (caja_a_presionada or caja_c_presionada or caja_d_presionada) and prueba and num_dialog == 25:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(variably,variably_rect)
                    EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -300
                    break

            if caja_b_presionada and (not (caja_a_presionada or caja_c_presionada or caja_d_presionada)) and prueba and num_dialog == 25:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(variably,variably_rect)
                    EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break

            #Caja c correcta
            if not caja_c_presionada and (caja_d_presionada or caja_b_presionada or caja_a_presionada) and prueba and num_dialog == 27:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(variably,variably_rect)
                    EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog = -300
                    break

            if caja_c_presionada and (not (caja_d_presionada or caja_b_presionada or caja_a_presionada)) and prueba and num_dialog == 27:
                while True:
                    caja_a_presionada = False
                    caja_b_presionada = False
                    caja_c_presionada = False
                    caja_d_presionada = False
                    EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                    EI.PANTALLA.blit(variably,variably_rect)
                    EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                    pygame.time.wait(1000)
                    num_dialog += 1
                    break 
                

            #Diálogos
            if num_dialog == -1:
                EI.mostrar_texto("Escape Island","Llegando a la aldea de las variables.","(Usa las flechas para continuar).",color=EI.ROJO)
            elif num_dialog == 0:
                t1 = "Haz llegado a una aldea maravillosa."
                t2 = "Un aura de variabilidad llena el ambiente."
                t3 = "Sientes como tu gran aventura empieza de verdad."
                EI.mostrar_texto("Aldea de las variables",t1,t2,t3,color=EI.VERDE_OSCURO)
            elif num_dialog == 1:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "???"
                EI.mostrar_texto(personaje,"Hola.","Bienvenido a la aldea de las variables.")
            elif num_dialog == 2:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "???"
                EI.mostrar_texto(personaje,"Veo que estás perdido.", "Déjame ayudarte.")
            elif num_dialog == 3:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                EI.mostrar_texto(personaje,"Soy el jefe de la aldea de variables.", "Mi nombre es Variably.")
            elif num_dialog == 4:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                EI.mostrar_texto(personaje,"Para progresar por estos lados, necesitas aprender a programar variables.", "Pero, ¡no te preocupes!", "Yo te enseñaré.")
            elif num_dialog == 5:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                EI.mostrar_texto(personaje,"Aquí te explicaremos qué es una variable y cómo se usa.","Empecemos por lo básico.","¿Te parece?")
            elif num_dialog == 6:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Una variable es como un lugar en el que puedes almacenar cosas."
                t2 = "Esas cosas pueden ser números, cadenas de texto y otros tipos de datos."
                t3 = "Y son muy útiles, ya que puedes acceder a esa información cuando la necesites."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 7:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Por lo que una variable no es más que un espacio para guardar."
                t2 = "Uno en el que guardas información que necesites para hacer lo que tengas que hacer después."
                EI.mostrar_texto(personaje,t1,t2)
            elif num_dialog == 8:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Eso sería el concepto básico de una variable."
                t2 = "Este es el fin de tu primera lección."
                t3 = "Te voy a hacer una pregunta para ver si entendiste."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 9:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Te voy a dar una pregunta con 4 respuestas."
                t2 = "Selecciona la que más te parezca."
                t3 = "Para seleccionarla rompe la caja con 'x' o 'z'."
                EI.mostrar_texto(personaje,t1,t2,t3)
            elif num_dialog == 10:
                #Quiz de variables 1
                EI.PANTALLA.blit(variably,variably_rect)
                t1 = "¿Qué es una variable en programación?"
                a = "Una caja."
                b = "Un espacio para guardar información."
                c = "Un valor numérico."
                d = "Una cadena de texto."
                correcta = 2
                prueba = True
                EI.pregunta("Quiz de variables 1",[t1,"",""],a,b,c,d)
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Quiz de variables 1
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Quiz de variables 1",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Quiz de variables 1
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Quiz de variables 1",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Quiz de variables 1
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Quiz de variables 1",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Quiz de variables 1
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Quiz de variables 1",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

            elif num_dialog == 11: #Si responde correctamente
                prueba = False
                dialog_continue = True
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Bien hecho joven aventurero."
                t2 = "Haz completado exitosamente el primer paso para dominar las variables."
                t3 = "Ya que aprendimos la parte teórica, veamos como se aplica."
                EI.mostrar_texto(personaje,t1,t2,t3)
                

            elif num_dialog == -100: # Si se equivoca
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Eso no es correcto."
                t2 = "Vamos a volver a repasar el concepto clave."
                t3 = "Presiona 'Espacio' para continuar."
                EI.mostrar_texto(personaje,t1,t2,t3)
                error = True
                devolver = 6

            #Siguen los diálogos del segundo tutorial
            elif num_dialog == 12:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Para esto vamos a usar un lenguaje de programación que se llama Python."
                t2 = "Ya verás que es bastante intuitivo y fácil de usar."
                EI.mostrar_texto(personaje,t1,t2)

            elif num_dialog == 13:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Para hacer una variable primero debes ponerle un nombre."
                t2 = "Generalmente el nombre que le pones está relacionado con lo que guarda dentro."
                t3 = "Pero le puedes poner el nombre que más te parezca."
                EI.mostrar_texto(personaje,t1,t2,t3)

            elif num_dialog == 14:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Por ejemplo, si vas a asignar un nombre a una variable, puedes poner: nombre = 'Juan'"
                t2 = "Recuerda que las cadenas de texto van entre comillas dobles o simples."
                t3 = "Y así se guarda 'Juan' en la variable nombre."
                EI.mostrar_texto(personaje,t1,t2,t3)

            elif num_dialog == 15:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "También, puedes guardar números de la siguente manera:"
                t2 = "numero_entero = 42"
                t3 = "numero_decimal = -3.1416"
                EI.mostrar_texto(personaje,t1,t2,t3)

            elif num_dialog == 16:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "El último tipo de dato simple que puedes guardar es un booleano."
                t2 = "Este dato es un valor que puede ser verdadero o falso."
                t3 = "El valor de verdadero se escribe como 'True' y falso como 'False'."
                EI.mostrar_texto(personaje,t1,t2,t3)

            elif num_dialog == 17:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Un ejemplo de esto es el siguiente:"
                t2 = "valor = True"
                t3 = "No se te olvide que los booleanos van en mayúscula en Python."
                EI.mostrar_texto(personaje,t1,t2,t3)

            elif num_dialog == 17:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Esos son los tipos más sencillos de datos que vas a encontrar."
                t2 = "Y ya sabes como guardarlos en una variable para poder trabajar con ellos después."
                t3 = "Durante tu viaje seguirás usándolos y aprendiendo sobre estos."
                EI.mostrar_texto(personaje,t1,t2,t3)

            elif num_dialog == 18:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Eso es todo por tu segunda y última lección aquí en la aldea."
                t2 = "Te voy a hacer una pregunta para ver si entendiste bien la lección."
                t3 = "¡Aquí vamos!"
                EI.mostrar_texto(personaje,t1,t2,t3)

            elif num_dialog == 19:
                prueba = True
                #Quiz de variables 2
                EI.PANTALLA.blit(variably,variably_rect)
                t1 = "Si yo quiero crear una variable que se llame 'fruta' y que guarde mi fruta favorita,"
                t2 = "¿Cuál de las siguentes es la forma correcta de nombrar la variable?"
                t3 = "Ten en cuenta la manera en la que están escritas."
                a = "'fresa' = fruta"
                b = "'fruta' = manzana"
                c = "kiwi = 'fruta'"
                d = "fruta = 'banana'"
                correcta = 4
                EI.pregunta("Quiz de variables 2",[t1,t2,t3],a,b,c,d)
                dialog_continue = False
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Quiz de variables 2
                        EI.pregunta("Quiz de variables 2",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Quiz de variables 2",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Quiz de variables 2
                        EI.pregunta("Quiz de variables 2",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Quiz de variables 2",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Quiz de variables 2
                        EI.pregunta("Quiz de variables 2",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Quiz de variables 2",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Quiz de variables 2
                        EI.pregunta("Quiz de variables 2",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Quiz de variables 2",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

            elif num_dialog == -200: # Si se equivoca
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Eso no es correcto."
                t2 = "Devólvamonos para repasarlo."
                t3 = "Presiona 'Espacio' para continuar."
                EI.mostrar_texto(personaje,t1,t2,t3)
                error = True
                devolver = 13

            elif num_dialog == 20: # Si responde correctamente
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Muy bien."
                t2 = "Me queda claro que estás dominando el arte de crear variables."
                t3 = "Solo falta una última cosa que hacer."
                EI.mostrar_texto(personaje,t1,t2,t3)
                prueba = False
                dialog_continue = True

            elif num_dialog == 21:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Te vas a enfrentar al mayor reto que hayas visto hasta el momento."
                t2 = "Voy a hacerte 5 preguntas sobre lo que aprendiste hasta ahora."
                t3 = "Estarás solo. Yo simplemente observaré tus respuestas."
                EI.mostrar_texto(personaje,t1,t2,t3)

            elif num_dialog == 22:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Si pasas, podrás irte."
                t2 = "Si no, entonces tu tiempo aquí se alargará."
                t3 = "¿Estás listo?"
                EI.mostrar_texto(personaje,t1,t2,t3)

            elif num_dialog == 23:
                #Examen de variables
                #Pregunta 1
                t1 = "¿Para qué sirve una variable?"
                a = "Para guardar información."
                b = "Para hacer que un número varíe."
                c = "Para despejar una ecuación matemática."
                d = "Para ejecutar código."
                correcta = 1
                EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                dialog_continue = False
                prueba = True
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False


            elif num_dialog == 24:
                #Pregunta 2
                t1 = "¿Cuál es la sintaxis corecta para definir una variable en Python?"
                a = "variable = valor"
                b = "valor = variable"
                c = "variable == valor"
                d = "valor == variable"
                correcta = 1
                EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                dialog_continue = False
                prueba = True
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False


            elif num_dialog == 25:
                #Pregunta 3
                t1 = "Si se define la siguiente variable:"
                t2 = "ejecutando = True"
                t3 = "¿De qué tipo es la información qué guarda?"
                a = "Texto."
                b = "Booleano."
                c = "Número entero."
                d = "Número decimal."
                correcta = 2
                EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                dialog_continue = False
                prueba = True
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

            elif num_dialog == 26:
                #Pregunta 4
                t1 = "¿A qué corresponde el valor de la variable 'dulces' en el siguiente código?"
                t2 = "dulces = True"
                t3 = "dulces = 32"
                a = "32"
                b = "True"
                c = "None"
                d = "True 32"
                correcta = 1
                EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                dialog_continue = False
                prueba = True
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,t2,t3],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

            elif num_dialog == 27:
                #Pregunta 5
                t1 = "¿Cuál es el nombre del lenguaje de programación que hemos estado usando?"
                a = "C++"
                b = "Java"
                c = "Python"
                d = "C"
                correcta = 3
                EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                dialog_continue = False
                prueba = True
                #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
                if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
                    EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje_variables + EI.ancho * 0.027, altura_variables))
                if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
                    EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje_variables + EI.ancho * 0.04, altura_variables))

                #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
                if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) == False:
                    if posx_hitbox_derecha_variables < EI.ancho * 0.81:
                        velocidad_personaje_variables += EI.ancho * 0.002 
                        posx_hitbox_derecha_variables += EI.ancho * 0.002
                        posx_hitbox_izquierda_variables += EI.ancho * 0.002
                    sumar = - EI.ancho * 0.04
                    anterior = "derecha"

                    if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                        EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 0
                    elif estado_caminar_derecha == 0:
                        EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 1
                    elif estado_caminar_derecha == 1:
                        EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 2
                    elif estado_caminar_derecha == 2:
                        EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 3
                    elif estado_caminar_derecha == 3:
                        EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 4
                    elif estado_caminar_derecha == 4:
                        EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 5
                    elif estado_caminar_derecha == 5:
                        EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 6
                    elif estado_caminar_derecha == 6:
                        EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_derecha = 7

                #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
                if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        velocidad_personaje_variables -= EI.ancho * 0.002 
                        posx_hitbox_derecha_variables -= EI.ancho * 0.002
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.002

                    sumar = - EI.ancho * 0.05
                    anterior = "izquierda"
                    
                    if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 0
                    elif estado_caminar_izquierda == 0:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 1
                    elif estado_caminar_izquierda == 1:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 2
                    elif estado_caminar_izquierda == 2:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 3
                    elif estado_caminar_izquierda == 3:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 4
                    elif estado_caminar_izquierda == 4:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 5
                    elif estado_caminar_izquierda == 5:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 6
                    elif estado_caminar_izquierda == 6:
                        EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje_variables + sumar, altura_variables))
                        estado_caminar_izquierda = 7


                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
                if ataque1 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque1_derecha:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
                if ataque1 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque1_izquierda[::-1]:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque1 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "derecha" or anterior == None):
                    restar = EI.ancho * 0.02
                    if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                        posx_hitbox_izquierda_variables += EI.ancho * 0.012
                        posx_hitbox_derecha_variables += EI.ancho * 0.012
                    for sprite in sprites_ataque3_derecha:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_derecha_variables < EI.ancho * 0.8:
                            velocidad_personaje_variables += EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - restar, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
                if ataque3 and (anterior == "izquierda"):
                    if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                        posx_hitbox_izquierda_variables -= EI.ancho * 0.012
                        posx_hitbox_derecha_variables -= EI.ancho * 0.012
                    for sprite in sprites_ataque3_izquierda[::-1]:
                        #Examen de variables
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        EI.PANTALLA.blit(fondo_aldea, (EI.ancho * 0.1, 0))
                        EI.PANTALLA.blit(variably,variably_rect)
                        EI.pregunta("Examen de variables",[t1,"",""],a,b,c,d)
                        if posx_hitbox_izquierda_variables > EI.ancho * 0.2:
                            velocidad_personaje_variables -= EI.ancho * 0.003
                        EI.PANTALLA.blit(sprite, (velocidad_personaje_variables - EI.ancho * 0.02, altura_variables - EI.alto * 0.009))  #Se dibuja el sprite actual
                        pygame.display.flip()  #Se actualiza la pantalla
                        pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
                    if hitbox_variables.colliderect(rectangulo_caja_a):
                        caja_a_presionada = True
                        EI.PANTALLA.blit(caja_a_rota_transformada, (EI.ancho * 0.25, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_b):
                        caja_b_presionada = True
                        EI.PANTALLA.blit(caja_b_rota_transformada, (EI.ancho * 0.4, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_c):
                        caja_c_presionada = True
                        EI.PANTALLA.blit(caja_c_rota_transformada, (EI.ancho * 0.55, EI.alto * 0.54))
                    elif hitbox_variables.colliderect(rectangulo_caja_d):
                        EI.PANTALLA.blit(caja_d_rota_transformada, (EI.ancho * 0.7, EI.alto * 0.54))
                        caja_d_presionada = True
                    ataque3 = False

            elif num_dialog == -300: # Si no pasa
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Lo intentaste. No pierdas la esperanza."
                t2 = "Lo intentaremos otra vez."
                t3 = "Presiona 'Espacio' para continuar."
                EI.mostrar_texto(personaje,t1,t2,t3)
                error = True
                devolver = 6

            elif num_dialog == 28: # Si pasa
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Felicidades."
                t2 = "Eres un maestro de las variables."
                t3 = "Te deseo lo mejor aventurero."
                EI.mostrar_texto(personaje,t1,t2,t3)
                prueba = False
                dialog_continue = True

            elif num_dialog == 29:
                EI.PANTALLA.blit(variably,variably_rect)
                personaje = "Variably"
                t1 = "Ya puedes proseguir con tu camino."
                EI.mostrar_texto(personaje,t1)

            elif num_dialog == 30:
                EI.mostrar_texto("Escape Island","Saliendo de la aldea de variables.",color=EI.AZUL)

            elif num_dialog == 31:
                mapa = True
                variables = False
                var = True
                completar_variables = True
                
                break
            else:
                EI.mostrar_texto("","")

            #Eventos    
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                    romper = False
                    #Si se presiona la tecla "Esc", entonces aparece un cuadro de dialogo para confirmar la salida
                    while True:
                        if romper == True:
                            break
                        EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
                        EI.PANTALLA.blit(texto_salida, (EI.ancho * 0.3, EI.alto * 0.4))
                        boton_salida.dibujar(EI.PANTALLA)
                        boton_salida2.dibujar(EI.PANTALLA)
                        for evento in pygame.event.get():
                            if evento.type == pygame.MOUSEMOTION:
                                #Si el cursor del mouse pasa por encima de algún botón, entonces su color cambia
                                boton_salida.color_normal = EI.AZUL if not boton_salida.esta_encima(evento.pos) else EI.ROJO
                                boton_salida2.color_normal = EI.AZUL if not boton_salida2.esta_encima(evento.pos) else EI.ROJO
                            if evento.type == pygame.MOUSEBUTTONDOWN:
                                #Si se presiona 'Regresar', entonces se rompe el ciclo
                                if boton_salida2.esta_encima(evento.pos):
                                    romper = True
                                    break
                                #Si se presiona 'Guardar y salir', entonces se guarda el progreso y se termina el programa
                                if boton_salida.esta_encima(evento.pos):
                                    EI.guardar_informacion({"completar_variables": completar_variables,"completar_condicionales": completar_condicionales,"completar_ciclos": completar_ciclos,"completar_funciones": completar_funciones, "completar_examen_final": completar_examen_final})
                                    pygame.quit()
                                    sys.exit()
                            pygame.display.update()
                if evento.type == pygame.KEYDOWN:
                    #Si se presiona la flecha izquierda o derecha, se avanza en los diálogos
                    if evento.key == pygame.K_RIGHT and dialog_continue:
                        #Avanzar el diálogo
                        num_dialog += 1
                    elif num_dialog >= 0 and evento.key == pygame.K_LEFT and dialog_continue:
                        #Retroceder el diálogo
                        num_dialog -= 1
                    #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1
                    if evento.key == pygame.K_x:
                        ataque1 = True
                    #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3
                    if evento.key == pygame.K_z:
                        ataque3 = True
                    if error and evento.key == pygame.K_SPACE:
                        num_dialog = devolver
                        dialog_continue = True
                        error = False
            
            pygame.display.update()
    
    if mapa:
        
        if (num_dialog == -1 or num_dialog >= 31) and (var or con or cic):
            altura = EI.alto * 0.3
            velocidad_personaje = EI.ancho * 0.6
            posx_hitbox_derecha = EI.ancho * 0.63
            posy_hitbox_derecha = EI.alto * 0.31
            posx_hitbox_izquierda = EI.ancho * 0.64
            hitbox = pygame.Rect(EI.ancho * 0.63, EI.alto * 0.31, EI.ancho * 0.017, EI.alto * 0.08)
            var = False
            con = False
            cic = False

        if anterior == "derecha":
            hitbox = pygame.Rect(posx_hitbox_derecha, posy_hitbox_derecha, EI.ancho * 0.017, EI.alto * 0.0802)
        elif anterior == "izquierda":
            hitbox = pygame.Rect(posx_hitbox_izquierda, posy_hitbox_derecha, EI.ancho * 0.017, EI.alto * 0.0802)
            
        if seleccion == 1:
            quieto_derecha = pygame.transform.scale(quieto_derecha, (EI.ancho * 0.022, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
            quieto_izquierda = pygame.transform.scale(quieto_izquierda, (EI.ancho * 0.022, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
            #Extraemos los sprites individuales del personaje 1
            sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 78, 128)
            sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 84, 128)
            sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//10, 87, 128)
            sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//10, 87, 128)
            sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 84, 128)
            sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 78, 128)
            sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 81, 128)
            sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 81, 128)
            sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//4, 84, 128)
            sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//4, 84, 128)
        elif seleccion == 2:
            quieto_derecha = pygame.transform.scale(quieto_derecha, (EI.ancho * 0.022, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
            quieto_izquierda = pygame.transform.scale(quieto_izquierda, (EI.ancho * 0.022, EI.alto * 0.09)) #Se adecua el sprite a un tamaño específico
            #Extraemos los sprites individuales del personaje 2
            sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//8, 81, 128)
            sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//8, 81, 128)
            sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//12, 85, 128)
            sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//12, 85, 128)
            sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//8, 75, 128)
            sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//8, 75, 128)
            sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//4, 78, 128)
            sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//4, 78, 128)
            sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//5, 80, 128)
            sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//5, 80, 128)
 

        #Eventos
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:
                romper = False
            #Si se presiona la tecla "Esc", entonces aparece un cuadro de dialogo para confirmar la salida
                while True:
                    if romper == True:
                        break
                    EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
                    EI.PANTALLA.blit(texto_salida, (EI.ancho * 0.3, EI.alto * 0.4))
                    boton_salida.dibujar(EI.PANTALLA)
                    boton_salida2.dibujar(EI.PANTALLA)
                    for evento in pygame.event.get():
                        if evento.type == pygame.MOUSEMOTION:
                            #Si el cursor del mouse pasa por encima de algún botón, entonces su color cambia
                            boton_salida.color_normal = EI.AZUL if not boton_salida.esta_encima(evento.pos) else EI.ROJO
                            boton_salida2.color_normal = EI.AZUL if not boton_salida2.esta_encima(evento.pos) else EI.ROJO
                        if evento.type == pygame.MOUSEBUTTONDOWN:
                            #Si se presiona 'Regresar', entonces se rompe el ciclo
                            if boton_salida2.esta_encima(evento.pos):
                                romper = True
                                break
                            #Si se presiona 'Guardar y salir', entonces se guarda el progreso y se termina el programa
                            if boton_salida.esta_encima(evento.pos):
                                EI.guardar_informacion({"completar_variables": completar_variables,"completar_condicionales": completar_condicionales,"completar_ciclos": completar_ciclos,"completar_funciones": completar_funciones, "completar_examen_final": completar_examen_final})
                                pygame.quit()
                                sys.exit()
                        pygame.display.update()
            if evento.type == pygame.KEYDOWN:
                #Si se presiona la tecla "espacio", entonces el personaje salta
                if evento.key == pygame.K_SPACE:
                    saltando = True
                #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1
                if evento.key == pygame.K_x:
                    ataque1 = True
                #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3
                if evento.key == pygame.K_z:
                    ataque3 = True
            #Si se presiona algún botón, entonces se abre el nivel
            if evento.type == pygame.MOUSEBUTTONDOWN:
                #Variables
                if boton_niveles.esta_encima(evento.pos) and hitbox.colliderect(hitbox_nivel_variables):
                    variables = True
                #Condicionales
                elif boton_niveles.esta_encima(evento.pos) and hitbox.colliderect(hitbox_nivel_condicionales) and completar_variables:
                    condicionales = True
                #Ciclos
                elif boton_niveles.esta_encima(evento.pos) and hitbox.colliderect(hitbox_nivel_ciclos) and completar_condicionales:
                    ciclos = True
                #Funciones
                elif boton_niveles.esta_encima(evento.pos) and hitbox.colliderect(hitbox_nivel_funciones) and completar_ciclos:
                    funciones = True
                #Examen final
                elif boton_niveles.esta_encima(evento.pos) and hitbox.colliderect(hitbox_examen_final) and completar_funciones:
                    examen_final = True
            
            if evento.type == pygame.MOUSEMOTION:
                #Si el cursor del mouse pasa por encima de algún botón, entonces su color cambia
                boton_niveles.color_normal = EI.AZUL if not boton_niveles.esta_encima(evento.pos) else EI.ROJO

        

        EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
        #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
        if ataque1 and (anterior == "derecha" or anterior == None):
            restar = EI.ancho * 0.02
            if posx_hitbox_derecha < EI.ancho * 0.9:
                posx_hitbox_izquierda += EI.ancho * 0.012
                posx_hitbox_derecha += EI.ancho * 0.012
            for sprite in sprites_ataque1_derecha:
                EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
                if posx_hitbox_derecha < EI.ancho * 0.9:
                    velocidad_personaje += EI.ancho * 0.003
                EI.PANTALLA.blit(sprite, (velocidad_personaje - restar, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                pygame.display.flip()  #Se actualiza la pantalla
                pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
            ataque1 = False

        #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1           
        if ataque1 and (anterior == "izquierda"):
            if posx_hitbox_izquierda > EI.ancho * 0.05:
                posx_hitbox_izquierda -= EI.ancho * 0.012
                posx_hitbox_derecha -= EI.ancho * 0.012
            for sprite in sprites_ataque1_izquierda[::-1]:
                EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
                if posx_hitbox_izquierda > EI.ancho * 0.05:
                    velocidad_personaje -= EI.ancho * 0.003
                EI.PANTALLA.blit(sprite, (velocidad_personaje + EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                pygame.display.flip()  #Se actualiza la pantalla
                pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
            ataque1 = False

        #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
        if ataque3 and (anterior == "derecha" or anterior == None):
            restar = EI.ancho * 0.02
            if posx_hitbox_derecha < EI.ancho * 0.9:
                posx_hitbox_izquierda += EI.ancho * 0.012
                posx_hitbox_derecha += EI.ancho * 0.012
            for sprite in sprites_ataque3_derecha:
                EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
                if posx_hitbox_derecha < EI.ancho * 0.9:
                    velocidad_personaje += EI.ancho * 0.003
                EI.PANTALLA.blit(sprite, (velocidad_personaje - restar, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                pygame.display.flip()  #Se actualiza la pantalla
                pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
            ataque3 = False

        #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3            
        if ataque3 and (anterior == "izquierda"):
            if posx_hitbox_izquierda > EI.ancho * 0.05:
                posx_hitbox_izquierda -= EI.ancho * 0.012
                posx_hitbox_derecha -= EI.ancho * 0.012
            for sprite in sprites_ataque3_izquierda[::-1]:
                EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
                if posx_hitbox_izquierda > EI.ancho * 0.05:
                    velocidad_personaje -= EI.ancho * 0.003
                EI.PANTALLA.blit(sprite, (velocidad_personaje + EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                pygame.display.flip()  #Se actualiza la pantalla
                pygame.time.delay(90)  #Se pausa la ejecución durante un breve período de tiempo
            ataque3 = False

        #Si se presiona la tecla "espacio", entonces el personaje salta
        if saltando and (anterior == "derecha" or anterior == None):
            if posx_hitbox_derecha < EI.ancho * 0.9:
                posx_hitbox_derecha += EI.ancho * 0.03
                posx_hitbox_izquierda += EI.ancho * 0.03
            for sprite in sprites_saltar_derecha:
                EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
                if posx_hitbox_derecha < EI.ancho * 0.9:
                    velocidad_personaje += EI.ancho * 0.003
                EI.PANTALLA.blit(sprite, (velocidad_personaje - EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                pygame.display.flip()  #Se actualiza la pantalla
                pygame.time.delay(50)  #Se pausa la ejecución durante un breve período de tiempo
            saltando = False

        #Si se presiona la tecla "espacio", entonces el personaje salta
        if saltando and (anterior == "izquierda"):
            if posx_hitbox_izquierda > EI.ancho * 0.05:
                posx_hitbox_derecha -= EI.ancho * 0.03
                posx_hitbox_izquierda -= EI.ancho * 0.03
            for sprite in sprites_saltar_izquierda[::-1]:
                EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
                if posx_hitbox_izquierda > EI.ancho * 0.05:
                    velocidad_personaje -= EI.ancho * 0.003
                EI.PANTALLA.blit(sprite, (velocidad_personaje + EI.ancho * 0.02, altura - EI.alto * 0.009))  #Se dibuja el sprite actual
                pygame.display.flip()  #Se actualiza la pantalla
                pygame.time.delay(50)  #Se pausa la ejecución durante un breve período de tiempo
            saltando = False

        teclas = pygame.key.get_pressed() 
        #Si no se está presionando ninguna tecla, entonces el personaje se queda quieto
        if teclas[pygame.K_RIGHT] == False and (anterior == "derecha" or anterior == None):
            EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
        if teclas[pygame.K_LEFT] == False and (anterior == "izquierda"):
            EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))

        #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
        if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "derecha" or anterior == None) and posy_hitbox_derecha < EI.alto * 0.46:
            altura += EI.alto * 0.01
            posy_hitbox_derecha += EI.ancho * 0.0055
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))

        #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
        if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "izquierda") and posy_hitbox_derecha < EI.alto * 0.46:
            altura += EI.alto * 0.01
            posy_hitbox_derecha += EI.ancho * 0.0055
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
        
        #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "derecha" or anterior == None):
            if posy_hitbox_derecha > 0:
                altura -= EI.alto * 0.01
                posy_hitbox_derecha -= EI.ancho * 0.0055
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
        
        #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "izquierda"):
            if posy_hitbox_derecha > 0:
                altura -= EI.alto * 0.01
                posy_hitbox_derecha -= EI.ancho * 0.0055
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
        
        
        #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]) == False:
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            if posx_hitbox_derecha < EI.ancho * 0.9:
                velocidad_personaje += EI.ancho * 0.002 
                posx_hitbox_derecha += EI.ancho * 0.002
                posx_hitbox_izquierda += EI.ancho * 0.002

            sumar = 0
            anterior = "derecha"
            if estado_caminar_derecha == None or estado_caminar_derecha == 7:
                EI.PANTALLA.blit(sprites_caminar_derecha[0], (velocidad_personaje + sumar, altura))
                estado_caminar_derecha = 0
            elif estado_caminar_derecha == 0:
                EI.PANTALLA.blit(sprites_caminar_derecha[1], (velocidad_personaje + sumar, altura))
                estado_caminar_derecha = 1
            elif estado_caminar_derecha == 1:
                EI.PANTALLA.blit(sprites_caminar_derecha[2], (velocidad_personaje + sumar, altura))
                estado_caminar_derecha = 2
            elif estado_caminar_derecha == 2:
                EI.PANTALLA.blit(sprites_caminar_derecha[3], (velocidad_personaje + sumar, altura))
                estado_caminar_derecha = 3
            elif estado_caminar_derecha == 3:
                EI.PANTALLA.blit(sprites_caminar_derecha[4], (velocidad_personaje + sumar, altura))
                estado_caminar_derecha = 4
            elif estado_caminar_derecha == 4:
                EI.PANTALLA.blit(sprites_caminar_derecha[5], (velocidad_personaje + sumar, altura))
                estado_caminar_derecha = 5
            elif estado_caminar_derecha == 5:
                EI.PANTALLA.blit(sprites_caminar_derecha[6], (velocidad_personaje + sumar, altura))
                estado_caminar_derecha = 6
            elif estado_caminar_derecha == 6:
                EI.PANTALLA.blit(sprites_caminar_derecha[7], (velocidad_personaje + sumar, altura))
                estado_caminar_derecha = 7

        #Si la tecla izquierda está siendo presionada o "a", entonces el personaje camina hacia la izquierda
        if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]) == False:
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            if posx_hitbox_izquierda > EI.ancho * 0.05:
                velocidad_personaje -= EI.ancho * 0.002 
                posx_hitbox_derecha -= EI.ancho * 0.002
                posx_hitbox_izquierda -= EI.ancho * 0.002
            sumar = 0
            anterior = "izquierda"
            if estado_caminar_izquierda == None or estado_caminar_izquierda == 7:
                EI.PANTALLA.blit(sprites_caminar_izquierda[7], (velocidad_personaje + sumar, altura))
                estado_caminar_izquierda = 0
            elif estado_caminar_izquierda == 0:
                EI.PANTALLA.blit(sprites_caminar_izquierda[6], (velocidad_personaje + sumar, altura))
                estado_caminar_izquierda = 1
            elif estado_caminar_izquierda == 1:
                EI.PANTALLA.blit(sprites_caminar_izquierda[5], (velocidad_personaje + sumar, altura))
                estado_caminar_izquierda = 2
            elif estado_caminar_izquierda == 2:
                EI.PANTALLA.blit(sprites_caminar_izquierda[4], (velocidad_personaje + sumar, altura))
                estado_caminar_izquierda = 3
            elif estado_caminar_izquierda == 3:
                EI.PANTALLA.blit(sprites_caminar_izquierda[3], (velocidad_personaje + sumar, altura))
                estado_caminar_izquierda = 4
            elif estado_caminar_izquierda == 4:
                EI.PANTALLA.blit(sprites_caminar_izquierda[2], (velocidad_personaje + sumar, altura))
                estado_caminar_izquierda = 5
            elif estado_caminar_izquierda == 5:
                EI.PANTALLA.blit(sprites_caminar_izquierda[1], (velocidad_personaje + sumar, altura))
                estado_caminar_izquierda = 6
            elif estado_caminar_izquierda == 6:
                EI.PANTALLA.blit(sprites_caminar_izquierda[0], (velocidad_personaje + sumar, altura))
                estado_caminar_izquierda = 7

        #Si la tecla derecha o "d" y shift están siendo presionadas, entonces el personaje corre hacia la derecha
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
            if posx_hitbox_derecha < EI.ancho * 0.9:
                velocidad_personaje += EI.ancho * 0.003
                posx_hitbox_derecha += EI.ancho * 0.003
                posx_hitbox_izquierda += EI.ancho * 0.003
            anterior = "derecha"
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            if estado_correr_derecha == None or estado_correr_derecha == 7:
                EI.PANTALLA.blit(sprites_correr_derecha[0], (velocidad_personaje, altura))
                estado_correr_derecha = 0
            elif estado_correr_derecha == 0:
                EI.PANTALLA.blit(sprites_correr_derecha[1], (velocidad_personaje, altura))
                estado_correr_derecha = 1
            elif estado_correr_derecha == 1:
                EI.PANTALLA.blit(sprites_correr_derecha[2], (velocidad_personaje, altura))
                estado_correr_derecha = 2
            elif estado_correr_derecha == 2:
                EI.PANTALLA.blit(sprites_correr_derecha[3], (velocidad_personaje, altura))
                estado_correr_derecha = 3
            elif estado_correr_derecha == 3:
                EI.PANTALLA.blit(sprites_correr_derecha[4], (velocidad_personaje, altura))
                estado_correr_derecha = 4
            elif estado_correr_derecha == 4:
                EI.PANTALLA.blit(sprites_correr_derecha[5], (velocidad_personaje, altura))
                estado_correr_derecha = 5
            elif estado_correr_derecha == 5:
                EI.PANTALLA.blit(sprites_correr_derecha[6], (velocidad_personaje, altura))
                estado_correr_derecha = 6
            elif estado_correr_derecha == 6:
                EI.PANTALLA.blit(sprites_correr_derecha[7], (velocidad_personaje, altura))
                estado_correr_derecha = 7

        #Si la tecla izquierda o "a" y shift están siendo presionadas, entonces el personaje corre hacia la izquierda
        if (teclas[pygame.K_LEFT] or teclas[pygame.K_a]) and (teclas[pygame.K_LSHIFT] or teclas[pygame.K_RSHIFT]):
            if posx_hitbox_izquierda > EI.ancho * 0.05:
                velocidad_personaje -= EI.ancho * 0.003
                posx_hitbox_derecha -= EI.ancho * 0.003
                posx_hitbox_izquierda -= EI.ancho * 0.003
            anterior = "izquierda"
            EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla
            if estado_correr_izquierda == None or estado_correr_izquierda == 7:
                EI.PANTALLA.blit(sprites_correr_izquierda[7], (velocidad_personaje, altura))
                estado_correr_izquierda = 0
            elif estado_correr_izquierda == 0:
                EI.PANTALLA.blit(sprites_correr_izquierda[6], (velocidad_personaje, altura))
                estado_correr_izquierda = 1
            elif estado_correr_izquierda == 1:
                EI.PANTALLA.blit(sprites_correr_izquierda[5], (velocidad_personaje, altura))
                estado_correr_izquierda = 2
            elif estado_correr_izquierda == 2:
                EI.PANTALLA.blit(sprites_correr_izquierda[4], (velocidad_personaje, altura))
                estado_correr_izquierda = 3
            elif estado_correr_izquierda == 3:
                EI.PANTALLA.blit(sprites_correr_izquierda[3], (velocidad_personaje, altura))
                estado_correr_izquierda = 4
            elif estado_correr_izquierda == 4:
                EI.PANTALLA.blit(sprites_correr_izquierda[2], (velocidad_personaje, altura))
                estado_correr_izquierda = 5
            elif estado_correr_izquierda == 5:
                EI.PANTALLA.blit(sprites_correr_izquierda[1], (velocidad_personaje, altura))
                estado_correr_izquierda = 6
            elif estado_correr_izquierda == 6:
                EI.PANTALLA.blit(sprites_correr_izquierda[0], (velocidad_personaje, altura))
                estado_correr_izquierda = 7
        
        #Si la hitbox del personaje superpone la hitbox de algún nivel, entonces se muestra la interfaz para ingresar a ese nivel

        #Variables
        if hitbox.colliderect(hitbox_nivel_variables):
            EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
            EI.PANTALLA.blit(texto_variables, (EI.ancho * 0.3, EI.alto * 0.35))
            boton_niveles.dibujar(EI.PANTALLA)
            if completar_variables:
                EI.PANTALLA.blit(estrella_rellena_transformada, (EI.ancho * 0.52, EI.alto * 0.43))
            else: 
                EI.PANTALLA.blit(estrella_vacia_transformada, (EI.ancho * 0.52, EI.alto * 0.43))
        #Condicionales
        elif hitbox.colliderect(hitbox_nivel_condicionales):
            EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
            EI.PANTALLA.blit(texto_condicionales, (EI.ancho * 0.29, EI.alto * 0.35))
            boton_niveles.dibujar(EI.PANTALLA)
            if completar_condicionales:
                EI.PANTALLA.blit(estrella_rellena_transformada, (EI.ancho * 0.52, EI.alto * 0.43))
            else: 
                EI.PANTALLA.blit(estrella_vacia_transformada, (EI.ancho * 0.52, EI.alto * 0.43))
        #Ciclos
        elif hitbox.colliderect(hitbox_nivel_ciclos):
            EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
            EI.PANTALLA.blit(texto_ciclos, (EI.ancho * 0.35, EI.alto * 0.35))
            boton_niveles.dibujar(EI.PANTALLA)
            if completar_ciclos:
                EI.PANTALLA.blit(estrella_rellena_transformada, (EI.ancho * 0.52, EI.alto * 0.43))
            else: 
                EI.PANTALLA.blit(estrella_vacia_transformada, (EI.ancho * 0.52, EI.alto * 0.43))
        #Funciones
        elif hitbox.colliderect(hitbox_nivel_funciones):
            EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
            EI.PANTALLA.blit(texto_funciones, (EI.ancho * 0.33, EI.alto * 0.35))
            boton_niveles.dibujar(EI.PANTALLA)
            if completar_funciones:
                EI.PANTALLA.blit(estrella_rellena_transformada, (EI.ancho * 0.52, EI.alto * 0.43))
            else: 
                EI.PANTALLA.blit(estrella_vacia_transformada, (EI.ancho * 0.52, EI.alto * 0.43))
        #Examen final
        elif hitbox.colliderect(hitbox_examen_final):
            EI.PANTALLA.blit(dialogo, (EI.ancho * 0.25, EI.alto * 0.3))
            EI.PANTALLA.blit(texto_examen_final, (EI.ancho * 0.38, EI.alto * 0.35))
            boton_niveles.dibujar(EI.PANTALLA)
            if completar_examen_final:
                EI.PANTALLA.blit(estrella_rellena_transformada, (EI.ancho * 0.52, EI.alto * 0.43))
            else: 
                EI.PANTALLA.blit(estrella_vacia_transformada, (EI.ancho * 0.52, EI.alto * 0.43))

    pygame.time.Clock().tick(30)
    #pygame.draw.rect(EI.PANTALLA, EI.ROJO, (EI.ancho * 0.22, EI.alto * 0.12, EI.ancho * 0.09, EI.alto * 0.1))
    pygame.display.update()
    
