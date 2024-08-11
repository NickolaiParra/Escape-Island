import pygame
import sys

pygame.init()
from Módulos import Escape_Island as EI

#Booleans
running= True
dialog_continue = True

num_dialog = -1

#personajes

funci= pygame.transform.scale(EI.funci,(EI.ancho*0.2,EI.alto*0.3))
funci_rect = funci.get_rect()
funci_rect.bottomleft = (EI.ancho*0.01,EI.alto*0.7)

#Fondos
fondo_selva = pygame.transform.scale(EI.fondo_selva,(EI.ancho*0.8,EI.alto*0.7))
fondo_selva_rect = fondo_selva.get_rect()
fondo_selva_rect.midtop = (EI.ancho//2, 0)


#cajas
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
#Funcion para las preguntas
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

while running:
    #fondo
    EI.PANTALLA.fill((0,0,0))
    EI.PANTALLA.blit(fondo_selva,fondo_selva_rect)

    #Dialogos
    if num_dialog==-1:
        EI.mostrar_texto("Escape Island","Llegando a la selva de las Funciones",color=EI.ROJO)
    elif num_dialog == 0:
        t1 = "Tu camino te lleva por una Peligrosa selva."
        t2 = "Vas con cuidado para no ser comido por ningun animal."
        EI.mostrar_texto("Selva de las Funciones",t1,t2,color=EI.MORADO)
    elif num_dialog == 1:
        EI.mostrar_texto("selva de las funciones","Hasta que te enredas en una telarana gigante",color=EI.MORADO)
    elif num_dialog == 2:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "???"
        EI.mostrar_texto(personaje, "Por fin, algo de comida :)")
    elif num_dialog == 3:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Ah, pero si es un humano"
        t2 = "Que te trae a esta Selva?"
        t3 = "Soy Funci"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 4:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Vienes de la cueva de las condicionales?"
        t2 = "Parece que quieres salir de la Isla"
        t3 = "Para hacerlo necesitaras mas conocimiento del que tienes ahora..."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 5:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Condi"
        t1 = "Por suerte Me cae muy bien condi, siempre me trae comida :3"
        t2 = "Dale gracias a él, te voy a dar una oportunidad"
        t3 = "Primero te voy a enseñar sobre mi especialidad, las funciones..."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 6:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Primero, revisaremos las Funciones en el cálculo, y luego"
        t2 = "veremos funciones en programación"
        t3 = "Bueno, Empecemos..."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 7:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Las funciones son uno de los pilares que debes conocer para el cálculo"
        t2 = "Una funcion se puede definir como una relacion entre magnitudes"
        t3 = "Y una magnitud es FUNCION de otra si el valor de la primera depende del valor de la segunda"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 8:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Por ejemplo, el área A de un circulo es función de su radio r"
        t2 = "El valor del área A de un circulo es proporcinal al cuadrado del Radio:"
        t3 = "A = π·r^2"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 9:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Otra definición en análisis matemático, el concepto general de función, se "
        t2 = "refiere a una regla que asigna a cada elemento de un primer"
        t3 = "conjunto un único elemento de un segundo conjunto."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 10:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Ahora vamos con los tipos de funciones en el cálculo, las cuales son:"
        t2 = "Funcion Lineal:"
        t3 = "Son funciones polinómicas de primer grado, es decir, se representa como una linea recta"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 11:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "La expresion general para las funciones lineales es:"
        t2 = "y=mx+n"
        t3 = "ejemplos: y=12 , y=45x , y=x+8 , t= 19"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 12:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ahora con las funciones cuadraticas"
        t2 = "Su expresión general es y=ax² + bx + c, con a=!0"
        t3 = "Ejemplos: y= x²+9 , y= 5+x² , t= 3s²+s+1"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 13:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ahora funciones con valor absoluto"
        t2 = "Son cualquier funcion que contenga una expresión de valor absoluto"
        t3 = "Ejemplos: y=|x+1| , t=x|x+3| , y=|x²+23|"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 14:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones de proporcionalidad inversa"
        t2 = "Son funciones que relacionan las magnitudes inversamente y su expresión general es: y=k/x"
        t3 = "Ejemplos: y=-1/x , y=-1/3x , y=1/x , t= 3/s"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 15:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones Radicales"
        t2 = "Son las que vienen expresadas mediante un radical"
        t3 = "La formula general de estas funciones es: y=c·sqrt(ax+b)"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 16:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ejemplos: sqrt(3x) , 32·sqrt(x) , sqrt(12/x) "
        EI.mostrar_texto(personaje,t1) 
    elif num_dialog == 17:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones Exponenciales "
        t2 = "Son las que tienen la ecuación y=a**(bx)"
        t3 = "Siendo la base 'a' un numero real positivo, distinto de cero"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 18:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones Logaritmicas"
        t2 = "Funciones del tipo y=log a(x) y son la inversa de la funcion exponencial"
        t3 = "Ejemplos: log 3(x+1), ln(x), log 12(x)"
        EI.mostrar_texto(personaje,t1,t2,t3)  
    elif num_dialog == 19:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones Trigonometricas"
        t2 = "Funciones asociadas a una razón trigonometrica"
        t3 = "Ejemplos: y=Sen(x), t=cos(s), y=x·tan(x)"
        EI.mostrar_texto(personaje,t1,t2,t3)   
    elif num_dialog ==20:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Ahora te haré una pequeña prueba para verificar que hayas entendido"
        t2 = "Empecemos"
        EI.mostrar_texto(personaje,t1,t2)
#Primera prueba
    elif num_dialog == 21:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cual de las siguientes funciones es trigonometrica?"
        t2 = ""
        t3 = ""
        a = "y=x"
        b = "t=43s/3"
        c = "y=4sen(57x)"
        d = "t = 4"
        pregunta("Prueba de Funciones (Cálculo)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 22:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cual de las siguientes funciones es Lineal?"
        t2 = ""
        t3 = ""
        a = "y=2x+45"
        b = "t=1/2x"
        c = "y=8sen(4x)"
        d = "t = 12"
        pregunta("Prueba de Funciones (Cálculo)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 23:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cual de las siguientes afirmaciones es falsa?"
        t2 = ""
        t3 = ""
        a = "Una función se puede definir como una relación entre magnitudes"
        b = "En las funciones de proporcionalidad inversa la X y la Y cambian de lugar"
        c = "y = 1/x, es una función de proporcionalidad inversa"
        d = "x**2 es una función exponencial"
        pregunta("Prueba de Funciones (Cálculo)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 24:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿A que tipo de funciones corresponde la siguiente definición:?"
        t2 = "Son funciones polinómicas de primer grado, es decir, se representa como una linea recta"
        t3 = ""
        a = "Funciones Trigonométricas"
        b = "Funciones de valor absoluto"
        c = "Funciones rectas"
        d = "Funciones Lineales"
        pregunta("Prueba de Funciones (Cálculo)",[t1,t2,t3],a,b,c,d)
    elif num_dialog ==-200: #Si no acierta
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Ey, Mala respuesta"
        t2 = "Si te sigues equivocando, te voy a comer"
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 25: # Si responde bien
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Bien Hecho"
        t2 = "Me sorprende lo rapido que aprendes :)"
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 26:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Al parecer no tendré cena hoy"
        t2 = "Pero todavia falta mucho para que te deje ir..."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 27:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ahora te voy a introducir a otro tipo de funciones"
        t2 = "Funciones en programación..."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 28:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Una función en programación es un bloque de código que realiza alguna operacion "
        t2 = "Puedes imaginar una función como una pequeña maquina, que toma "
        t3 = "ciertos datos(argumentos), realiza una operacion y devuelve un resultado"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 29:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Utilizar funciones, hace que el código quede mucho"
        t2 = "más limpio, fácil de entender y organizado"
        t3 = "Veamos un Ejemplo"
        EI.mostrar_texto(personaje,t1,t2,t3)  
    elif num_dialog == 30:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "PRIMERO DEFINIMOS LA FUNCION..."
        t2 = "def saludar(nombre): "
        t3 = '   return "¡Hola, " + nombre + "!"'
        EI.mostrar_texto(personaje,t1,t2,t3)  
    elif num_dialog == 31:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Y AHORA LA LLAMAMOS..."
        t2 = 'mensaje = saludar("Funci") '
        t3 = "print(mensaje)"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 32:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "En el ejemplo anterior la función toma un argumento(nombre)"
        t2 = "y devuelve un saludo personalizado"
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 33:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ahora veremos las 3 ventajas de utilizar funciones..."
        t2 = "Modularidad, Reutilización de código y legibilidad"
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 34:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "MODULARIDAD"
        t2 = "Las funciones nos permiten dividir el código en módulos más"
        t3 = "pequeños y mucho más manejables."
        EI.mostrar_texto(personaje,t1,t2,t3)    
    elif num_dialog == 35:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "REUTILIZACIÓN DE CÓDIGO"
        t2 = "Despues de definida una función, la puedes usar posteriormente"
        t3 = "cuantas veces quieras en tu código"
        EI.mostrar_texto(personaje,t1,t2,t3) 
    elif num_dialog == 36:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "LEGIBILIDAD"
        t2 = "Al definir las funciones con nombres descriptivos, tu código se vuelve"
        t3 = "mucho más legible y comprensible"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 37:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ahora te daré los pasos que generalmente se deben tomar cuando "
        t2 = "quieras declarar una función"
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 38:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "El primer paso es definirla:"
        t2 = "Define la tarea que debe realizar la función"
        t3 = "y ponle un nombre descriptivo que indique que hace la función"
        EI.mostrar_texto(personaje,t1,t2,t3)    
    elif num_dialog == 39:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "El segundo paso es declarar los parámetros:"
        t2 = "Si la función necesita información para realizar su trabajo"
        t3 = "especifica los parámetros que la función aceptará"
        EI.mostrar_texto(personaje,t1,t2,t3) 
    elif num_dialog == 40:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "El tercer paso es especificar los datos que la función"
        t2 = "va a retornar al final de su ejecución"
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3) 
    elif num_dialog == 41:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ten en cuenta que no todas las funciones retornan algún valor"
        t2 = "Asímismo, no todas las funciones necesitan declarar parametros"
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3) 
    elif num_dialog == 42:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ahora, el cuarto paso es Escribir el cuerpo de la función:"
        t2 = "Defines todas las instrucciones, lógica y cálculos "
        t3 = "necesarios para la tarea que la función lleva a cabo"
        EI.mostrar_texto(personaje,t1,t2,t3) 
    elif num_dialog == 43:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ahora te mostraré un ejemplo de la correcta utilizacion"
        t2 = "de lo que te acabo de enseñar, cada linea tiene en frente"
        t3 = "los pasos que está cumpliendo: "
        EI.mostrar_texto(personaje,t1,t2,t3) 
    elif num_dialog == 44:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "def sumarnumeros(num1,num2):    /#1 y #2"
        t2 = "    suma = num1 +num2                 / #4 "
        t3 = "    return suma                    / #3"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 45:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Con lo que te he enseñado sobre estas funciones"
        t2 = "pondré a prueba tu conocimiento con otra exámen"
        t3 = "Comencemos: "
        EI.mostrar_texto(personaje,t1,t2,t3)       
    elif num_dialog == 46:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cuantos pasos (generalmente) se deben cumplir al"
        t2 = "momento de declarar una función?"
        t3 = ""
        a = "2"
        b = "3"
        c = "6"
        d = "4"
        pregunta(" Prueba de Funciones (Programación)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 47:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Según lo que te enseñé, cual es el primer paso para "
        t2 = "  declarar una funcion?"
        t3 = ""
        a = "Definir la función"
        b = "Declarar los parámetros"
        c = "Especificar el retorno y su tipo"
        d = "Escribir el cuerpo de la función"
        pregunta(" Prueba de Funciones (Programación)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 48:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cuales son las 3 principales ventajas de utilizar "
        t2 = "funciones en tu código según lo que vimos?"
        a = " Rapidez,optimización, velocidad"
        b = " Optimización, Legibilidad, Hacer que el código se vea más bonito"
        c = " Estabilidad, reutilización, Parametrización"
        d = " Modularidad, Reutilización de código, legibilidad "
        pregunta(" Prueba de Funciones (Programación)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 49:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cual de las siguientes afirmaciones es falsa?"
        t2 = ""
        t3 = ""
        a = " Una función es un bloque de código que realiza alguna operacion"
        b = " Las funciónes ayudan a que el código sea más comprensible"
        c = " Las funciones ayudan en la reutlización de código"
        d = " Todas las funciones necesitan retornar y recibir parametros"
        pregunta(" Prueba de Funciones (Programación)",[t1,t2,t3],a,b,c,d)
    elif num_dialog ==50:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Bien hecho, superaste mis expectativas"
        t2 = "Ahora cumpliré con mi promesa, te dejaré ir"
        t3 = "Al cabo que ni hambre tenía UnU"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog ==51:
        personaje = "Selva de las funciones"
        t1 = "Sales de la selva de las funciones "
        t2 = "cubierto de trozos de telaraña, pero con vida..."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3,color=EI.MORADO)        
    
   
#eventosss
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