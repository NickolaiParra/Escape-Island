import pygame
import sys

pygame.init()

from Módulos import Escape_Island as EI


seleccion = 0

#Texto
fuente_2 = pygame.font.Font("Fuentes\\Nicolast.otf", int(EI.ancho * 0.04)) 
texto_seleccionar = fuente_2.render('Selecciona   tu   personaje', True, (EI.ROJO))

#Botones
boton_personaje1 = EI.Boton(EI.ancho * 0.1, EI.alto * 0.27, EI.ancho * 0.2, EI.alto * 0.5, "", 0, 0)
boton_personaje2 = EI.Boton(EI.ancho * 0.4, EI.alto * 0.27, EI.ancho * 0.2, EI.alto * 0.5, "", 0, 0)
boton_personaje3 = EI.Boton(EI.ancho * 0.7, EI.alto * 0.27, EI.ancho * 0.2, EI.alto * 0.5, "", 0, 0)
boton_cancelar = EI.Boton(EI.ancho * 0.2, EI.alto * 0.85, EI.ancho * 0.2, EI.alto * 0.1, "Cancelar", int(EI.ancho * 0.05), int(EI.ancho * 0.015))
boton_aceptar = EI.Boton(EI.ancho * 0.6, EI.alto * 0.85, EI.ancho * 0.2, EI.alto * 0.1, "Aceptar", int(EI.ancho * 0.05), int(EI.ancho * 0.015))

#Imágenes
#Personaje 1
quieto_derecha1 = pygame.image.load("Imagenes\Sprites\Personaje_1\quieto_derecha.png")
quieto_derecha1 = pygame.transform.scale(quieto_derecha1, (EI.ancho * 0.09, EI.alto * 0.4)) #Se adecua el sprite a un tamaño específico
#Personaje 2
quieto_derecha2 = pygame.image.load("Imagenes\Sprites\Personaje_2\quieto_derecha.png")
quieto_derecha2 = pygame.transform.scale(quieto_derecha2, (EI.ancho * 0.1, EI.alto * 0.4)) #Se adecua el sprite a un tamaño específico
#Personaje 3
quieto_derecha3 = pygame.image.load("Imagenes\Sprites\Personaje_3\quieto_derecha.png")
quieto_derecha3 = pygame.transform.scale(quieto_derecha3, (EI.ancho * 0.19, EI.alto * 0.34)) #Se adecua el sprite a un tamaño específico
#Candado
candado_cerrado = pygame.image.load("Imagenes\Iconos\Candado_cerrado.png")
candado_cerrado = pygame.transform.scale(candado_cerrado, (EI.ancho * 0.15, EI.alto * 0.3)) #Se adecua la imagen a un tamaño específico
candado_abierto = pygame.image.load("Imagenes\Iconos\Candado_abierto.png")

p1 = False
p2 = False

controlar_bucle = False

while True:
    if controlar_bucle:
        break
    for evento in pygame.event.get():
        if evento.type == pygame.KEYDOWN:
            #Si se presiona la tecla "Esc", entonces se sale del juego
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
        #Si se da click con el mouse encima de algún botón, entonces su color cambia
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_personaje1.esta_encima(evento.pos):
            boton_personaje1.color_normal = EI.ROJO 
            boton_personaje2.color_normal = EI.AZUL
            boton_personaje3.color_normal = EI.AZUL
            p1 = True
            p2 = False
            
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_personaje2.esta_encima(evento.pos):
            boton_personaje2.color_normal = EI.ROJO
            boton_personaje1.color_normal = EI.AZUL 
            boton_personaje3.color_normal = EI.AZUL
            p2 = True
            p1 = False

        if evento.type == pygame.MOUSEMOTION:
            #Si el cursor del mouse pasa por encima de algún  botón, entonces su color cambia
            boton_personaje1.color_normal = EI.AZUL if not boton_personaje1.esta_encima(evento.pos) and not p1 else EI.ROJO
            boton_personaje2.color_normal = EI.AZUL if not boton_personaje2.esta_encima(evento.pos) and not p2 else EI.ROJO
            boton_personaje3.color_normal = EI.AZUL if not boton_personaje3.esta_encima(evento.pos) else EI.GRIS
            boton_aceptar.color_normal = EI.AZUL if not boton_aceptar.esta_encima(evento.pos) else EI.ROJO
            boton_cancelar.color_normal = EI.AZUL if not boton_cancelar.esta_encima(evento.pos) else EI.ROJO
        
        if evento.type == pygame.MOUSEBUTTONDOWN and boton_aceptar.esta_encima(evento.pos) and (p1 or p2):
            seleccion = 1 if p1 else 2
            controlar_bucle = True
            break

        


    EI.PANTALLA.fill(EI.FONDO) #Se limpia la pantalla
    #Mostramos los botones
    boton_personaje1.dibujar(EI.PANTALLA)
    boton_personaje2.dibujar(EI.PANTALLA)
    boton_personaje3.dibujar(EI.PANTALLA)
    boton_cancelar.dibujar(EI.PANTALLA)
    boton_aceptar.dibujar(EI.PANTALLA)
    
    EI.PANTALLA.blit(quieto_derecha1, (EI.ancho * 0.15, EI.alto * 0.32)) #Se imprime la imágen del personaje 1
    EI.PANTALLA.blit(quieto_derecha2, (EI.ancho * 0.45, EI.alto * 0.32)) #Se imprime la imágen del personaje 2
    EI.PANTALLA.blit(quieto_derecha3, (EI.ancho * 0.705, EI.alto * 0.37)) #Se imprime la imágen del personaje 3
    EI.PANTALLA.blit(candado_cerrado, (EI.ancho * 0.725, EI.alto * 0.35)) #Se imprime la imágen del candado cerrado

    EI.PANTALLA.blit(texto_seleccionar, (EI.ancho * 0.2, EI.alto * 0.1)) #Se imprime el texto "Selecciona tu personaje"
    

    pygame.display.flip() #Actualizar la pantalla

if seleccion == 1:
    #Cargamos las hojas de sprites del personaje 1
    quieto_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\quieto_derecha.png")
    quieto_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\quieto_izquierda.png")
    correr_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\correr_derecha.png")
    caminar_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\caminar_derecha.png")
    caminar_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\caminar_izquierda.png")
    correr_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\correr_izquierda.png")
    ataque1_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\\ataque1_derecha.png")
    ataque1_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\\ataque1_izquierda.png")
    ataque3_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\\ataque3_derecha.png")
    ataque3_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\\ataque3_izquierda.png")
    saltar_derecha = pygame.image.load("Imagenes\Sprites\Personaje_1\saltar_derecha.png")
    saltar_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_1\saltar_izquierda.png")
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
    quieto_derecha = pygame.image.load("Imagenes\Sprites\Personaje_2\quieto_derecha.png")
    quieto_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_2\quieto_izquierda.png")
    correr_derecha = pygame.image.load("Imagenes\Sprites\Personaje_2\correr_derecha.png")
    caminar_derecha = pygame.image.load("Imagenes\Sprites\Personaje_2\caminar_derecha.png")
    caminar_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_2\caminar_izquierda.png")
    correr_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_2\correr_izquierda.png")
    ataque1_derecha = pygame.image.load("Imagenes\Sprites\Personaje_2\\ataque1_derecha.png")
    ataque1_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_2\\ataque1_izquierda.png")
    ataque3_derecha = pygame.image.load("Imagenes\Sprites\Personaje_2\\ataque3_derecha.png")
    ataque3_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_2\\ataque3_izquierda.png")
    saltar_derecha = pygame.image.load("Imagenes\Sprites\Personaje_2\saltar_derecha.png")
    saltar_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_2\saltar_izquierda.png")
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
elif seleccion == 3:
    #Cargamos las hojas de sprites del personaje 3
    quieto_derecha = pygame.image.load("Imagenes\Sprites\Personaje_3\quieto_derecha.png")
    quieto_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_3\quieto_izquierda.png")
    correr_derecha = pygame.image.load("Imagenes\Sprites\Personaje_3\correr_derecha.png")
    caminar_derecha = pygame.image.load("Imagenes\Sprites\Personaje_3\caminar_derecha.png")
    caminar_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_3\caminar_izquierda.png")
    correr_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_3\correr_izquierda.png")
    ataque1_derecha = pygame.image.load("Imagenes\Sprites\Personaje_3\\ataque1_derecha.png")
    ataque1_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_3\\ataque1_izquierda.png")
    ataque3_derecha = pygame.image.load("Imagenes\Sprites\Personaje_3\\ataque3_derecha.png")
    ataque3_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_3\\ataque3_izquierda.png")
    saltar_derecha = pygame.image.load("Imagenes\Sprites\Personaje_3\saltar_derecha.png")
    saltar_izquierda = pygame.image.load("Imagenes\Sprites\Personaje_3\saltar_izquierda.png")
    #Extraemos los sprites individuales del personaje 3
    sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//11, 80, 128)
    sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//11, 80, 128)
    sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//11, 92, 128)
    sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//11, 92, 128)
    sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//9, 81, 128)
    sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//9, 81, 128)
    sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//5, 95, 128)
    sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//5, 95, 128)
    sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//6, 90, 128)
    sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//6, 90, 128)



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
        if evento.type == pygame.KEYDOWN:
            #Si se presiona la tecla "Esc", entonces se sale del juego
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            elif evento.key == pygame.K_RETURN or evento.key == pygame.K_KP_ENTER:
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
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]):
            EI.PANTALLA.blit(fondo1, (0, 0))
            EI.mostrar_texto("Movimientos", "Para comenzar, usa las flechas para desplazarte:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(flecha_derecha, (EI.ancho * 0.65, EI.alto * 0.75))
            if posx_hitbox_derecha < EI.ancho * 0.95:
                velocidad_personaje += EI.ancho * 0.002 
                posx_hitbox_derecha += EI.ancho * 0.002
                posx_hitbox_izquierda += EI.ancho * 0.002
            sumar = EI.ancho * 0.015 if seleccion == 3 else - EI.ancho * 0.04
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

            sumar = EI.ancho * 0.02 if seleccion == 3 else - EI.ancho * 0.05
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
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]):
            EI.PANTALLA.blit(fondo1, (0, 0))
            EI.mostrar_texto("Movimientos", "Puedes presionar las flechas + shift para correr:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(shift_flechaderecha, (EI.ancho * 0.7, EI.alto * 0.75))
            if posx_hitbox_derecha < EI.ancho * 0.95:
                velocidad_personaje += EI.ancho * 0.002 
                posx_hitbox_derecha += EI.ancho * 0.002
                posx_hitbox_izquierda += EI.ancho * 0.002
            sumar = EI.ancho * 0.015 if seleccion == 3 else - EI.ancho * 0.04
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

            sumar = EI.ancho * 0.02 if seleccion == 3 else - EI.ancho * 0.05
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
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]):
            EI.PANTALLA.blit(fondo1, (0, 0))
            EI.mostrar_texto("Movimientos", "Puedes presionar espacio para saltar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(espacio_sinpresionar, (EI.ancho * 0.6, EI.alto * 0.8))
            if posx_hitbox_derecha < EI.ancho * 0.95:
                velocidad_personaje += EI.ancho * 0.002 
                posx_hitbox_derecha += EI.ancho * 0.002
                posx_hitbox_izquierda += EI.ancho * 0.002
            sumar = EI.ancho * 0.015 if seleccion == 3 else - EI.ancho * 0.04
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

            sumar = EI.ancho * 0.02 if seleccion == 3 else - EI.ancho * 0.05
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
            EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                EI.PANTALLA.blit(fondo1, (0, 0))
            EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))

        #Si se presiona la tecla hacia abajo o "s", entonces el personaje baja
        if (teclas[pygame.K_DOWN] or teclas[pygame.K_s]) and (anterior == "izquierda") and posy_hitbox_derecha < EI.alto * 0.48:
            altura += EI.alto * 0.01
            posy_hitbox_derecha += EI.ancho * 0.0055
            EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
            EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                EI.PANTALLA.blit(fondo1, (0, 0))
            EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))

        #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "derecha" or anterior == None):
            if posy_hitbox_derecha > 0:
                altura -= EI.alto * 0.01
                posy_hitbox_derecha -= EI.ancho * 0.0055
            EI.PANTALLA.blit(quieto_derecha, (velocidad_personaje + EI.ancho * 0.027, altura))
            EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                EI.PANTALLA.blit(fondo1, (0, 0))
            EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
        
        #Si se presiona la tecla hacia arriba o "w", entonces el personaje sube
        if (teclas[pygame.K_UP] or teclas[pygame.K_w]) and (anterior == "izquierda"):
            if posy_hitbox_derecha > 0:
                altura -= EI.alto * 0.01
                posy_hitbox_derecha -= EI.ancho * 0.0055
            EI.PANTALLA.blit(quieto_izquierda, (velocidad_personaje + EI.ancho * 0.04, altura))
            EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
            if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]) or (teclas[pygame.K_LEFT] or teclas[pygame.K_a]):
                EI.PANTALLA.blit(fondo1, (0, 0))
            EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
        
        #Si la tecla derecha está siendo presionada o "d", entonces el personaje camina hacia la derecha
        if (teclas[pygame.K_RIGHT] or teclas[pygame.K_d]):
            EI.PANTALLA.blit(fondo1, (0, 0))
            EI.mostrar_texto("Ataques", "Puedes presionar 'x' y 'z' para atacar:", "Presiona 'Enter' para continuar.", "", int(EI.ancho * 0.03), int(EI.ancho * 0.03))
            EI.PANTALLA.blit(tecla_x, (EI.ancho * 0.6, EI.alto * 0.8))
            EI.PANTALLA.blit(tecla_z, (EI.ancho * 0.7, EI.alto * 0.8))
            if posx_hitbox_derecha < EI.ancho * 0.95:
                velocidad_personaje += EI.ancho * 0.002 
                posx_hitbox_derecha += EI.ancho * 0.002
                posx_hitbox_izquierda += EI.ancho * 0.002
            sumar = EI.ancho * 0.015 if seleccion == 3 else - EI.ancho * 0.04
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

            sumar = EI.ancho * 0.02 if seleccion == 3 else - EI.ancho * 0.05
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
            restar = 0 if seleccion == 3  else EI.ancho * 0.02
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
            restar = 0 if seleccion == 3 else EI.ancho * 0.02
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
elif seleccion == 3:
    quieto_derecha = pygame.transform.scale(quieto_derecha, (EI.ancho * 0.058, EI.alto * 0.088)) #Se adecua el sprite a un tamaño específico
    quieto_izquierda = pygame.transform.scale(quieto_izquierda, (EI.ancho * 0.058, EI.alto * 0.088)) #Se adecua el sprite a un tamaño específico
    #Extraemos los sprites individuales del personaje 3
    sprites_caminar_derecha = EI.cargar_sprites(caminar_derecha, caminar_derecha.get_width()//11, 80, 128)
    sprites_caminar_izquierda = EI.cargar_sprites(caminar_izquierda, caminar_izquierda.get_width()//11, 80, 128)
    sprites_saltar_derecha = EI.cargar_sprites(saltar_derecha, saltar_derecha.get_width()//11, 92, 128)
    sprites_saltar_izquierda = EI.cargar_sprites(saltar_izquierda, saltar_izquierda.get_width()//11, 92, 128)
    sprites_correr_izquierda = EI.cargar_sprites(correr_izquierda, correr_izquierda.get_width()//9, 81, 128)
    sprites_correr_derecha = EI.cargar_sprites(correr_derecha, correr_derecha.get_width()//9, 81, 128)
    sprites_ataque3_derecha = EI.cargar_sprites(ataque3_derecha, ataque3_derecha.get_width()//5, 95, 128)
    sprites_ataque3_izquierda = EI.cargar_sprites(ataque3_izquierda, ataque3_izquierda.get_width()//5, 95, 128)
    sprites_ataque1_derecha = EI.cargar_sprites(ataque1_derecha, ataque1_derecha.get_width()//6, 90, 128)
    sprites_ataque1_izquierda = EI.cargar_sprites(ataque1_izquierda, ataque1_izquierda.get_width()//6, 90, 128)

mapa_avion_ajustado = pygame.transform.scale(EI.mapa_avion, (EI.ancho, EI.alto)) #Ajustamos el mapa al tamaño de la pantalla
EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Mostramos el mapa
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

while True: 
    if anterior == "derecha":
        hitbox = pygame.Rect(posx_hitbox_derecha, posy_hitbox_derecha, EI.ancho * 0.017, EI.alto * 0.0802)
    elif anterior == "izquierda":
        hitbox = pygame.Rect(posx_hitbox_izquierda, posy_hitbox_derecha, EI.ancho * 0.017, EI.alto * 0.0802)


    EI.PANTALLA.blit(mapa_avion_ajustado, (0, 0)) #Se limpia la pantalla

    for evento in pygame.event.get():

        if evento.type == pygame.KEYDOWN:
            #Si se presiona la tecla "Esc", entonces se sale del juego
            if evento.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            #Si se presiona la tecla "espacio", entonces el personaje salta
            if evento.key == pygame.K_SPACE:
                saltando = True
            #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1
            if evento.key == pygame.K_x:
                ataque1 = True
            #Si se presiona la tecla "z", entonces el personaje realiza el ataque 3
            if evento.key == pygame.K_z:
                ataque3 = True
        
            
    #Si se presiona la tecla "x", entonces el personaje realiza el ataque 1         
    if ataque1 and (anterior == "derecha" or anterior == None):
        restar = 0 if seleccion == 3  else EI.ancho * 0.02
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
        restar = 0 if seleccion == 3 else EI.ancho * 0.02
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

        sumar = EI.ancho * 0.015 if seleccion == 3 else 0
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
        sumar = EI.ancho * 0.02 if seleccion == 3 else 0
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
    
    
    

    
    pygame.display.update()
    
