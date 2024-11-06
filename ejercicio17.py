#desarrollar el algoritmo que lea tres números y diga si uno es divisible del
#otro

num1 = float(input("digite el numero 1:"))
num2 = float(input("digite el numero 2:"))
num3 = float(input("digite el numero 3:"))

divisible1 = False
divisible2 = False
divisible3 = False
if num1 % num2 and num1 % num3:
    divisible1 = True
if num2 % num3 and num2 % num1:
    divisible2 = True
if num3 % num2 and num3 % num1:
    divisible3 = True
    print("los valores son divisibles entre si")
else: 
    print("no son divisibles entre si")
    