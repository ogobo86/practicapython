def numeros_perfumeria():
    for n in range(1,100000):
        yield f'P - {n}'

def numeros_farmacia():
    for n in range(1,100000):
        yield f'F - {n}'

def numeros_cosmetica():
    for n in range(1,100000):
        yield f'C - {n}'


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(area):

    print("\n" + "*" * 23)
    print("Su numero es:")
    if area == "P":
        print(next(p))
    elif area == "F":
        print(next(f))
    else:
        print(next(c))

    print ("ESpere y en la brevedad sera atendidio")
    print ("*" * 23 + "\n")


