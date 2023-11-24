

def cambiar_letras(tipo):

    def mayusculas (texto):
        print (texto.upper())

    
    def minusculas (texto):
        print (texto.lower())

    if tipo == 'may':
        return mayusculas
    elif tipo == 'min':
        return minusculas
    

operacion = cambiar_letras('may')

operacion ('chachalaca')


def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print ("Hola")
        funcion(palabra)
        print ("adios")
    return otra_funcion

@decorar_saludo
def mayusculas (texto):
    print (texto.upper())

@decorar_saludo
def minusculas (texto):
        print (texto.lower())

minusculas ("Python")