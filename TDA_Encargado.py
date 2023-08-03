# Encargado nombre dni


def crearEncargado(nombre, dni):
    return {"nombre": nombre, "DNI": dni}


def getNombre(encargado):
    return encargado["nombre"]


def modNombre(encargado, nombre):
    encargado["nombre"] = nombre


def getDni(encargado):
    return encargado["DNI"]


def modDni(encargado, dni):
    encargado["DNI"] = dni
