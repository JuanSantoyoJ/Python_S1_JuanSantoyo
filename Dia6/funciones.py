from modulo import *

nombres = [
    ["Adrián"],
    ["Alejandra"],
    ["Ámbar", "Isabella"],
    ["Andrés", "David"],
    ["Aura", "Camila"],
    ["Camilo", "Andrés"],
    ["Daniel", "Esteban"],
    ["David", "Santiago"],
    ["Edgar", "Leonardo"],
    ["Gerson", "Steven"],
    ["Harley", "Yefrey"],
    ["John", "Stiven"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "David"],
    ["Juan", "Eduardo"],
    ["Juan", "Fernando"],
    ["Juan", "Jose"],
    ["Maria", "Juliana"],
    ["Mateo", "Roman"],
    ["Naya", "Zarela"],
    ["Nicolas"],
    ["Omar", "Fernando"],
    ["Santiago"],
    ["Santiago", "Andrés"],
    ["Santiago"],
    ["Sara", "Sofía"],
    ["Sayara", "Yurley"],
    ["Sergio", "Andrés"],
    ["Simón", "Dante"],
    ["Thomas", "Sebastián"],
    ["Vladimir"]
]

apellidos = [
    ["Quintero", "Pinzón"],
    ["Pinzón", "Alvarez"],
    ["Plata", "López"],
    ["Reyes", "Espinel"],
    ["Pico", "Araque"],
    ["Suárez", "Fuentes"],
    ["Guerrero", "Quintero"],
    ["Vera", "Mendez"],
    ["Acevedo", "Arteaga"],
    ["Chaparro", "Martínez"],
    ["Cabrales", "Vargas"],
    ["Negron", "Regalado"],
    ["Saavedra", "Jaimez"],
    ["Santoyo", "Jaimes"],
    ["Vargas", "Soto"],
    ["Pinilla", "Guzmán"],
    ["Umaña", "Barragan"],
    ["Abril", "Roman"],
    ["Saavedra", "Mejia"],
    ["Camargo"],
    ["Lizcano", "Jaimes"],
    ["Chedraui", "Mantilla"],
    ["Granados", "Parra"],
    ["Aguilar", "Vesga"],
    ["Quiñonez", "Sosa"],
    ["Jaimes", "Perez"],
    ["Díaz", "Rodríguez"],
    ["Aparicio", "Arciniegas"],
    ["Rueda", "Hernández"],
    ["Salamanca", "Galvis"],
    ["Bastos", "Garcia"],
    ["Diaz", "Contreras"]
]
booleanito = True
while booleanito == True:
    print ("""
    1. Ver estudiantes
    2. Agregar estudiantes
    3. Editar estudiantes
    4. Eliminar estudiantes
    5. Salir
    """)
    user = int(input("Ingrese un número : ")) ##TODOS los inputs entran como texto (string "")
    if user == 1:
        VerLista(nombres, apellidos)
    elif user == 2:
        ##NOMBRES
        SolicitarPrimerNombre = input("Ingrese el primer nombre")
        SolicitarSegundoNombre= input("Ingrese el segundo nombre")
        ListaNombress = UnirNombres(SolicitarPrimerNombre, SolicitarSegundoNombre)
        FuncionAppend(nombres, ListaNombress)
        ##APELLIDOS
        PrimerApellido = input("Ingrese el primer apellido")
        SegundoApellido = input("Ingrese el segundo apellido")
        ListaApellidos = UnirApellidos(PrimerApellido, SegundoApellido)
        FuncionAppend(apellidos, ListaApellidos)
    elif user == 3:
        EstudianteEditar = int(input("Cuál estudiante quieres editar"))
        SolicitarPrimerNombre = input("Ingrese el primer nombre: ")
        SolicitarSegundoNombre = input("Ingrese el segundo nombre: ")
        ListaNombress = UnirNombres(SolicitarPrimerNombre, SolicitarSegundoNombre)
        EditarEstudiante(nombres, EstudianteEditar, ListaNombress)
        ##
        PrimerApellido = input("Ingrese el primer apellido")
        SegundoApellido = input("Ingrese el segundo apellido")
        ListaApellidos = UnirApellidos(PrimerApellido, SegundoApellido)
        EditarEstudiante(apellidos, EstudianteEditar, ListaApellidos)
    elif user == 4:
        EstudianteEliminar = int(input("¿Cuál estudiante quieres eliminar?"))
        EliminarEstudiante(nombres, EstudianteEliminar)
        EliminarEstudiante(apellidos, EstudianteEliminar)
    elif user == 5:
        booleanito = False
        