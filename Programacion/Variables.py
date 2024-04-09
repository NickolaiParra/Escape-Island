import pygame

pygame.init()

#Configuración pendiente para conectar al módulo principal.
informacion_pantalla = pygame.display.Info()
ancho = informacion_pantalla.current_w
alto = informacion_pantalla.current_h
screen = pygame.display.set_mode((ancho, alto))
fullscreen = True

running = True

while running:
    screen.fill((0,0,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE and fullscreen:
                fullscreen = False
                pygame.quit()
                pygame.init()
                screen = pygame.display.set_mode((ancho - (ancho * 0.1), alto - (0.2 * alto)))
            elif event.key == pygame.K_f and not fullscreen:
                fullscreen = True
                pygame.quit()
                pygame.init()
                screen = pygame.display.set_mode((ancho, alto))
    
    pygame.display.update()
    

    
    
pygame.quit()