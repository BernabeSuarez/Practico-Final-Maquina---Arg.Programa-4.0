# Inscripcion
# a fecha, nombre del estudiante, nombre de la materia, nombre del profesor, curso, división y la nota


def inscribir(fecha, nombre, materia, profesor, curso, division, nota=-1):
    return {
        "fecha": fecha,
        "nombre": nombre,
        "materia": materia,
        "profesor": profesor,
        "curso": curso,
        "division": division,
        "nota": nota,
    }


def getFecha(inscripcion):
    return inscripcion["fecha"]


def modFecha(inscripcion, fecha):
    inscripcion["fecha"] = fecha


def getNombre(inscripcion):
    return inscripcion["nombre"]


def modNombre(inscripcion, nombre):
    inscripcion["nombre"] = nombre


def getMateria(inscripcion):
    return inscripcion["materia"]


def modMateria(inscripcion, materia):
    inscripcion["materia"] = materia


def getProfesor(inscripcion):
    return inscripcion["profesor"]


def modProfesor(inscripciones, profesor):
    inscripcion["profesor"] = profesor


def getCurso(inscripcion):
    return inscripcion["curso"]


def modCurso(inscripcion, curso):
    inscripcion["curso"] = curso


def getDivision(inscripcion):
    return inscripcion["division"]


def modDivision(inscripcion, division):
    inscripcion["division"] = divison


def getNota(inscripcion):
    return inscripcion["nota"]


def modNota(inscripcion, nota):
    inscripcion["nota"] = nota


def modInscripcion(inscripciones, data_a_modificar, alumno):
    inscripciones[alumno] = data_a_modificar
    new_file = list(inscripciones.values())
    return new_file


def sobreescribir_inscripciones(inscripciones, data_a_modificar, alumno):
    new_file = TDA_Inscripciones.modInscripcion(inscripciones, data_a_modificar, alumno)
    archivo = open("Inscripciones.txt", "w")
    for item in new_file:
        data = list(item.values())
        inscripcion_personal = ",".join(data)
        archivo.write(inscripcion_personal)
        archivo.write("\n")
    archivo.close()
