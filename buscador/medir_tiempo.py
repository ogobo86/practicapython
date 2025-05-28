import timeit
#Identifica el tiempo de ejecucion de un bloque de codigo 

#import time
#time permite establecer marcas de tiempo, requiere de dos variables INICIO y FINAL

def prueba_for (numero):
    lista = []
    for num in range (1, numero + 1):
        lista.append(num)
    return lista


def prueba_while (numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista

#Pruebas con TIME
'''
inicio = time.time()
prueba_for(1500000)
final = time.time()
print (final - inicio)

inicio_while = time.time()
prueba_while(1500000)
final_while = time.time()
print (final_while - inicio_while)
'''

#Pruebas con TIMEIT

declaracion ='''
prueba_for(10)
'''

mi_setup = '''
def prueba_for (numero):
    lista = []
    for num in range (1, numero + 1):
        lista.append(num)
    return lista
'''

duracion = timeit.timeit(declaracion, mi_setup, number = 1000000)
print (duracion)

declaracion_while = '''
prueba_while(10)
'''
mi_setup_while = '''
def prueba_while (numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''

duracion_while = timeit.timeit(declaracion_while, mi_setup_while, number = 1000000)
print (duracion_while)
