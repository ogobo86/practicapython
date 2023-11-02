#Pequeño bloque de codigo para entender estructura de control 

n = int ( input ('Ingrese un número entero: '))


if n != 0: 
    #Esta lpinea de codigo verifica si es valor insertado por el usuario es mayor a 0
    if n > 0 : 
        #Si el número ingresado por el usuario al diviirlo entre dos y el residuo es igual 0, es un número par. 
        if n % 2 == 0 :
            print (f'El número {n} es PAR POSITIVO')
        
        else: 
            print (f'El número {n} es IMPAR POSITIVO')
    else:
    #En caso de ser menor a 0 se ejecuta esta estructura de codigo.    
        if n % 2 == 0 : 
            print ( f'El número {n} es PAR NEGATIVO')

        else :
            print ( f'El número {n} es IMPAR NEGATIVO')

else: 
    print (f'El número {n} es NEUTRO')