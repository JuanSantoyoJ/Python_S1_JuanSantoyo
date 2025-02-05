#Palabra palindrome
def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]
palabra_ingresada = input("Ingresa una palabra: ")
if es_palindromo(palabra_ingresada):
    print(f"'{palabra_ingresada}' es un palíndromo.")
else:
    print(f"'{palabra_ingresada}' no es un palíndromo.")
#Desarrolado por Juan David Santoyo Jaimes / T.I: 1099740117