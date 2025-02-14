# Factorial de un número
n = int(input("Ingresa el factorial: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("El factorial de", n, "es", factorial(n))
#Desarrollado por Juan David Santoyo Jaimes / T.I: 1099740117