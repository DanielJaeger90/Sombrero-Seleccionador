# Ejercicio Sombrero Seleccionador de Hogwarts

# Autor: Daniel Iturralde

# Fecha: 2024/03/24

import random

def hacer_pregunta(pregunta, respuestas):
    print(pregunta)
    for i, respuesta in enumerate(respuestas):
        print(f"{i+1}. {respuesta}")
    seleccion = int(input("Selecciona una respuesta (1-4): "))
    while seleccion < 1 or seleccion > 4:
        seleccion = int(input("Selecciona una respuesta válida (1-4): "))
    return seleccion - 1

def sombrero_seleccionador():
    preguntas = [
        ("¿Qué cualidad valoras más?", ["Valentía", "Astucia", "Lealtad", "Intelecto"]),
        ("¿Qué animal te representa mejor?", ["León", "Serpiente", "Tejón", "Águila"]),
        ("¿Qué haces en tu tiempo libre?", ["Practicar deportes", "Planear estrategias", "Ayudar a otros", "Estudiar"]),
        ("¿Qué tipo de persona admiras?", ["Audaz y valiente", "Astuta y ambiciosa", "Amable y leal", "Inteligente y creativa"]),
        ("¿Qué harías para alcanzar tus metas?", ["Afrontar desafíos", "Utilizar cualquier medio", "Trabajar en equipo", "Investigar y aprender"])
    ]
    
    puntajes = {"Gryffindor": 0, "Slytherin": 0, "Hufflepuff": 0, "Ravenclaw": 0}

    for pregunta, respuestas in preguntas:
        respuesta_seleccionada = hacer_pregunta(pregunta, respuestas)
        if respuesta_seleccionada == 0:  # Gryffindor
            puntajes["Gryffindor"] += 1
        elif respuesta_seleccionada == 1:  # Slytherin
            puntajes["Slytherin"] += 1
        elif respuesta_seleccionada == 2:  # Hufflepuff
            puntajes["Hufflepuff"] += 1
        elif respuesta_seleccionada == 3:  # Ravenclaw
            puntajes["Ravenclaw"] += 1

    casa_seleccionada = max(puntajes, key=puntajes.get)
    print("\n¡El Sombrero Seleccionador ha decidido!")
    print(f"¡Felicidades! ¡Has sido seleccionado para la casa de {casa_seleccionada}!")

if __name__ == "__main__":
    print("¡Bienvenido al Sombrero Seleccionador de Hogwarts!")
    print("Responde a las siguientes preguntas para saber a qué casa perteneces:")
    sombrero_seleccionador()
