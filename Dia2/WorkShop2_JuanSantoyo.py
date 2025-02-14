#Interes simple y compuesto
def Interes_Simple (CapInicial, Tasa, Tiempo):
    Int=CapInicial * (Tasa/100) * Tiempo
    return Int

Capital=int(input("Ingresa el capital inicial: "))
Tasa_De_Interes=float(input("Ingresa los intereses (%): "))
Tiempo_Años=int(input("Ingresa el tiempo (en años): "))
Resultado=Interes_Simple(Capital,Tasa_De_Interes,Tiempo_Años)
print("El interes simple en",Tiempo_Años,"Años" , "fue de:",Resultado,"$")

def Interes_Comp(CapInicial, Tasa, Tiempo):
    InteresComp = CapInicial * (1 + Tasa / 100) ** Tiempo
    return InteresComp

Capital = int(input("Ingresa el Capital: "))
Intereses = float(input("Ingresa los intereses (%): "))
Tiempo_Años = int(input("Ingresa el tiempo (años): "))
ResultadoComp = Interes_Comp(Capital, Intereses, Tiempo_Años)
print("El interes compuesto es: ",ResultadoComp)
#Desarrollado por Juan David Santoyo Jaimes / T-I: 1099740117