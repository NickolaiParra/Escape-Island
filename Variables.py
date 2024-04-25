import pygame

pygame.init()

BLACK = (0,0,0)
ORANGE = (255,100,0)

#Configuración pendiente para conectar al módulo principal.
informacion_pantalla = pygame.display.Info()
ancho = informacion_pantalla.current_w
alto = informacion_pantalla.current_h
screen = pygame.display.set_mode((ancho, alto))
fuente_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf",35)
personaje_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf",40)
personaje_dialog.set_bold(True)

#Booleanos
fullscreen = True
running = True
dialog_active = False

#Rects de diálogos
dialframe = pygame.image.load("Imagenes/Sprites/dialogo.png").convert()
dialframe = pygame.transform.scale(dialframe,(ancho, 0.3*alto))
dialframe_rect = dialframe.get_rect()
dialframe_rect.bottomleft = (0,alto)

dialog_char = personaje_dialog.render("Hola",True,BLACK)
dialog_char_rect = dialog_char.get_rect()
dialog_char_rect.topright = (ancho * 0.1,alto* 0.74)
dialog_text1 = fuente_dialog.render("Hola",True,BLACK)
dialog_text_rect1 = dialog_text1.get_rect()
dialog_text_rect1.topright = (ancho * 0.1,alto* 0.80)
dialog_text2 = fuente_dialog.render("Hola",True,BLACK)
dialog_text_rect2 = dialog_text1.get_rect()
dialog_text_rect2.topright = (ancho * 0.1,alto* 0.85)
dialog_text3 = fuente_dialog.render("Hola",True,BLACK)
dialog_text_rect3 = dialog_text1.get_rect()
dialog_text_rect3.topright = (ancho * 0.1,alto* 0.90)


num_dialog = 0

#función para mostrar los diálogos
def show_text(personaje,linea1,linea2 = "",linea3 = "",character_color= ORANGE):
    screen.blit(dialframe,dialframe_rect)
    dialog_char = personaje_dialog.render(personaje,True,character_color)
    screen.blit(dialog_char,dialog_char_rect)
    dialog_text1 = fuente_dialog.render(linea1,True,BLACK)
    screen.blit(dialog_text1,dialog_text_rect1)
    dialog_text2 = fuente_dialog.render(linea2,True,BLACK)
    screen.blit(dialog_text2,dialog_text_rect2)
    dialog_text3 = fuente_dialog.render(linea3,True,BLACK)
    screen.blit(dialog_text3,dialog_text_rect3)

#Función para mostrar una pregunta  
def pregunta(pregunta,r1,r2,r3,r4,correcta = 1):
    pass


#While principal
while running:
    #Fondo
    screen.fill((190,220,255))
    
    #Diálogos
    if dialog_active and num_dialog == 1:
        personaje = "Variably"
        show_text(personaje,"Hola.","Bienvenido a la aldea de las variables")
    elif dialog_active and num_dialog == 2:
        show_text(personaje,"Veo que estás perdido", "Déjame ayudarte")
    elif dialog_active and num_dialog == 3:
        show_text(personaje,"Soy el jefe de la aldea de variables", "Mi nombre es Variably")
    elif dialog_active and num_dialog == 4:
        show_text(personaje,"Para progresar por estos lados, necesitas aprender a programar variables", "Pero, ¡no te preocupes!", "Yo te enseñaré")
    elif dialog_active and num_dialog == 5:
        show_text(personaje,"Aquí te explicaremos qué es una variable y cómo se usa","Empecemos por lo básico","¿Te parece?")
    elif dialog_active and num_dialog == 6:
        t1 = "Una variable es como un lugar en el que puedes almacenar cosas"
        t2 = "Esas cosas pueden ser números, cadenas de texto y otros tipos de datos"
        t3 = "Y son muy útiles ya que puedes acceder a esa información cuando la necesites"
        show_text(personaje,t1,t2,t3)
    
    #Eventos    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #Salir del juego
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and fullscreen:
                #Salir de pantalla completa
                fullscreen = False
                pygame.quit()
                pygame.init()
                screen = pygame.display.set_mode((ancho - (ancho * 0.1), alto - (0.2 * alto)))
                #Cambiar el tamaño de los diálogos
                dialframe = pygame.transform.scale(dialframe,(ancho - (ancho * 0.1), 0.3*(alto - (0.2 * alto))))
                dialframe_rect = dialframe.get_rect()
                dialframe_rect.bottomleft = (0,alto - (0.2 * alto))
                fuente_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf",30)
                personaje_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf",40)
                personaje_dialog.set_bold(True)
                dialog_char = personaje_dialog.render("Hola",True,BLACK)
                dialog_char_rect = dialog_char.get_rect()
                dialog_char_rect.topright = ((ancho - (ancho * 0.1)) * 0.1,(alto - (0.2 * alto))* 0.74)
                dialog_text1 = fuente_dialog.render("Hola",True,BLACK)
                dialog_text_rect1 = dialog_text1.get_rect()
                dialog_text_rect1.topright = ((ancho - (ancho * 0.1)) * 0.1,(alto - (0.2 * alto))* 0.80)
                dialog_text2 = fuente_dialog.render("Hola",True,BLACK)
                dialog_text_rect2 = dialog_text2.get_rect()
                dialog_text_rect2.topright = ((ancho - (ancho * 0.1)) * 0.1,(alto - (0.2 * alto))* 0.85)
                dialog_text3 = fuente_dialog.render("Hola",True,BLACK)
                dialog_text_rect3 = dialog_text3.get_rect()
                dialog_text_rect3.topright = ((ancho - (ancho * 0.1)) * 0.1,(alto - (0.2 * alto))* 0.90)
            elif event.key == pygame.K_f and not fullscreen:
                #Entrar a pantalla completa
                fullscreen = True
                pygame.quit()
                pygame.init()
                screen = pygame.display.set_mode((ancho, alto))
                #Cambiar el tamaño de los diálogos
                dialframe = pygame.transform.scale(dialframe,(ancho, 0.3*alto))
                dialframe_rect = dialframe.get_rect()
                dialframe_rect.bottomleft = (0,alto)
                fuente_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf",30)
                personaje_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf",40)
                personaje_dialog.set_bold(True)
                dialog_char = personaje_dialog.render("Hola",True,BLACK)
                dialog_char_rect = dialog_char.get_rect()
                dialog_char_rect.topright = (ancho * 0.1,alto* 0.74)
                dialog_text1 = fuente_dialog.render("Hola",True,BLACK)
                dialog_text_rect1 = dialog_text1.get_rect()
                dialog_text_rect1.topright = (ancho * 0.1,alto* 0.80)
                dialog_text2 = fuente_dialog.render("Hola",True,BLACK)
                dialog_text_rect2 = dialog_text2.get_rect()
                dialog_text_rect2.topright = (ancho * 0.1,alto* 0.85)
                dialog_text3 = fuente_dialog.render("Hola",True,BLACK)
                dialog_text_rect3 = dialog_text3.get_rect()
                dialog_text_rect3.topright = (ancho * 0.1,alto* 0.90)
            elif event.key == pygame.K_z and dialog_active:
                #Avanzar el diálogo
                num_dialog += 1
            elif event.key == pygame.K_m:
                #Activar/Desactivar diálogos
                #Pendiente de cambiar
                if dialog_active:
                    dialog_active = False
                else:
                    dialog_active = True
    
    pygame.time.Clock().tick(60)
    pygame.display.update()
    

pygame.quit()