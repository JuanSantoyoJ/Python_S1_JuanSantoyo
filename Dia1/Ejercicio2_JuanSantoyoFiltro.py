#Construya un programa tal que lea un número entero N, muestre la cantidad de términos y el resultado
#de la siguiente serie:
CantidadDeTerminos=int(input("Ingresa el ultimo num de la sucesion: "))
sum=0
for i in range(1, CantidadDeTerminos):
    if (i%2==0):
        sum=sum-(1/1)
    else:
        sum=sum+(1/1)
print("La cantidad de terminos es: ", CantidadDeTerminos)
print("La sumatoria da: ", sum)
#Desarrollado por Juan David Santoyo / T.I: 1099740117