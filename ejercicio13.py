#desarrollar un algoritmo que halle la nota total de una materia en el SENA, y
#determine si la gano o la reprobó

nota1 = float(input("digite la nota 1:"))
nota2 = float(input("digite la nota 2:"))
nota3 = float(input("digite la nota 3:"))

nota_final = 0
nota_final = (nota1 + nota2 + nota3)/3
if nota_final > 3:
    print("su materia ha sido aprobada")
else: 
    nota_final < 2.9
    print("su materia ha sido reprobada")
