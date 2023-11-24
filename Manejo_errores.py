

def suma ():
    n1 = int (input("Ingresa el numero 1: "))
    n2 = int (input("Ingresa el numero 2: "))

    print ("Gracias por sumar")


suma()

'''try:
    # Codigo que queremos probar
    suma ()

except:
    # Codigo a ejecutrar si no hay un error
    print ("Algo no ha salido bien")
else:
    # Codigo a ejecutar si no hay un error
    print ("Hiciste todo bien")
finally: 
    # Codigo que se va a ejecutar de todos modos. 
    print ("Eso fue todo")'''


def pedir_numero ():
    while True:
        try:
            numero = int ( input ("Dame un numero: "))
        except:
            print ("Eso no es un numero")
        else:
            print (f"ingresaste el numero {numero}.")
            break
    
    print ("Gracias")


pedir_numero()
