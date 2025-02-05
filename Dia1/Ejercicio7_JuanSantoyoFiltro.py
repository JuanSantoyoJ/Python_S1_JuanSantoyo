#Numeros Amigos
n1=int(input("Ingresa el n1: "))
n2=int(input("Ingresa el n2: "))
suma1=0
suma2=0
for i in range (1,n1):
    if (n1%i ==0):
        suma1+=i
for i in range (1,n2):
    if (n2%i ==0):
        suma2+=i
if suma1==n2 and suma2==n1:
    print(n1," y ",n2," Son numeros amigos" )
else:
    print("No son numeros amigos")
#Desarrolado Juan David Santoyo Jaimes 