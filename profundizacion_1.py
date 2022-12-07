# CODE:34
# Funciones [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 3.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios con funciones y módulos
import random

'''
Enunciado:
Crear la función "lista_aleatoria"
Para este ejercicio utilizaremos el módulo random
Ejemplo de como obtener un numero aleatorio
entre inicio y fin
inicio <= numero <= fin
numero = random.randint(inicio, fin)

NOTA: Esta función ya se utilizó en uno de los ejemplos de clase
Documentación oficial de random
https://docs.python.org/3.7/library/random.html

Alumno:
- Realice una funcion llamada "lista_aleatoria" (fuera del blocke main)
la cual reciba como parámetro el rango de aceptación de la lista
"inicio y fin" y la cantidad de elementos que deseamos que
contenga la lista, es decir, la cantidad de elementos random a generar.

def lista_aleatoria (inicio, fin, cantidad)

- Dentro de la función deberá realizar un bucle que repita "cantidad"
veces esta operacion:
numero = random.randint(inicio, fin)

Cada valor generado lo debe guardar en una lista, recuerde:
1) Iniciar y crear esa lista vacia.
2) Para agregar nuevos elementos en la lista utiliza "append"

Finalmente dicha función debe retornar la lista de elementos random generados.
'''

# --------------------------------
# Aquí dentro definir la función lista_aleatoria

def lista_aleatoria(inicio, fin, cantidad):
    aleatorios = []
    for i in range (cantidad):
        numero = random.randint(inicio, fin)
        aleatorios.append(numero)
    return aleatorios
# --------------------------------

if __name__ == '__main__':
        print("Bienvenidos a otra clase de Inove con Python")
    
        inicio = 0
        fin = 10
        cantidad = 5
print(lista_aleatoria(inicio, fin, cantidad))
    # Alumno: Luego de crear la función invocarla en este lugar:

    # mi_lista_aleatoria = lista_aleatoria(inicio, fin, cantidad)

    # Imprimir en pantalla "mi_lista_aleatoria" que tendrá
    # los valores retornado por la función lista_aleatoria:

    # print(mi_lista_aleatoria)

print("terminamos")
