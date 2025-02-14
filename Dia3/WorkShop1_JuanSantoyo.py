#Fahrenheit y Celsius
def Celsius_a_Fahrenheit(c):
    conversion=(c*1.8)+32
    return conversion
def Fahrenheit_a_Celsius(f):
    conversion=(f-32)*0.55
    return conversion
opcion=input("Quieres convertir Celsius a Fahrenheit (Ingresa c) o quieres convertir Fahrenheit a Celsius (Ingresa f): ")
if (opcion == "C" or opcion == "c"):
    Celsius=int(input("Ingresa los grados Celsius: "))
    resultadoC=Celsius_a_Fahrenheit(Celsius)
    print("El resultado es: ",resultadoC)
elif (opcion == "F" or opcion == "f"):
    Fahrenheit=int(input("Ingresa los grados Fahrenheit: "))
    resultadoF=Fahrenheit_a_Celsius(Fahrenheit)
    print("El resultado es: ",resultadoF)
else:
    print("Error")
#Desarrollado por Juan David Santoyo Jaimes / T.I: 1099740117