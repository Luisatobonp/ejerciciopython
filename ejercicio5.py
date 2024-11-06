#desarrollar un programa que capture tres números e imprima por pantalla
#cual es el número mayor, el menor, cuales son iguales, si los tres
#diferentes.

num1 = float(input("digite el numero 1:"))
#la variable may va almacenar el numero mayor
may = num1
#la variable men va almacenar el numero menor
men = num1
num2 = float(input("digite el numero 2:"))
if num2 > may:
    may = num2

if num2< men:
    men = num2


num3 = float(input("digite el numero 3:"))
if  num3 > may:
    may = num3

if num3 < men:
    men = num3
    
if num1 == num2:
    print("num1 y num2 son iguales", num1)
if num1 == num3:
    print("num1 y num3 son iguales", num3)
if num2 == num3:
    print("num2 y num3 son iguales", num3)
print("el numero mayor es:" , may)
print("el numero menor es:", men)





