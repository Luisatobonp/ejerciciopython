#desarrollar un algoritmo que capture un número y diga si es par o impar.

num = float(input("ingrese un numero:"))
resultado = num % 2
if resultado == 0:
    print("el resultado es par")
else:
    print("el resultado es impar")