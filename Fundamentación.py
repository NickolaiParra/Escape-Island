import random

def explain_addition():
    print("\n--- Suma ---")
    print("La suma consiste en añadir dos números para obtener su total.")
    print("Por ejemplo, 3 + 2 = 5\n")

def explain_subtraction():
    print("\n--- Resta ---")
    print("La resta consiste en quitar un número de otro para obtener la diferencia.")
    print("Por ejemplo, 5 - 2 = 3\n")

def explain_multiplication():
    print("\n--- Multiplicación ---")
    print("La multiplicación consiste en añadir un número a sí mismo varias veces.")
    print("Por ejemplo, 3 * 2 = 6\n")

def explain_division():
    print("\n--- División ---")
    print("La división consiste en dividir un número en partes iguales.")
    print("Por ejemplo, 6 / 2 = 3\n")

def generate_question(operation):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    if operation == '+':
        correct_answer = num1 + num2
        question = f"¿Cuánto es {num1} + {num2}?"
    elif operation == '-':
        correct_answer = num1 - num2
        question = f"¿Cuánto es {num1} - {num2}?"
    elif operation == '*':
        correct_answer = num1 * num2
        question = f"¿Cuánto es {num1} * {num2}?"
    elif operation == '/':
        correct_answer = round(num1 / num2, 1)
        question = f"¿Cuánto es {num1} / {num2}? Si el resultado no es entero, entonces escribe una cifra decimal."
    
    return question, correct_answer

def practice_operation(operation):
    score = 0
    for _ in range(5):
        question, correct_answer = generate_question(operation)
        print(question)
        
        while True:
            try:
                user_answer = float(input("Tu respuesta: "))
                break
            except ValueError:
                print("Por favor, ingresa un número válido.")
        
        if user_answer == correct_answer:
            print("¡Correcto!")
            score += 1
        else:
            print(f"Incorrecto. La respuesta correcta es {correct_answer}.")

    print(f"Tu puntuación es: {score}/5")

def main():
    print("¡Bienvenido al tutorial de matemáticas!")
    while True:
        print("\n¿Qué operación te gustaría aprender o practicar?")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")
        choice = input("Selecciona una opción (1-5): ")

        if choice == '1':
            explain_addition()
            practice_operation('+')
        elif choice == '2':
            explain_subtraction()
            practice_operation('-')
        elif choice == '3':
            explain_multiplication()
            practice_operation('*')
        elif choice == '4':
            explain_division()
            practice_operation('/')
        elif choice == '5':
            print("¡Gracias por jugar! ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción entre 1 y 5.")

if __name__ == "__main__":
    main()
