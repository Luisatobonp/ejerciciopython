#11.Escriba un algoritmo que acepte o rechace una pieza en forma de varilla,
#para una empresa de acuerdo a los siguientes criterios:
#a. Su longitud debe ser mayor de 7.5 cm pero no exceder los 9 cm
#b. Su diámetro no debe ser menor que 0.5 cm ni mayor de 1.3 cm.
#c. Por ningún motivo su masa debe exceder los 5.8 cm
#i. Nota: masa = diámetro * longitud / densidad; densidad = 3.5
#Gr/cm

longitud = float(input("digite su longitud:"))
diametro = float(input("digite su diametro:"))
masa = (diametro * longitud)/ 3.5

acepta = False


if longitud > 7.5 and longitud < 9 and  diametro > 0.5 and diametro < 1.3 and masa < 5.8:
    print("se acepta")
else: 
    print("no se acepta")




