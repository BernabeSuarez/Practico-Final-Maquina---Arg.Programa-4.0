import TDA_Encargado
import TDA_Inscripciones


def sobreescribir_inscripciones(inscripciones, data_a_modificar, alumno):
    inscripciones[alumno] = data_a_modificar
    new_file = list(inscripciones.values())
    archivo = open("Inscripciones.txt", "w")
    for item in new_file:
        data = list(item.values())
        inscripcion_personal = ",".join(data)
        archivo.write(inscripcion_personal)
        archivo.write("\n")
    archivo.close()


def inscribir():
    fecha = input("Ingrese la fecha del examen(dd/mm/aa): ")
    nombre = input("Ingrese el nombre y apellido del alumno: ")
    materia = input("Materia que rinde: ")
    profesor = input("Nombre completo del profesor responsable:")
    curso = input("Curso al que pertenece: ")
    division = input("Division del curso: ")
    newData = TDA_Inscripciones.inscribir(
        fecha, nombre, materia, profesor, curso, division, nota=-1
    )
    listaInsc = open("Inscripciones.txt", "a")
    listaInsc.write(
        f"\n{newData['fecha']},{newData['nombre']},{newData['materia']},{newData['profesor']},{newData['curso']},{newData['division']},{newData['nota']}"
    )
    listaInsc.close()


def modificar(inscripciones, data_a_modificar, alumno):
    print("Que desea modificar?")
    print("")
    print("1. Fecha del examen.")
    print("2. Materia a rendir.")
    print("3. Profesor de la materia.")
    print("4. Curso del alumno.")
    print("5. Division del curso.")
    print("")
    opcion_mod = input("Ingrese una opcion: ")
    if int(opcion_mod) == 1:
        new_fecha = input("Ingrese la fecha nueva: ")
        TDA_Inscripciones.modFecha(data_a_modificar, new_fecha)
        print("La fecha fue actualizada correctamente")
    elif int(opcion_mod) == 2:
        new_materia = input("Ingrese la materia: ")
        TDA_Inscripciones.modMateria(data_a_modificar, new_materia)
        print("La materia fue actualizada correctamente")
    elif int(opcion_mod) == 3:
        new_profesor = input("Ingrese la nombre del profesor: ")
        TDA_Inscripciones.modMateria(data_a_modificar, new_profesor)
        print("El profesor fue actualizado correctamente")
    elif int(opcion_mod) == 4:
        new_curso = input("Ingrese el curso: ")
        TDA_Inscripciones.modMateria(data_a_modificar, new_curso)
        print("El curso fue actualizado correctamente")
    elif int(opcion_mod) == 5:
        new_division = input("Ingrese la division del curso: ")
        TDA_Inscripciones.modMateria(data_a_modificar, new_division)
        print("La division fue actualizada correctamente")

    sobreescribir_inscripciones(inscripciones, data_a_modificar, alumno)


def menuModificar(inscripciones):
    alumno = input("Ingrese el alumno que desea modificar: ").lower()
    # acceder al diccionario que contiene el la inscripcion del alumno solicitado
    if alumno in inscripciones.keys():
        data_a_modificar = inscripciones[alumno]
        seguir = True
        while seguir == True:
            modificar(inscripciones, data_a_modificar, alumno)
            print("Desea modificar otra cosa?")
            opcion = input("Ingrese Si o No:").lower()
            if opcion == "si":
                seguir = True
            elif opcion == "no":
                break
            else:
                print("Ingrese una opcion valida")
                seguir = True

    else:
        print("Alumno no encontrado!")
        print("")


def menu_encargado(inscripciones):
    sel = 1
    while sel != 0:
        print("Seleccione que accion desea realizar:")
        print("1. Realizar la iscripcion de alumnos")
        print("2. Modificar la iscripcion de alumnos")
        print("3. Salir")

        opcionMenu = int(input("Ingrese una opcion: "))
        sel = opcionMenu
        if opcionMenu == 1:
            inscribir()
        elif opcionMenu == 2:
            try:
                menuModificar(inscripciones)
                print("Inscripcion modificada con exito")
                print("")
            except:
                print("No se pudo realizar la modificacion, intente nuevamente")
                print("")
        elif opcionMenu == 3:
            break
        else:
            print("Ingrese una opcion correcta")
            print("")
