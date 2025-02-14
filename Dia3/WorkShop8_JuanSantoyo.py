# Funcion que recibe una palabra y cuenta el número de vocales, consonantes y el caracter que más se repite.
palabra = input("Ingresa una palabra: ")

def contar_vocales(palabra):
    vocales = "aeiou"
    consonantes = "bcdfghjklmnpqrstvwxyz"
    contador_vocales = 0
    contador_consonantes = 0
    caracteres = {}

    for letra in palabra:
        if letra in vocales:
            contador_vocales += 1
        elif letra in consonantes:
            contador_consonantes += 1

        caracteres[letra] = caracteres.get(letra, 0) + 1

    max_caracter = max(caracteres, key=caracteres.get)

    print("Número de vocales:", contador_vocales)
    print("Número de consonantes:", contador_consonantes)
    print("Caracter que más se repite:", max_caracter)

contar_vocales(palabra)
#Desarrollado por Juan David Santoyo Jaimes / T.I: 1099740117