# Serie fibonacci
def analizar_fibonacci(n):
    num1 = 0
    num2 = 1
    pares = [] 
    suma_fibonacci = 0  

    print("Serie de Fibonacci:")
    for i in range(n):
        print(num1)
        if num1 % 2 == 0:
            pares.append(num1)
        suma_fibonacci += num1 
        num3 = num1 + num2
        num1 = num2
        num2 = num3

    print("Números pares en la serie:") 
    for par in pares:
        print(par)

    print("Suma de la serie de Fibonacci:", suma_fibonacci) 
n = int(input("Ingresa el largo de la serie: "))
analizar_fibonacci(n)
#Desarrollado por Juan David Santoyo Jaimes / T.I: 1099740117