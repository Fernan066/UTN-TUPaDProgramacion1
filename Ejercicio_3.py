# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

while True:
    operador = input("Ingrese nombre del operador: ")

    if operador.isalpha():
        break
    else:
        print("Nombre inválido")

while True:
    print("\n1) Reservar turno")
    print("2) Cancelar turno")
    print("3) Ver agenda del día")
    print("4) Ver resumen general")
    print("5) Cerrar sistema")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un número")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 5:
        print("Error: opción inválida")
        continue

    match opcion:

        case 1:
            dia = input("Día (1=Lunes, 2=Martes): ")

            if not dia.isdigit():
                print("Día inválido")
                continue

            dia = int(dia)

            while True:
                nombre = input("Nombre del paciente: ")

                if nombre.isalpha():
                    break
                else:
                    print("Nombre inválido")

            if dia == 1:
                if (nombre == lunes1 or nombre == lunes2 or
                    nombre == lunes3 or nombre == lunes4):
                    print("Paciente ya tiene turno en Lunes")

                elif lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("No hay cupos en Lunes")

            elif dia == 2:
                if (nombre == martes1 or nombre == martes2 or
                    nombre == martes3):
                    print("Paciente ya tiene turno en Martes")

                elif martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("No hay cupos en Martes")

            else:
                print("Día inválido")

        case 2:
            dia = input("Día (1=Lunes, 2=Martes): ")

            if not dia.isdigit():
                print("Día inválido")
                continue

            dia = int(dia)

            nombre = input("Nombre del paciente: ")

            if not nombre.isalpha():
                print("Nombre inválido")
                continue

            if dia == 1:
                if nombre == lunes1:
                    lunes1 = ""
                elif nombre == lunes2:
                    lunes2 = ""
                elif nombre == lunes3:
                    lunes3 = ""
                elif nombre == lunes4:
                    lunes4 = ""
                else:
                    print("Paciente no encontrado")

            elif dia == 2:
                if nombre == martes1:
                    martes1 = ""
                elif nombre == martes2:
                    martes2 = ""
                elif nombre == martes3:
                    martes3 = ""
                else:
                    print("Paciente no encontrado")

            else:
                print("Día inválido")

        case 3:
            dia = input("Día (1=Lunes, 2=Martes): ")

            if not dia.isdigit():
                print("Día inválido")
                continue

            dia = int(dia)

            if dia == 1:
                print("\nLunes:")
                print("1:", lunes1 if lunes1 != "" else "(libre)")
                print("2:", lunes2 if lunes2 != "" else "(libre)")
                print("3:", lunes3 if lunes3 != "" else "(libre)")
                print("4:", lunes4 if lunes4 != "" else "(libre)")

            elif dia == 2:
                print("\nMartes:")
                print("1:", martes1 if martes1 != "" else "(libre)")
                print("2:", martes2 if martes2 != "" else "(libre)")
                print("3:", martes3 if martes3 != "" else "(libre)")

            else:
                print("Día inválido")

        case 4:
            ocupados_lunes = 0
            if lunes1 != "": ocupados_lunes += 1
            if lunes2 != "": ocupados_lunes += 1
            if lunes3 != "": ocupados_lunes += 1
            if lunes4 != "": ocupados_lunes += 1

            ocupados_martes = 0
            if martes1 != "": ocupados_martes += 1
            if martes2 != "": ocupados_martes += 1
            if martes3 != "": ocupados_martes += 1

            print("\nLunes ocupados:", ocupados_lunes, "libres:", 4 - ocupados_lunes)
            print("Martes ocupados:", ocupados_martes, "libres:", 3 - ocupados_martes)

            if ocupados_lunes > ocupados_martes:
                print("Día con más turnos: Lunes")
            elif ocupados_martes > ocupados_lunes:
                print("Día con más turnos: Martes")
            else:
                print("Empate")

        case 5:
            print("Sistema cerrado")
            break