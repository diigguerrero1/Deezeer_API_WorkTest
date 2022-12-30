
# Esta funcion nos ayudara a quitar los elementos repetidos de un diccionario

def remover_duplicados(objetos):

    resultado = {}

    for k, v in objetos.items():
        if v not in resultado.values():
            resultado[k] = v 

    return resultado