from random import *

print ("Bienvenido al juego del 'Ahoracado'")
nombre = input ('¿Cúal es tu nombre? \n')
print (f"Bueno, {nombre}, he pensado un número entre 1 y 100. \n Cuentas con 8 (ocho) intentos para adivinar cuál crees que es el número\n")
intentos = 0
numero_secreto = randint (1,100)

while intentos <8 :
    x =  int (input("¿Cúal es el número secreto?: "))
    intentos+= 1

    if x not in range(1,101):
        print ("El número no se encuentra en el rango de 1 al 100")
        
    elif x > numero_secreto :
        print (f"La respuesta es incorrecta, el número es menor al número secreto.")

    elif x < numero_secreto :
        print (f"La respuesta es incorrecta, el número es mayor al número secreto")
        
    else :
        x == numero_secreto 
        print (f"¡Felicidades {nombre}!, haz logrado descrubir el número secreto: {x} \n En tan solo {intentos} intentos.")
        break
    
if x != numero_secreto :
    print (f"Lo siento haz terminado con los intentos, el número secretos es: {numero_secreto}")