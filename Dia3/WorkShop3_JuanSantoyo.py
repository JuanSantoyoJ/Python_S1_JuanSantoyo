## comprobar si un numero es par o impar 
import math 
## tengo que importar math ya que es complejo 
def clasificar_numero(n):
    if n < 0:
        return "el numero no debe ser negativo"
    par_impar = "par" if n % 2==0 else "impar "

    if n < 2:
        primo_o_no = "no es primo ni compuesto"

    else: 
 
        for i in range (2, int(math.sqrt(n)) +1):
            if n % i == 0:
               primo_o_no = "compuesto"
               break
        else: 
            primo_o_no="primo"

    raiz=int(math.sqrt(n))
    cuadrado_perfecto= "es un cuadrado perfecto"if raiz*raiz== n else "no es cuadrado perfecto"

    return f"El número {n} es {par_impar}, {primo_o_no}, y {cuadrado_perfecto}."

while True:
    try:
        numero = int(input("Ingresa un número entero: "))
        break  # Salir del bucle si la entrada es válida
    except ValueError:
      print("Entrada inválida. Por favor, ingresa un número entero.")
clasificacion = clasificar_numero(numero)
print(clasificacion)
#Desarrolado por Juan David Santoyo Jaimes / T.I: 1099740117