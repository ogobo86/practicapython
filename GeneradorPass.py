import random

def generar_pass():

    mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','V','W','X','Y','Z']
    minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','v','w','x','y','z']
    simbolos = ['#', '$', '%', '&']
    numeros = ['1','2','3','4','5','6','7','8','9','0']

    #Creamos una lista con el contenido de las listas para poder acceder al contenido de manera aleatoria
    caracteres = mayusculas + minusculas + simbolos + numeros

    contra = []

    #RANGE cumple la funcion de la longitud de caracteres para generar el pass
    for i in range  (15):
        #Choice accede a la lista caracteres y obtiene uno de manera random
        caracter_random = random.choice(caracteres)
        contra.append(caracter_random)
    
    #Convierte la lista a str
    contra = "".join(contra)

    return contra

def main ():
    contrasena = generar_pass()
    print (f'Generamos la contrasena siguiente: ', contrasena)


if __name__ == '__main__':
    main()