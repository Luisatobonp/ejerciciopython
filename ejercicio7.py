#Desarrolle un algoritmo que lea de un registro: el nombre, la edad, el sexo,
#el estado civil de cualquier persona e imprima el nombre de la persona, si
#corresponde a un hombre casado mayor de 40 años o a una mujer soltera
#menor de 50 años.

nombre = input("digite su nombre:")
edad = int(input("digite su edad:"))
estado_civil = input("digite su estado civil:")
sexo = input("digite su sexo:")

if sexo == "hombre" and estado_civil == "casado" and edad > 40:
    print("el nombre de la persona es:", nombre)

if sexo == "mujer" and estado_civil == "soltera" and edad < 50:
    print("el nombre de la persona es:", nombre)
    
