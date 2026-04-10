# Ejercicio 1— “Acceso al Campus y Menú Seguro”

usuario_correcto = "alumno"
clave_correcta = "python123"

intentos = 0
acceso = False

while intentos < 3:
    print(f"Intengo {intentos+1}/3")

    usuario = input("Usuario: ")
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso autorizad")
        acceso = True
        break
    else:
        print("Error: Nombre de usuario o contraseña incorrectos")
        intentos += 1

if not acceso:
    print("Cuenta bloqueada")

while acceso:
    print("1) Estado")
    print("2) Cambiar clave")
    print("3) Mensaje")
    print("4) Salir")
    print(" ")

    opcion = input("Opción: ")

    if not opcion.isdigit():
        print("Error: ingrese un numero valido")
        continue

    opcion = int(opcion)

    if opcion < 1 or opcion > 4:
        print("Opcion no valida")
        continue

    match opcion:
        case 1:
            print("Estado: inscripto")
            print(" ")
        case 2:
            while True:
                nueva_clave = input("Nueva clase: ")

                if len(nueva_clave) < 6:
                    print("Minimo 6 caracteres")
                    continue
                confirmacion = input("Confirmar clave: ")

                if nueva_clave != confirmacion:
                    print("Las claves no coinciden")
                else:
                    clave_correcta = nueva_clave
                    print("Clave actualizada correctamente")
                    break
        case 3:
            print("Mandale mecha, vos podes 🗣️")
            print(" ")
        case 4:
            print("Saliento del sistema")
            print(" ")
            break