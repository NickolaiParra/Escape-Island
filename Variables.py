import pygame

pygame.init()

BLACK = (0,0,0)

#Configuración pendiente para conectar al módulo principal.
informacion_pantalla = pygame.display.Info()
ancho = informacion_pantalla.current_w
alto = informacion_pantalla.current_h
screen = pygame.display.set_mode((ancho, alto))
fuente_dialog = pygame.font.Font("Fuentes/Fortune.otf",30)

#Booleanos
fullscreen = True
running = True
show_dialog = True

#Rects
dialframe = pygame.image.load("Imagenes/Sprites/dialogo.png").convert()
dialframe = pygame.transform.scale(dialframe,(ancho, 0.3*alto))
dialframe_rect = dialframe.get_rect()
dialframe_rect.bottomleft = (0,alto)

dialog_text = fuente_dialog.render("Hola",True,BLACK)
dialog_text_rect = dialog_text.get_rect()
dialog_text_rect.topright = (ancho * 0.1,alto* 0.75)

num_dialog = 0


def show_text(texto):
    screen.blit(dialframe,dialframe_rect)
    dialog_text = fuente_dialog.render(texto,True,BLACK)
    screen.blit(dialog_text,dialog_text_rect)

while running:
    #Fondo
    screen.fill((190,220,255))
    
    #Diálogos
    if show_dialog and num_dialog == 1:
        show_text("Hola")
    elif show_dialog and num_dialog == 2:
        show_text("Me gusta este diálogo")
    elif show_dialog and num_dialog == 3:
        show_text("Aquí va un texto un poquito más largo porque quiero probar a ver que pasa")
    
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
                dialframe = pygame.transform.scale(dialframe,(ancho - (ancho * 0.1), 0.3*(alto - (0.2 * alto))))
                dialframe_rect = dialframe.get_rect()
                dialframe_rect.bottomleft = (0,alto - (0.2 * alto))
                fuente_dialog = pygame.font.Font("Fuentes/Fortune.otf",30)
                dialog_text = fuente_dialog.render("Hola",True,BLACK)
                dialog_text_rect = dialog_text.get_rect()
                dialog_text_rect.topright = ((ancho - (ancho * 0.1)) * 0.1,(alto - (0.2 * alto))* 0.75)
            elif event.key == pygame.K_f and not fullscreen:
                #Entrar a pantalla completa
                fullscreen = True
                pygame.quit()
                pygame.init()
                screen = pygame.display.set_mode((ancho, alto))
                dialframe = pygame.transform.scale(dialframe,(ancho, 0.3*alto))
                dialframe_rect = dialframe.get_rect()
                dialframe_rect.bottomleft = (0,alto)
                fuente_dialog = pygame.font.Font("Fuentes/Fortune.otf",30)
                dialog_text = fuente_dialog.render("Hola",True,BLACK)
                dialog_text_rect = dialog_text.get_rect()
                dialog_text_rect.topright = (ancho * 0.1,alto* 0.75)
            elif event.key == pygame.K_z and show_dialog:
                #Avanzar el diálogo
                num_dialog += 1
            elif event.key == pygame.K_m:
                #Activar/Desactivar diálogos
                if show_dialog:
                    show_dialog = False
                else:
                    show_dialog = True
    
    pygame.display.update()
    

pygame.quit()