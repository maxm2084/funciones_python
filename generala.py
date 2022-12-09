# Python Inicial [Python]
# Ejercicio integrador

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

'''
Enunciado:
Este ejercicio representa ya un problema que forma parte de un juego
Lo que se desea realizar es una parte del juego "la generala".
El enunciado está armado a modo de guía, pueden resolver el problema
de otra forma.
Si tienen dudas sobre el enunciado o alguno de los puntos por favor
comuníquelo por el campus y lo discutiremos entre todos, ya que siempre
puede haber varias interpretaciones de un mismo enunciado.

Deberá realizar una lista para guardar 5 dados, guardar los números
sacados en esa tirada de de dados (son 5 dados, cada uno del número 1 al 6)

1) El jugador tira los dados y saca 5 números aleatorios, puede usar
la función de "lista_aleatoria" para generar dichas lista de números
(la función "lista_aleatoria" se creó en los ejercicios de profudización de funciones)

Esa lista de datos generada aleatoriamente se llamará "dados_tirados"
Lista "dados_tirados" se utiliza para guardar 5 dados, cada dado es de 6 caras,
es decir que cada dado puede valer un número de 1 a 6.

2) Luego debe analizar los 5 números y ver cual es el número que
más se repitio entre los 5 dados.
Debe usar la función de Python "max" con la "key" de list.count para
determinar cual fue el número que más se repitió en esa tirada. 
Consultar los ejemplos de anexo de la clase de funciones en donde se realizó esta operación con "max"

3) Una vez reconocido el número más repetido entre los 5 dados,
debe guardar en una variable aparte llamada "contador_generala"
cuantas veces se repitió hasta ahora el número más repetido. 
Ese número será el candidato para buscar sacar generala.

Si por ejemplo salió 4-4-2-1-4, debe quedarse con esos tres "4",
por lo tanto el "contador_generala" valdrá 3, porque el primer número
más repetido fue 4, y este número salio tres veces en la primera tirada.

4) Debe volver a tirar los dados, generar nuevos
números aleatorios.
Si en el contador "contador_generala" tengo 3 dados guardados
significa que ahora deberé tirar solo dos dados (5-3). 
Es decir que en este caso debería generar solo dos números
aleatorios nuevos con "lista_aleatoria"
Ahora tendré una nueva lista de "dados_tirados", en este caso
de dos nuevos números aleatorios entre 1 y 6 representando a los dados
tirados.

5) Luego de tirar nuevamente los datos en el paso anterior,
por ejemplo digamos que salieron los números: 4-1
Debo volver a contar cuantas veces aparece el número "4",
ya que es el número que estoy buscando almacenar para llegar a generala.
Se deberá aumentar el contador por cada cuatro que haya salido en la tirada.
Sino salió el "4" vuelvo a tirar sin aumentar el contador (repetir el punto 4)

5) Debe repetir este proceso hasta que el contador "contador_generala"
haya llegado a 5, es decir, he sacado 5 números iguales

NOTA: Recordar que en este ejemplo se buscó alcanzar la generala con "4" porque
fue el primero número más repetido en la primera tirada. Tener eso en cuenta que el
número que deberá buscar para alcanzar la generala depende de cual fue el más repetido
en la primera tirada.
'''

import random
import time

# --------------------------------
# Dentro de esta sección copiar y crear
# todas las funciones que utilice
def lista_aleatoria(inicio, fin, cantidad):
    aleatorios = []
    for i in range (cantidad):
        numero = random.randint(inicio, fin)
        aleatorios.append(numero)
    return aleatorios

# Esta funcion la encontre en internet (no es de elaboracion propia)
def countdown(num_of_secs):
    while num_of_secs:
        m, s = divmod(num_of_secs, 60)
        min_sec_format = '{:02d}:{:02d}'.format(m, s)
        print(min_sec_format, end=' Seg ')
        time.sleep(1)
        num_of_secs -= 1
        
    print('Los dados han sido tirados.')
# --------------------------------

if __name__ == '__main__':
    print("¡El juego de la generala!")
    print("Se tiran los dados¡")
    countdown(3)
    # A partir de aquí escriba el código que
    # invoca a las funciones y resuelve el enunciado
    # Leer el enunciado con atención y consultar cualquier duda
contador_generala = 0

dados_tirados=[]

dados_tirados = lista_aleatoria(1,6,5-contador_generala)

print(dados_tirados)


num_repetido = max(set(dados_tirados), key= dados_tirados.count)
print("-------------------------------")
print(f"El numero repetido es: {num_repetido}")

contador_generala = dados_tirados.count(num_repetido)
print("-------------------------------")

print(f"El contador esta en {contador_generala}/5")

while contador_generala < 5:
    print("Se tiran los dados¡")
    countdown(3)
    dados_tirados=[]

    dados_tirados = lista_aleatoria(1,6,5-contador_generala)

    print(dados_tirados)

    num_igual = num_repetido
    print("-------------------------------")
    print(f"El numero buscado es : {num_igual}")
    contador_generala += dados_tirados.count(num_igual)
    print("-------------------------------")
    print(f"El contador esta en {contador_generala}/5")

    if contador_generala == 5:
        print("GENERALA¡¡¡")


   