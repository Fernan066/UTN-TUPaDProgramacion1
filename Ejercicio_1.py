# Ejercicio 1— “Caja del Kiosco”

total_sin = 0
total_con = 0

while True:
    Nombre = input("Ingrese su nombre (solo letras): ")

    if Nombre.isalpha():
        break
    else:
        print("Nombre inválido")

while True:
    Cantidad_productos = input("Ingrese la cantidad de productos: ")

    if Cantidad_productos.isdigit() and int(Cantidad_productos) > 0:
        Cantidad_productos = int(Cantidad_productos)
        break
    else:
        print("Ingrese un numero valido")

for i in range(Cantidad_productos):

    # PRECIO
    while True:
        precio = input(f"Producto {i+1} - precio: ")

        if precio.isdigit():
            precio = int(precio)
            break
        else:
            print("Precio invalido")

    while True:
        descuento = input("Tiene descuento? (S/N): ").lower()

        match descuento:
            case "s":
                tiene_descuento = True
                break
            case "n":
                tiene_descuento = False
                break
            case _:
                print("Ingrese S o N")

    total_sin += precio

    if tiene_descuento:
        precio_final = precio * 0.9
        total_con += precio_final
    else:
        total_con += precio

ahorro = total_sin - total_con
promedio = total_con / Cantidad_productos

print(f"\nCliente: {Nombre}")
print(f"Total sin descuento: $ {total_sin}")
print(f"Total con descuento: $ {total_con:.2f}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")