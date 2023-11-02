from random import shuffle
#lista inicial 
palitos = ["-", "--", "---", "----"]

#Mezla palitos
def mezclar (lista):
    shuffle(lista)
    return lista

#pedirl intento 
def probar_suerte ():
    intento = 0
    while intento not in [1, 2, 3, 4]:
        intento = int(input ("Elige un número del 1 al 4: "))
    return intento

# Comprobar intento 
def chequear_intento (lista, intento): 
    if lista [intento - 1] == "-":
        print ( "A lavar los platos.")
    else:
        print ("Esta vez te has salvado.")

    print(f"Te ha tocado {lista[intento-1]}")

palitos_mezclador = mezclar (palitos)
seleccion = probar_suerte ()
chequear_intento (palitos_mezclador, seleccion)
#
