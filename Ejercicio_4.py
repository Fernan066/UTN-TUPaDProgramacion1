# Ejercicio 4 — “Escape Room: La Bóveda”

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
racha_forzar = 0

while True:
    agente = input("Ingrese nombre del agente: ")
    if agente.isalpha():
        break
    else:
        print("Nombre inválido")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3:
        print("Sistema bloqueado por alarma")
        break

    print(f"\nEnergía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas} | Alarma: {alarma}")
    print("1) Forzar cerradura")
    print("2) Hackear panel")
    print("3) Descansar")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error")
        continue

    match int(opcion):

        case 1:
            energia -= 20
            tiempo -= 2
            racha_forzar += 1

            if racha_forzar == 3:
                alarma = True
                print("La cerradura se trabó y activó la alarma")
                continue

            if energia < 40:
                while True:
                    riesgo = input("Riesgo 1-3: ")
                    if riesgo.isdigit() and 1 <= int(riesgo) <= 3:
                        break
                    else:
                        print("Número inválido")

                match int(riesgo):
                    case 3:
                        alarma = True
                        print("Se activó la alarma")
                        continue

            if not alarma:
                cerraduras_abiertas += 1
                print("Cerradura abierta")

        case 2:
            energia -= 10
            tiempo -= 3
            racha_forzar = 0

            for i in range(4):
                print("Hackeando")
                codigo_parcial += "A"

            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                cerraduras_abiertas += 1
                print("Cerradura abierta por hackeo")

        case 3:
            energia += 15
            if energia > 100:
                energia = 100
            tiempo -= 1
            racha_forzar = 0

            if alarma:
                energia -= 10

        case _:
            print("Opción inválida")

if cerraduras_abiertas == 3:
    print("VICTORIA")
elif energia <= 0 or tiempo <= 0:
    print("DERROTA")
elif alarma and tiempo <= 3:
    print("DERROTA POR BLOQUEO")