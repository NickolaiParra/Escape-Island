import pygame
import sys

pygame.init()
from Módulos import Escape_Island as EI

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

#Función para mostrar una pregunta  
def pregunta(titulo,pregunta,r1,r2,r3,r4, tamaño_texto =int(EI.ancho * 0.02),tamaño_titulo =int(EI.ancho * 0.023)):
    l1,l2,l3 = pregunta
    EI.mostrar_texto(titulo,l1,l2,l3,color=EI.ROJO,)
    fuente_dialog = pygame.font.Font("Fuentes/Sedan-Regular.ttf", tamaño_texto)
    fuente_titulo = pygame.font.Font("Fuentes/Sedan-Regular.ttf", tamaño_titulo)
    
    titulo_pregunta = fuente_titulo.render(" Respuestas: ",True,EI.ROJO)
    titulo_pregunta_rect = titulo_pregunta.get_rect()
    titulo_pregunta_rect.topleft =  (EI.ancho * 0.19,EI.alto*0.04)
    pygame.draw.rect(EI.PANTALLA,EI.DORADO_FONDO,titulo_pregunta_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,titulo_pregunta_rect,1)
    EI.PANTALLA.blit(titulo_pregunta,titulo_pregunta_rect)
    
    resp_a = fuente_dialog.render((" a. "+ r1 + " "),True,EI.NEGRO)
    resp_a_rect = resp_a.get_rect()
    resp_a_rect.topleft = (EI.ancho * 0.2,EI.alto*0.1)
    pygame.draw.rect(EI.PANTALLA,EI.AMARILLO_FONDO,resp_a_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_a_rect,1)
    EI.PANTALLA.blit(resp_a,resp_a_rect)
    
    resp_b = fuente_dialog.render((" b. "+ r2 + " "),True,EI.NEGRO)
    resp_b_rect = resp_b.get_rect()
    resp_b_rect.topleft = (EI.ancho * 0.2,EI.alto*0.15)
    pygame.draw.rect(EI.PANTALLA,EI.AMARILLO_FONDO,resp_b_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_b_rect,1)
    EI.PANTALLA.blit(resp_b,resp_b_rect)
    
    resp_c = fuente_dialog.render((" c. "+ r3 + " "),True,EI.NEGRO)
    resp_c_rect = resp_c.get_rect()
    resp_c_rect.topleft = (EI.ancho * 0.2,EI.alto*0.2)
    pygame.draw.rect(EI.PANTALLA,EI.AMARILLO_FONDO,resp_c_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_c_rect,1)
    EI.PANTALLA.blit(resp_c,resp_c_rect)
    
    resp_d = fuente_dialog.render((" d. "+ r4 + " "),True,EI.NEGRO)
    resp_d_rect = resp_d.get_rect()
    resp_d_rect.topleft = (EI.ancho * 0.2,EI.alto*0.25)
    pygame.draw.rect(EI.PANTALLA,EI.AMARILLO_FONDO,resp_d_rect)
    pygame.draw.rect(EI.PANTALLA,EI.NEGRO,resp_d_rect,1)
    EI.PANTALLA.blit(resp_d,resp_d_rect)
    
    EI.PANTALLA.blit(caja_a,caja_a_rect)
    EI.PANTALLA.blit(caja_b,caja_b_rect)
    EI.PANTALLA.blit(caja_c,caja_c_rect)
    EI.PANTALLA.blit(caja_d,caja_d_rect)


#While principal
while running:
    #Fondo
    EI.PANTALLA.fill((0,0,0))
    EI.PANTALLA.blit(fondo_bosque,fondo_bosque_rect)
    
    
    #Diálogos
    if num_dialog == -1:
        EI.mostrar_texto("Escape Island","Llegando al bosque de ciclos.",color=EI.ROJO)
    elif num_dialog == 0:
        t1 = "Haz llegado a un bosque pegajoso."
        t2 = "Te motivas a seguir."
        EI.mostrar_texto("Bosque de ciclos",t1,t2,color=EI.MORADO)
    elif num_dialog == 1:
        t1 = "Al caminar durante un rato notas que el paisaje se empieza a repetir."
        t2 = "Crees que estas caminando en circulos."
        EI.mostrar_texto("Bosque de ciclos",t1,t2,color=EI.MORADO)
    elif num_dialog == 2:
        t1 = "¡Oye!"
        t2 = "!Deja de caminar!"
        t3 = "Así no vas a llegar  a ningún lado."
        EI.mostrar_texto("???",t1,t2)
    elif num_dialog == 3:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        t1 = "¡Hola!"
        t2 = "Yo soy el cicloso."
        t3 = "Habito estas tierras desde su nacimiento."
        EI.mostrar_texto("Cicloso",t1,t2,t3)
    elif num_dialog == 4:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        t1 = "Te puedo sacar de este ciclo infinito"
        t2 = "Pero para ello debes dominar el uso de los ciclos"
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
        t2 = "No te vas a poner a escribir el mismo código esa cantidad de veces ¿O si?"
        t3 = ""
        EI.mostrar_texto("Cicloso",t1,t2,t3)
    elif num_dialog == 8:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        t1 = "No."
        t2 = "Por esa misma razón se usa una herramienta muy poderosa en programacion."
        t3 = "Los ciclos."
        EI.mostrar_texto("Cicloso",t1,t2,t3)
    elif num_dialog == 9:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        t1 = "Estos ciclos te permiten repetir una cantidad de veces cierta parte de tu código."
        t2 = "Así si tienes que hacer una operacíon múltiples veces lo puedes hacer sin necesidad"
        t3 = "de escribir el código cientos de veces."
        EI.mostrar_texto("Cicloso",t1,t2,t3)
    elif num_dialog == 10:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        t1 = "Eso es básicamente lo que hacen los ciclos, su concepto más básico."
        t2 = "Bueno creo que es necesario ver si entendiste,"
        t3 = "ya que es fundamental que lo hagas para seguir adelante."
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
        pregunta("Quiz de ciclos 1",[t1,"",""],a,b,c,d)
        #dialog_continue = False
    elif num_dialog == -100: # Si se equivoca
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Eso está mal."
        t2 = "Vamos a tener que repetirlo."
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 12: # Si responde correctamente
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Perfecto."
        t2 = "¡Continuemos!"
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 13:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Ahora pasaremos a su ejecución en python."
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
        t1 = "Hay dos tipos de ciclos muy importantes y que vas a encontrar en todo lado."
        t2 = "Estos son el 'for' y el 'while'"
        t3 = "¿Cuál es su diferencia?"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 16: 
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "El 'for' se usa cuando necesitas que se repita el código una cantidad de veces específica,"
        t2 = "mientras que el 'while' se ejecuta hasta que una condición que le des no se cumpla,"
        t3 = "por lo que si sabes usar condiciones te sera muy útil para usar los 'while'"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 17:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Ahora, ¿cómo se escriben para que funcione?"
        t2 = "Empecemos por el 'for'."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 18:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "La sintaxis de un 'for' puede ser:"
        t2 = "'for elemento in elementos:'"
        t3 = "ó 'también for numero in range(rango):'"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 19:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "La primera forma de escribirse pasa por todos los elementos que hayan dentro"
        t2 = "de una lista o algo que contenga elementos que se puedan recorrer,"
        t3 = "por ejemplo los caracteres de una palabra."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 20:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Un ejemplo de esto sería:"
        t2 = "'for vocal in \"aeiou\":'"
        t3 = "'    código'"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 21:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Ahí repetiría el código por la cantidad de vocales que hay en \"aeiou\"."
        t2 = "y se guardaría cada vocal por la que pasa en la variable 'vocal'."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 22:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "La  segunda forma en cambio, repite el código por una cantidad de veces, específicada en el"
        t2 = "rango del cíclo. Este rango tiene que ser un número entero."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 23:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Por ejemplo:"
        t2 = "'for i in range(5):' repetiría el código 5 veces, y guardaría el número"
        t3 = " del ciclo en la variable 'i', empezando por 0 y terminando en 4 (en este caso)."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 24:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Algo que es importante notar es que si tienes una variable que contenga un número entero"
        t2 = "puedes usar esa variable como rango para el 'for'."
        t3 = "Algo como: 'for numero in range(numeros)'."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 25:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "En este caso el código se repetiría la cantidad de veces que sea el valor de 'números',"
        t2 = "y en cada repetición (también llamada iteración o ciclo) se guardaría en la variable 'número'"
        t3 = "el número de la repetición desde 0 hasta el valor de 'números' menos 1."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 26:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Así es como funciona el 'for'."
        t2 = "Vamos por buen camino."
        t3 = "Recuerda que puedes regresar  en mi explicación si se te complica algo."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 27:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Ahora pasemos con el 'while'."
        t2 = "Si has llegado hasta aquí asumiré que ya sebes sobre las condiciones."
        t3 = "Es importante que lo reduerdes."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 28:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Bien, si estás listo pasaré a mostrarte la  estructura de un 'while'."
        t2 = "¿Preparado?"
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 29:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "'While \"condición\":'"
        t2 = "'    código'"
        t3 = "Se ve más sencillo que el for ¿no?"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 30:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Básicamente todo lo que este dentro de ese while se va ejecutar mientras se cumpla esa condición."
        t2 = "Para que lo entiendas mejor te diré que lo que hace es que cada ves que inicia un nuevo ciclo"
        t3 = "verifica si se cumple esa condición, y si lo hace se sigue ejecutando."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 31:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Si lo entiendes verás que es muy fácil que acabes en un ciclo infinito, por lo que ten cuidado"
        t2 = "de poner alguna forma de hacer que esa condición se deje de cumplir en algún momento si no"
        t3 = "quieres que se ejecute para siempre."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 32:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "¿Necesitas un ejemplo?"
        t2 = "Dejame pensar..."
        t3 = "Bueno aquí va:"
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
        t1 = "Este código lo que hace es que empieza con el número 1 y verifica si es menor que 10,"
        t2 = "como eso es verdad le suma 1 al número y queda en 2. Luego vuelve a verificar y vuelve a sumar."
        t3 = "Eso ocurre hasta que el número queda en 10."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 35:
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Como 10 no es menor que 10 entonces no le vuelve a sumar nada y el número se queda en 10"
        t2 = "Así puedes usar los ciclos, pero no es la única manera de hacerlo. Tienes que ser creativo"
        t3 = "para crear condiciones que hagan lo que quieras."
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
        t1 = "¿Cuáles son los dos tipos de ciclos que se pueden usar en python?"
        a = "'if' y 'for'"
        b = "'range' y 'for'"
        c = "'if y 'while'"
        d = "'while' y 'for'"
        correcta = 4
        pregunta("Quiz de ciclos 2",[t1,"",""],a,b,c,d)
        #dialog_continue = False
    elif num_dialog == -200: # Si se equivoca
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Eso está mal."
        t2 = "Vamos a tener que repetirlo."
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 38: # Si responde correctamente
        EI.PANTALLA.blit(cicloso,cicloso_rect)
        personaje = "Cicloso"
        t1 = "Vale. Con este conocimiento podrás salir de este bosque"
        t2 = "Recuerda dar lo mejor de ti."
        t3 = "¡Nos vemos!"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 39:
        #Examen de ciclos
        #Pregunta 1
        t1 = "¿Cuál de las siguientes tiene una estructura válida de un 'for' en python?"
        a = "for 'condición':"
        b = "for 'letra' in 'palabra':"
        c = "for 'letra' = 'palabra':"
        d = "for = 'condición'"
        correcta = 4
        pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
    elif num_dialog == 40:
        #Pregunta 2
        t1 = "¿Cuál de las siguientes NO tiene una estructura válida de un 'while' en python?"
        a = "while True:"
        b = "while a > b:"
        c = "while a = b:"
        d = "while a > b and b > c:"
        correcta = 3
        pregunta("Examen de ciclos",[t1,"",""],a,b,c,d)
    elif num_dialog == 41:
        #Pregunta 3
        t1 = "¿Cuántas veces se repite el siguiente 'for'?"
        t2 = "for i in range(10):"
        a = "10"
        b = "9"
        c = "11"
        d = "i"
        correcta = 1
        pregunta("Examen de ciclos",[t1,t2,""],a,b,c,d)
    elif num_dialog == 42:
        #Pregunta 4
        t1 = "¿Cuántas veces se repite el siguiente 'while' si a = 0?"
        t2 = "while a >= 10:"
        t3 = "    a = a + 1"
        a = "10"
        b = "9"
        c = "11"
        d = "0"
        correcta = 1
        pregunta("Examen de ciclos",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 43:
        #Pregunta 5
        t1 = "¿Cuántas veces se repite el siguiente 'while'?"
        t2 = "while (True and ((not False and True) or True)):"
        a = "Ninguna"
        b = "Infinitas"
        c = "1'"
        d = "1000"
        correcta = 2
        pregunta("Examen de ciclos",[t1,t2,""],a,b,c,d)
    elif num_dialog == -300: # Si no pasa
        t1 = "El bosque  te obliga a repetir."
        t2 = "Devuélvete y cumple la condición para salir de este ciclo."
        t3 = ""
        EI.mostrar_texto("Bosque de ciclos",t1,t2,t3,color=EI.MORADO)
        #Vuelve a num_dialog == 13
    elif num_dialog == 44: # Si pasa
        t1 = "Una salida se abre ante ti."
        t2 = "Avanzas y hacia ella."
        t3 = ""
        EI.mostrar_texto("Bosque de ciclos",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 45: 
        t1 = "Has salido del bosque."
        t2 = "Te sientes aliviado de haber salido de ese ciclo infinito."
        t3 = "Ya falta poco."
        EI.mostrar_texto("Bosque de ciclos",t1,t2,t3,color=EI.MORADO)
    elif num_dialog == 46: 
        EI.mostrar_texto("Escape Island","Saliendo del Bosque de ciclos.",color=EI.ROJO)
    
        
        
    else:
        EI.mostrar_texto("","")
    
    #Eventos    
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
    
    pygame.time.Clock().tick(60)
    pygame.display.update()
    

pygame.quit()