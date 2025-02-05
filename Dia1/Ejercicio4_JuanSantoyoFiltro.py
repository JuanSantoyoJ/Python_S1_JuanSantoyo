#Mayor y menor
grande=0
pequeño=0
for i in range(1,11):
    num=int(input("Ingrese un numero: "))
    if i == 1:
        grande=num
        pequeño=num
    elif num > grande:
        grande=num
    elif num < pequeño:
        pequeño=num
print("El mayor es: ", grande)
print("El numero menor es: ", pequeño)    
 
#Desarollado Juan David Santoyo Jaimes / T.I : 1099740117