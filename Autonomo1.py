import random
while True:
    #Reglas del juego
    opciones = ['piedra', 'papel', 'tijera']
    computadora = random.choice(opciones)
    #Menu del juego
    print("-------Lista-------")
    print("Piedra")
    print("Papel")
    print("✂️ Tijera")
    print("Salir")
    Jugador = input("seleccione uno: ").lower()
    
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
    volver = input("Quieres volver a jugar: ").lower()
    if volver == "no":
        print("Gracias por jugar")
        break
    elif volver == "si":
       print("volver a jugar")
       continue
