#desarrollar un programa que, dado una calificación de un alumno en un parcial, escribe aprobado si la calificación es superior a 3.
#parcial, escribe aprobado si la calificación es superior a 3.
num = float(input("digite la calificacion de 0 a 5:"))
if num >= 3 and num <= 5:
    print("aprobado")
elif num < 3 and num >=0:
    print("reprobado")
else: 
    print("la calificacion no es valida")


