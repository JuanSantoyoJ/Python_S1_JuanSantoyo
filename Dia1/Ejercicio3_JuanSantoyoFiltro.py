#Numeros que satisfacen la expresion:
print("Estos numeros satisfacen la siguiente expresion: (P^3) + (Q^4) - 2 (P^2) < 680")
for p in range(0,200):
    for q in range(0,200):
        SatisNum=(p**3) + (q**4) - (2 * (p**2))
        if (SatisNum<680):
            print("P: ",p)
            print("Q: ",q)
            print("= ", SatisNum)
#Desarrollado por: Juan David Santoyo Jaimes / T.I. : 1099740117