# Factorial de un número, permutaciones y combinaciones
n = int(input("Ingresa el número: "))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def permutations(n, r):
    return factorial(n) // factorial(n-r)

def combinations(n, r):
    return factorial(n) // (factorial(r) * factorial(n-r))

print("El factorial de", n, "es", factorial(n))
print("El número de permutaciones de", n, "es", permutations(n, n))
print("El número de combinaciones de", n, "es", combinations(n, n))
#Desarrollado por Juan David Santoyo Jaimes / T.I: 1099740117