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

fuente_dialog = "Fuentes/Monofonto.ttf"

while running:
    #fondo
    EI.PANTALLA.fill((0,0,0))
    EI.PANTALLA.blit(fondo_selva,fondo_selva_rect)

    #Dialogos
    if num_dialog==-1:
        EI.mostrar_texto("Escape Island","Llegando a la Selva de funciones.",color=EI.ROJO)
    elif num_dialog == 0:
        t1 = "Tu camino te lleva por una peligrosa selva."
        t2 = "Vas con cuidado para no ser comido por ningún animal."
        EI.mostrar_texto("Selva de funciones",t1,t2,color=EI.MORADO)
    elif num_dialog == 1:
        EI.mostrar_texto("Selva de funciones","¡Te enredas en una telarana gigante!",color=EI.MORADO)
    elif num_dialog == 2:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "???"
        EI.mostrar_texto(personaje, "Por fin, algo de comida.")
    elif num_dialog == 3:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Ah, pero si es un humano."
        t2 = "¿Qué te trae a esta selva?"
        t3 = "Soy Funci."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 4:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Vienes del Bosque de ciclos?"
        t2 = "Parece que quieres salir de la isla."
        t3 = "Para hacerlo, necesitarás más conocimiento del que tienes ahora..."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 5:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Para tu suerte, cicloso me cae bien. Siempre me trae comida."
        t2 = "Dale gracias a él, porque te voy a dar una oportunidad."
        t3 = "Para comenzar, voy a enseñarte sobre mi especialidad: las funciones..."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 6:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Primero, revisaremos las funciones en el cálculo, y luego"
        t2 = "veremos funciones en programación."
        t3 = "Bueno, iniciemos..."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 7:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Las funciones son uno de los pilares que debes conocer para el cálculo."
        t2 = "Una funcion se puede definir como una relación entre magnitudes."
        t3 = "Y una magnitud es función de otra si el valor de la primera depende del valor de la segunda."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 8:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Por ejemplo, el área (A) de un circulo es función de su radio (r)."
        t2 = "El valor del área de un círculo es proporcinal al cuadrado del radio:"
        t3 = "A = πr²"
        EI.mostrar_texto(personaje,t1,t2,t3,fuente_dialog_t3=fuente_dialog)
    elif num_dialog == 9:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "En análisis matemático, una función se define como"
        t2 = "una regla de correspondencia que asigna a cada elemento de un primer"
        t3 = "conjunto (dominio) un único elemento de un segundo conjunto (rango)."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 10:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Ahora vamos a abordar los principales tipos de funciones, las cuales son:"
        t2 = "Funciones lineales:"
        t3 = "Son funciones polinómicas de primer grado, es decir, se representan como una línea recta."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 11:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "La expresion general para las funciones lineales es:"
        t2 = "y = mx + b"
        t3 = "Ejemplos: y=12, y=45x, y=x+8, y=19"
        EI.mostrar_texto(personaje,t1,t2,t3,fuente_dialog_t2=fuente_dialog, fuente_dialog_t3=fuente_dialog)
    elif num_dialog == 12:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones cuadráticas:"
        t2 = "Su expresión general es y = ax² + bx + c, con a ≠ 0"
        t3 = "Ejemplos: y = x²+9, y=5+x², t=3s²+s+1"
        EI.mostrar_texto(personaje,t1,t2,t3,fuente_dialog_t2=fuente_dialog, fuente_dialog_t3=fuente_dialog)
    elif num_dialog == 13:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones con valor absoluto:"
        t2 = "La función valor absoluto (|x|) se define a trozos: x si x >= 0 y -x si x < 0"
        t3 = "Ejemplos: y=|x+1|, t=x|x+3|, y=|x²+23|"
        EI.mostrar_texto(personaje,t1,t2,t3,fuente_dialog_t3=fuente_dialog,fuente_dialog_t2=fuente_dialog)
    elif num_dialog == 14:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones racionales:"
        t2 = "Son cocientes de dos polinomios (f(x)/g(x)), donde el denominador es diferente de 0."
        t3 = "Ejemplos: y=2x+3/5+x², y=-3x³-x/x²+4"
        EI.mostrar_texto(personaje,t1,t2,t3,fuente_dialog_t3=fuente_dialog,fuente_dialog_t2=fuente_dialog)
    elif num_dialog == 15:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones radicales:"
        t2 = "Son las que vienen expresadas mediante un radical."
        t3 = "La expresión general de estas funciones es: y=c·√(ax+b)"
        EI.mostrar_texto(personaje,t1,t2,t3,fuente_dialog_t3=fuente_dialog,fuente_dialog_t2=fuente_dialog)
    elif num_dialog == 16:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ejemplos: √(3x), 32√(x), √(12/x) "
        EI.mostrar_texto(personaje,t1,fuente_dialog_t1=fuente_dialog) 
    elif num_dialog == 17:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones exponenciales:"
        t2 = "Son las que tienen por ecuación y = a**(bx)"
        t3 = "Siendo la base (a) un número real positivo, distinto de cero."
        EI.mostrar_texto(personaje,t1,t2,t3,fuente_dialog_t3=fuente_dialog,fuente_dialog_t2=fuente_dialog)
    elif num_dialog == 18:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones logarítmicas:"
        t2 = "Funciones del tipo y = log en base 'a' de (x). Son la inversa de la función exponencial."
        t3 = "Ejemplos: log₃(x+1), ln(x)"
        EI.mostrar_texto(personaje,t1,t2,t3,fuente_dialog_t3=fuente_dialog,fuente_dialog_t2=fuente_dialog)  
    elif num_dialog == 19:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Funciones trigonométricas:"
        t2 = "Funciones asociadas a una razón trigonométrica (sen, cos, tan...)"
        t3 = "Ejemplos: y=sen(x), t=cos(s), y=x·tan(x)"
        EI.mostrar_texto(personaje,t1,t2,t3,fuente_dialog_t3=fuente_dialog,fuente_dialog_t2=fuente_dialog)   
    elif num_dialog ==20:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Ahora te haré una pequeña prueba para verificar que hayas entendido."
        t2 = "Empecemos."
        EI.mostrar_texto(personaje,t1,t2)
#Primera prueba
    elif num_dialog == 21:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cuál de las siguientes funciones es trigonométrica?"
        t2 = ""
        t3 = ""
        a = "y=x"
        b = "t=43s/3"
        c = "y=4sen(57x)"
        d = "t=4"
        EI.pregunta("Prueba de funciones (Cálculo)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 22:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cuál de las siguientes funciones es lineal?"
        t2 = ""
        t3 = ""
        a = "y=2x+45"
        b = "t=1/2x"
        c = "y=8sen(4x)"
        d = "t=|x²|"
        EI.pregunta("Prueba de funciones (Cálculo)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 23:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cuál de las siguientes afirmaciones es falsa?"
        t2 = ""
        t3 = ""
        a = "Una función se puede definir como una relación entre magnitudes."
        b = "En las funciones racionales el denominador no puede ser 0."
        c = "Las funciones de valor absoluto se definen a trozos."
        d = "x² es una función exponencial."
        EI.pregunta("Prueba de funciones (Cálculo)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 24:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿A qué tipo de funciones corresponde la siguiente definición?:"
        t3 = ""
        t2 = "\"Son funciones polinómicas de primer grado, es decir, se representan como una línea recta\"."
        a = "Funciones trigonométricas"
        b = "Funciones de valor absoluto"
        c = "Funciones cuadráticas"
        d = "Funciones lineales"
        EI.pregunta("Prueba de Funciones (Cálculo)",[t1,t2,t3],a,b,c,d)
    elif num_dialog ==-200: #Si no acierta
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Ey, respuesta incorrecta."
        t2 = "Si te sigues equivocando, te voy a comer."
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 25: #Si responde bien
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Bien hecho."
        t2 = "Me sorprende lo rapido que aprendes."
        EI.mostrar_texto(personaje,t1,t2)
    elif num_dialog == 26:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Al parecer no tendré cena hoy."
        t2 = "Pero todavía falta mucho para que te deje ir..."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 27:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ahora te voy a introducir a otro tipo de funciones."
        t2 = "Funciones en programación."
        t3 = "Este tipo de funciones está estrechamente relacionada con las matemáticas."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 28:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Una función en programación es un bloque de código que realiza alguna operación."
        t2 = "Puedes imaginar una función como una pequeña máquina, que toma"
        t3 = "ciertos datos (argumentos), realiza una operación y devuelve un resultado."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 29:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "El primer paso es declararla usando \"def\","
        t2 = "seguido de un nombre descriptivo para la función."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)    
    elif num_dialog == 30:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "El segundo paso es definir los parámetros."
        t2 = "Entre paréntesis debes especificar las entradas de la función."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 31:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "El tercer paso es escribir el cuerpo de la función:"
        t2 = "Es decir, defines todas las instrucciones que la función va a llevar a cabo."
        t3 = "Además, recuerda que el cuerpo de la función debe estar indentado."
        EI.mostrar_texto(personaje,t1,t2,t3) 
    elif num_dialog == 32:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "El cuarto paso es especificar los datos que la función"
        t2 = "va a retornar al final de su ejecución."
        t3 = "Para ello, debes usar \"return\"."
        EI.mostrar_texto(personaje,t1,t2,t3) 
    elif num_dialog == 33:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ten en cuenta que no todas las funciones retornan algún valor."
        t2 = "Así mismo, no todas las funciones necesitan declarar parámetros."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3) 
    elif num_dialog == 34:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Utilizar funciones hace que el código quede mucho"
        t2 = "más limpio, fácil de entender y organizado."
        t3 = "Veamos un ejemplo."
        EI.mostrar_texto(personaje,t1,t2,t3)  
    elif num_dialog == 35:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Primero, definimos la función:"
        t2 = "def saludar(nombre): "
        t3 = '   return "¡Hola, " + nombre + "!"'
        EI.mostrar_texto(personaje,t1,t2,t3)  
    elif num_dialog == 36:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Y ahora llamamos a la función:"
        t2 = 'mensaje = saludar("Funci") '
        t3 = "print(mensaje) -> '¡Hola, Funci!'"
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 37:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "En el ejemplo anterior la función toma un argumento (nombre)"
        t2 = "y devuelve un saludo personalizado."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 38:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Ahora veremos las 3 ventajas de utilizar funciones:"
        t2 = "Modularidad, reutilización de código y legibilidad."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 39:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Modularidad:"
        t2 = "Las funciones nos permiten dividir el código en módulos más"
        t3 = "pequeños y mucho más manejables."
        EI.mostrar_texto(personaje,t1,t2,t3)    
    elif num_dialog == 40:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Reutilización de código:"
        t2 = "Despues de definida una función, la puedes usar posteriormente"
        t3 = "cuantas veces quieras en tu código."
        EI.mostrar_texto(personaje,t1,t2,t3) 
    elif num_dialog == 41:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t1 = "Legibilidad:"
        t2 = "Al definir las funciones con nombres descriptivos, tu código se vuelve"
        t3 = "mucho más legible y comprensible."
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 42:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "funci"
        t3 = ""
        t1 = "Ahora, pondré a prueba tu conocimiento con otra examen."
        t2 = "Comencemos: "
        EI.mostrar_texto(personaje,t1,t2,t3)       
    elif num_dialog == 43:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cuántos pasos (generalmente) se deben cumplir al"
        t2 = "momento de declarar una función?"
        t3 = ""
        a = "2"
        b = "3"
        c = "6"
        d = "4"
        EI.pregunta("Prueba de funciones (Programación)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 44:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Según lo que te enseñé, cuál es el primer paso para "
        t2 = "declarar una funcion?"
        t3 = ""
        a = "Definir la función."
        b = "Declarar los parámetros."
        c = "Especificar el retorno y su tipo."
        d = "Escribir el cuerpo de la función."
        EI.pregunta("Prueba de funciones (Programación)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 45:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cuáles son las 3 principales ventajas de utilizar "
        t2 = "funciones en tu código?"
        a = " Rapidez, optimización, velocidad."
        b = " Optimización, legibilidad, estética."
        c = " Estabilidad, reutilización, parametrización."
        d = " Modularidad, reutilización de código, legibilidad."
        EI.pregunta("Prueba de funciones (Programación)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 46:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "¿Cuál de las siguientes afirmaciones es falsa?"
        t2 = ""
        t3 = ""
        a = " Una función es un bloque de código que realiza alguna operación."
        b = " Las funciones ayudan a que el código sea más comprensible."
        c = " Las funciones permiten la reutilización de código."
        d = " Todas las funciones necesitan retornar y recibir parametros."
        EI.pregunta("Prueba de funciones (Programación)",[t1,t2,t3],a,b,c,d)
    elif num_dialog == 47:
        EI.PANTALLA.blit(funci,funci_rect)
        personaje = "Funci"
        t1 = "Bien hecho, superaste mis expectativas."
        t2 = "Ahora cumpliré con mi promesa, te dejaré ir."
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3)
    elif num_dialog == 48:
        personaje = "Selva de funciones"
        t1 = "Sales de la Selva de funciones cubierto de trozos de telaraña, pero con vida..."
        t2 = ""
        t3 = ""
        EI.mostrar_texto(personaje,t1,t2,t3,color=EI.MORADO)        
    
   
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
    pygame.display.update()
    

pygame.quit()