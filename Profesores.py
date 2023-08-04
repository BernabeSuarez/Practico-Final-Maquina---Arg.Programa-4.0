import TDA_Profesores
import TDA_Inscripciones


def guardar_nota(inscripciones, data_a_modificar, alumno):
    new_file = TDA_Inscripciones.modInscripcion(inscripciones, data_a_modificar, alumno)
    archivo = open("Inscripciones.txt", "w")
    for item in new_file:
        data = list(item.values())
        inscripcion_personal = ",".join(data)
        archivo.write(inscripcion_personal)
        archivo.write("\n")
    archivo.close()


def cargarNota(inscripciones):
    alumno = input("Ingrese el alumno que desea modificar: ").lower()
    # acceder al diccionario que contiene el la inscripcion del alumno solicitado
    if alumno in inscripciones.keys():
        data_a_modificar = inscripciones[alumno]
        nota = input("Ingresela nota: ")
        TDA_Inscripciones.modNota(data_a_modificar, nota)
        guardar_nota(inscripciones, data_a_modificar, alumno)
        print("Nota cargada correctamente")

    else:
        print("Alumno no encontrado!")
        print("")


def menuModificarNota(inscripciones):
    alumno = input("Ingrese el alumno que desea modificar: ").lower()
    # acceder al diccionario que contiene el la inscripcion del alumno solicitado
    if alumno in inscripciones.keys():
        data_a_modificar = inscripciones[alumno]
        nota_actual = data_a_modificar["nota"]
        print(f"La nota actual es: {nota_actual}")
        print("")
        print("Desea modificarla?")
        seleccion = input("Si / No: ").lower()
        if seleccion == "si":
            nota = input("Ingresela nota: ")
            TDA_Inscripciones.modNota(data_a_modificar, nota)
            guardar_nota(inscripciones, data_a_modificar, alumno)
            print("Nota modificada con exito")
        elif seleccion == "no":
            pass
        else:
            print("Solamente responda Si o No")

    else:
        print("Alumno no encontrado!")
        print("")


def menu_profesores():
    inscripciones = TDA_Inscripciones.getInsctipciones()
    if len(inscripciones) < 1:
        print("")
        print(
            "No existen Inscripciones realizadas, por favor contacte a un encargado que realize las inscripciones"
        )
        print("")

    else:
        sel = 1
        while sel != 0:
            print("Seleccione que accion desea realizar:")
            print("")
            print("1. Cargar nota del alumno")
            print("2. Modificar nota de alumno")
            print("3. Salir")
            print("")

            opcionMenu = int(input("Ingrese una opcion: "))
            sel = opcionMenu
            if opcionMenu == 1:
                try:
                    cargarNota(inscripciones)
                    print("")
                except:
                    print("No se pudo cargar la nota, por favor, intente nuevamente")
                    print("")
            elif opcionMenu == 2:
                try:
                    menuModificarNota(inscripciones)
                    print("")
                except:
                    print("No se pudo realizar la modificacion, intente nuevamente")
                    print("")
            elif opcionMenu == 3:
                break
            else:
                print("Ingrese una opcion correcta")
                print("")
