import random
while True:
    #Reglas del juego
    opciones = ['piedra', 'papel', 'tijera']
    computadora = random.choice(opciones)
    #Menu del juego
    nombre = input("Hola intruduce un usuario para empezar a jugar: ")
    #Se usa un fString para incluir dentro del print una variable que en este caso use la variable
    #que almacena un nombre 
    print(f"Bienvenido al juego \nPiedra🪨 Papel📄 O Tijera✂️  {nombre}")
    print("-------Lista-------")
    print("|🪨|Piedra"        )
    print("|📄|Papel "        )
    print("|✂️|Tijera"        )
    print("-------Salir-------")
    Jugador = input(f"Hora de juga {nombre} selecciona tu jugada: ").lower()
    if Jugador == "salir":
        print("Saliendo")
        break
    #Se realiza una comparacion entre la eleccion de el jugador y la computador ay se define un ganador
    elif Jugador not in ("piedra", "papel", "tijera",):
        print("opcion no valida vuelve a ingresar")
        continue
    if computadora == "piedra" and Jugador == "tijera":
      print("GANA COMPUTADORA")
    elif computadora == "tijera" and Jugador == "piedra":
      print("GANA JUGADOR")
    elif computadora == "papel" and Jugador == "piedra":
      print("GANA COMPUTADORA")
    elif computadora == "piedra" and Jugador == "papel":
      print("GANA JUGADOR")
    elif computadora == "tijera" and Jugador == "papel":
      print("GANA COMPUTADORA")
    elif computadora == "papel" and Jugador == "tijera":
      print("GANA JUGADOR")
    elif computadora == "piedra" and Jugador == "piedra":
      print("EMPATE")
    elif computadora == "papel" and Jugador == "papel":
      print("EMPATE")
    elif computadora == "tijera" and Jugador == "tijera":
     print("EMPATE")
    while True:
     volver = input("¿Quieres volver a jugar? (si/no): ").lower()
     if volver == "si":
        print(f"Vamos a jugar de nuevo {nombre}")
        break  # sale de este while y vuelve al juego
     elif volver == "no":
        print(f"Gracias por jugar {nombre}")
        exit()  # termina todo el programa
     else:
        print("Opción no válida")
