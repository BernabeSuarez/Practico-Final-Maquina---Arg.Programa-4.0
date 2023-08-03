from os import system
import TDA_Encargado
import TDA_Inscripciones
import Encargado


system("clear")

print("*********************************************")
print("Bienvenido")
print("Ingrese al sistema")
print("")


def salir():
    print("")
    print("Gracias por utilizar nuestro programa")


# Ingresar a la plataforma de usuarios.
user = input("Ingrese su nombre y apellido: ").lower()

# abrir los archivos de textos
encarg_file = open("Encargados.txt", "r")
profe_file = open("Profesores.txt", "r")
insc_file = open("Inscripciones.txt", "r")

# guardar la info de los archivos
encargados = encarg_file.read().split("\n")
profesores = profe_file.read().rstrip().split("\n")
inscriptos = insc_file.read().rstrip().split("\n")

# cerrar los archivos de texto
encarg_file.close()
profe_file.close()
insc_file.close()


encar_auth_list = {}
prof_auth_list = {}
inscripciones = {}


# generar un diccionario de los encargados
for item in encargados:
    data = item.split(",")
    encar_auth_list[data[0].lower()] = data[1]

# generar un dccionario de los profesores
for item in profesores:
    data = item.split(",")
    prof_auth_list[data[0].lower()] = data[1].lower()

# generar un diccionario de las Inscripciones
for item in inscriptos:
    data = item.split(",")
    inscripciones[data[1].lower()] = TDA_Inscripciones.inscribir(
        data[0], data[1], data[2], data[3], data[4], data[5], data[6]
    )
# autenticacion de usuario

if user in encar_auth_list.keys():
    dni = input("Ingrese su DNI(sin puntos): ")
    if dni in encar_auth_list.values():
        print("Usuario Encargado autenticado")
        # llamar a la funcion del menu encargado
        print(inscripciones)
        Encargado.menu_encargado(inscripciones)
        salir()
    else:
        print("DNI no coincide con el registrado para este Usuario.")
elif user in prof_auth_list.keys():
    materia = input("Ingrese la materia que dicta: ")
    if materia in prof_auth_list.values():
        print("Usuario Profesor autenticado")  # llamar a la funcion del menu encargado
    else:
        print("La materia no corresponde al profesor")
        print("")
else:
    print("Usuario incorrecto")
