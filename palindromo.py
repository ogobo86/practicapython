
def palindromo (palabra):
    #quitamos espacios 
    palabra = palabra.replace(' ', '')
    #volvemos mayusculas a minusculas
    palabra = palabra.lower()

    palabra_invertida = palabra [::-1]

    if palabra == palabra_invertida:
        return True
    else:
        return False


#Funcion principal
def main():
    #Solicitamos al usuario 
    palabra = input ('Ingresa una palabra: ')
    #Invocamos la funcion para reconocer la palabra ingresada
    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print('Es palindromo')
    else:
        print('NO es palindromo')



#Punto de Entrada de la aplicacion
if __name__ == '__main__':
    main()