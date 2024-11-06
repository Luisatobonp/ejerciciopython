#Prepare un algoritmo que identifique e imprima el número medio de un
#conjunto de tres números únicos. El número medio es aquel que no es el
#menor ni el mayor.

num1 = int(input("digite el primer numero:"))
num2 = int(input("digite el segundo numero:"))
num3 = int(input("digite el tercer numero:"))


# Colocamos los números en una lista
numeros = [num1, num2, num3]
    # Ordenamos la lista
numeros.sort()
    # El número medio es el segundo elemento
print ("el numero medio es:", numeros[1])