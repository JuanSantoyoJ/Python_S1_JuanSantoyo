#funcion para validar un email
def validarEmail(email):
    if email.count("@") == 1 and email.count(".") == 1:
        return True
    else:
        return False
email=input("Ingresa tu email: ")
if validarEmail(email):
    print("Email válido")
else:
    print("Email no válido")
#Desarrollado por Juan David Santoyo Jaimes / T.I: 1099740117