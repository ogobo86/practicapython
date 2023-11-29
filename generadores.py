# Funcion normal 
def mi_funcion():
    return 4

# GENERADOR
def mi_generador():
    yield 4
#yield mantiene a la espera para generarlo en el momento indicado


print (mi_funcion())
print (mi_generador())

g = mi_generador()

print (f"En esta impresion con el uso de next(),podemos imprimir el valor de yield ya que se esta solicitando {next(g)}.")

def mi_funcion1():
    lista = []
    for x in range(1,5):
        lista.append(x * 10)
    return lista
def mi_generador1 ():
    for x in range(1,5):
        yield x * 10

generador = mi_generador1()
print(mi_funcion1())
#Tener en cuenta que el uso de YIELD generar un error al iterar SOLO UN ELEMENTO
print(next(generador))
print(next(generador))

def mi_generador3 ():
    x = 1
    yield x

    x+=1
    yield x

    x += 1
    yield x

guarda  = mi_generador3()

#YIEL RETIENE LA INFORMACION HASTA QUE SE SOLICITADA
print(next(guarda))
print(next(guarda))
print ("Texto")
print(next(guarda))
