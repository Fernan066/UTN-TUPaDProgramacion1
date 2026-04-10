# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

print("BIENVENIDO A LA ARENA")

while True:
    nombre = input("Nombre del Gladiador: ")
    if nombre.isalpha():
        break
    else:
        print("Error: Solo se permiten letras.")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_jugador = 15
danio_enemigo = 12
turno_jugador = True

print("=INICIO DEL COMBATE=")

while vida_jugador > 0 and vida_enemigo > 0:

    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    print("Elige accion:")
    print("1. Ataque Pesado")
    print("2. Rafaga Veloz")
    print("3. Curar")

    while True:
        opcion = input("Opcion: ")
        if opcion.isdigit():
            opcion = int(opcion)
            if opcion >= 1 and opcion <= 3:
                break
            else:
                print("Error: opcion invalida.")
        else:
            print("Error: Ingrese un numero valido.")

    match opcion:

        case 1:
            if vida_enemigo < 20:
                danio = danio_jugador * 1.5
            else:
                danio = danio_jugador

            vida_enemigo -= danio
            print(f"Atacaste al enemigo por {danio} puntos de daño!")

        case 2:
            print(">> Inicias una rafaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print("> Golpe conectado por 5 de daño")

        case 3:
            if pociones > 0:
                vida_jugador += 30
                pociones -= 1
                print("Te curaste 30 puntos de vida")
            else:
                print("No quedan pociones!")

    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f">> El enemigo contraataca por {danio_enemigo} puntos!")

print("\n=== FIN DEL COMBATE ===")

if vida_jugador > 0:
    print(f"VICTORIA! {nombre} ha ganado la batalla.")
else:
    print("DERROTA...Has caído en combate.")