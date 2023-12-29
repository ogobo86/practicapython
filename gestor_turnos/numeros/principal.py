import numeros

def preguntar():

    print("Bienvenido a Farmacia Python")

    while True:
        print("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmeticos")
        try:
            mi_area = input ('Elija su area: ').upper()
            ['P','F', 'C'].index(mi_area)
        except ValueError:
            print('Esa no es una opcion valida')
        else:
            break
    
    numeros.decorador(mi_area)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres otro turno? [S] [N]: ").upper()
            ['S', 'N'].index(otro_turno)
        except ValueError:
            print("Esa no es una opcion valida\n")
        else:
            if otro_turno == "N":
                print("Gracias por su visita")
                break

inicio()
        