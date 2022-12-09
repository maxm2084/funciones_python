# CODE:33
# Funciones [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con funciones

# Objetivo:
# Reutilizar código escrito en desafios anteriores

# --------------------------------
# Alumno:
# Aquí copiar la función "generar_invitados"
# ya elaborada
def generar_invitados(invitados):
      
    while str.isdecimal(invitados) is False or int(invitados)<1 :
        invitados = input("Error,debe ingresar un numero mayor a cero: ")
       
    listado = []  
    for i in range(int(invitados)):
        ingreso = input(f"Ingrese el nombre del invitado {i+1}/{invitados}: ")
        listado.append(ingreso)
    return listado
# --------------------------------

# --------------------------------
# Alumno:
# Aquí copiar la función "ordenar"
# ya elaborada
def ordenar(lista):
    lista.sort()
    return lista
# --------------------------------

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")

    # Alumno: 
    # Copiar las funciones "generar_invitados" y "ordenar"
    # creadas en los ejercicios anteriores
    # Deberá copiarlas fuera del bloque "__main__" como se detalla
    # al comienzo del archivo
    # --> El objetivo es generar una lista de invitados y ordenarla

    # Luego de copiar las funciones, invocarla en este lugar:

    # 1) Primero generar una lista de invitados con "generar_invitados"
    #    Almacenar el retorno en "lista_invitados"
    invitaciones = input("Ingrese la cantidad de invitados: ")
    

    # lista_invitados = generar_invitados()
    lista_invitados = generar_invitados(invitaciones)
    # 2) Luego ordenar la lista de invitados con "ordenar"
    #    --> Pasar como parámetro la "lista_invitados"
    #    --> Retornar la lista de invitados ordenada
    #    --> Almacenar el retorno en "lista_invidatos_ordenada"

    # lista_invidatos_ordenada = ordenar(lista_invitados)
    print(ordenar(lista_invitados))
    # Imprimir en pantalla "lista_invidatos_ordenada":

    print("terminamos")
