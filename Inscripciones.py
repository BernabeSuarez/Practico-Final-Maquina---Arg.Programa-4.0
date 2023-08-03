def getInscripciones():
    f = open("Inscripciones.txt")
    data = f.read().rstrip().split("\n")
    f.close()

    for item in data:
        info = item.split(",")
        alumno = {}
        alumno["fecha"] = info[0]
        alumno["nombre"] = info[1]
        alumno["materia"] = info[2]
        alumno["profesor"] = info[3]
        alumno["curso"] = info[4]
        alumno["division"] = info[5]
        alumno["nota"] = info[6]
        inscripciones[info[1]] = alumno
