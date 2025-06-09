import random
menu = input("Quieres jugar: ")
if menu == "Si":
    print("Vamos a jugar")
else:
    print("Chao")
opciones = ['Piedra', 'Papel', 'Tijera']
computadora = random.choice(opciones)
print("Piedra")
print("Papel")
print("Tijera")

Jugador = input("ELIJE UNA JUGADA: ")
 
if computadora == "Piedra" and Jugador == "Tijera":
    print("GANA COMPUTADORA")
elif computadora == "Tijera" and Jugador == "Piedra":
    print("GANA JUGADOR")
elif computadora == "Papel" and Jugador == "Piedra":
    print("GANA COMPUTADORA")
elif computadora == "Piedra" and Jugador == "Papel":
    print("GANA JUGADOR")
elif computadora == "Tijera" and Jugador == "Papel":
    print("GANA COMPUTADORA")
elif computadora == "Papel" and Jugador == "Tijera":
    print("GANA JUGADOR")
elif computadora == "Piedra" and Jugador == "Piedra":
    print("EMPATE")
elif computadora == "Papel" and Jugador == "Papel":
    print("EMPATE")
elif computadora == "Tijera" and Jugador == "Tijera":
    print("EMPATE")
else:
    print(menu)