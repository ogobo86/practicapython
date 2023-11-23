#Detectar un numero primo

def es_primo(numero):
    
    contador = 0

    for i in range (1, numero + 1):
        if i == 1 or i == numero:
            continue

         #Verifica que la divisio con lso numero haste el numero ingresado sea igual a 0    
        if numero % i == 0:
            contador += 1

    if contador == 0 :
        return True
    else:
        return False

def main():
    
    numero = int (input('Ingresa un numero : '))

    if es_primo(numero):
        print('Es primo')
    else:
        print('No es primo')

if __name__ == '__main__':
    main()