#FUNCION PARA VER LA LISTA
def VerLista(nombres, apellidos):
    for i in range(len(nombres)):
        NombresCompletos = " ".join(nombres[i]) + " " + " ".join(apellidos[i])
        print(f"Estudiante {i + 1}: {NombresCompletos}")
    ##[ , ] .join
    

#FUNCION PARA CREAR LISTAS
def UnirNombres (n1, n2):
    ListaNombres = [n1, n2]
    ##.APPEND() AGREGA ELEMENTOS A LA LISTA
    return ListaNombres

def UnirApellidos (a1, a2):
    ListaApellidos = [a1, a2]
    return ListaApellidos

# [Santiago, Jose] -> UnirNombres
# [Aguilar, Vesga ] -> UnirApellidos

def FuncionAppend (a, c):
    a.append(c)
    
def EditarEstudiante(lista, EstudianteEditado, Solicitado):
    lista[EstudianteEditado-1] = Solicitado
    #return lista
    
def EliminarEstudiante(lista, EstudianteEliminado):
    lista.pop(EstudianteEliminado-1)