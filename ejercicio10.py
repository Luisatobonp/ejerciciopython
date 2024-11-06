#A ciertos estudiantes se les dice que su calificación final será el promedio
#de las dos calificaciones más altas de entre las tres que se han obtenido en
#el curso. Haga un algoritmo que permita a un estudiante efectuar el cálculo
#correspondiente a su nota final.

rating1 = float(input("ingrese la nota 1:"))
rating2 = float(input("ingrese la nota 2:"))
rating3 = float(input("ingrese la nota 3:"))

numero_mayor = rating1
numero_mitad = "no hay numero medio"
numero_menor = rating1

if rating1 > rating2 and rating1 > rating3:
    numero_mayor = rating1
if rating2 > rating1 and rating2 > rating3:
    numero_mayor = rating2
if rating3 > rating1 and rating3 > rating2:
    numero_mayor = rating3

if rating1 < rating2 and rating1 < rating3:
    numero_menor = rating1
if rating2 < rating1 and rating2 < rating3:
    numero_menor = rating2
if rating3 < rating1 and rating3 < rating2:
    numero_menor = rating3
    
if rating1 != numero_mayor and rating1 != numero_menor:
    numero_mitad = rating1
if rating2 != numero_mayor and rating2 != numero_menor:
    numero_mitad = rating2
if rating3 != numero_mayor and rating3 != numero_menor:
    numero_mitad = rating3

print("el numero mayor es:", numero_mayor)
print("el numero medio es:", numero_mitad)
print("el numero menor es:", numero_menor)

prom = (numero_mayor + numero_mitad)/2
print("su nota final es:", prom)
