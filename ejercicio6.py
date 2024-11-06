#Escriba el algoritmo que al capturar un numero entero convierta grados
#centígrados a kelvin, si captura un numero flotante diga si es mayor a 10.5,
#y si captura un carácter escriba su nombre.

entrada = input("Introduce un valor: ")

# Intentar convertir a entero
try:
    print("kelvin = ", int(entrada)+ 273.15)


except ValueError:
    # Intentar convertir a flotante
    try:
        if float(entrada) > 10.5:
            print(f"{entrada} es mayor a 10.5")
        else:
            print(f"{entrada} es menor a 10.5")

    except ValueError:
        # Verificar si es un carácter
        if len(entrada) == 1:
            print(f"{entrada} es un carácter.")
        else:
            print(f"{entrada} no es un entero, ni un flotante, ni un carácter.")
