#Dados tres números enteros únicos, a, b y c. Elabore un algoritmo que los
#ordene de mayor a menor e imprímalos.

a = int(input("digite el primer numero:"))
b = int(input("digite el segundo numero"))
c = int(input("digite el tercer numero:"))

if a != b and a != c and b != c:
    numeros = [a, b, c]
    numeros.sort(reverse=True)
    print("los numeros ordenados de mayor a menor son:", numeros)

else:
    print("los numeros digitados deben ser diferentes")
    


        