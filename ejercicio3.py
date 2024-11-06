#desarrollar el algoritmo dado como dato el sueldo de un trabajador, le aplica
#un aumento del 15% si su sueldo es inferior a $300.000.

sal = float(input("ingrese su salario"))
if sal < 300000:
    aum = sal * 0.15 
    print ("su sueldo es de:", (sal + aum))

else:
    print("no aplica aumento")

