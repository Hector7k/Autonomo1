import random
opciones = ['Piedra', 'Papel', 'Tijera']
computadora = random.choice(opciones)
while True:
    print("Lista")
    print("Piedra")
    print("Papel")
    print("Tijera")
    print("salir")
    Jugador = input("\n seleccione uno: ")
    
    if Jugador == "salir":
        print("Saliendo")
        break
    elif Jugador not in ("Piedra", "Papel", "Tijera",):
        print("opcion no valida vuelve a ingresar")
        continue
    elif computadora == "Piedra" and Jugador == "Tijera":
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
