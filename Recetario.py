import os
from pathlib import Path
from os import system

# Mostrar menu inicio

mi_ruta = Path (Path.home(),"desktop","Recetas" )


def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("*/*.txt"):
        contador += 1
        return contador
    

def inicio ():
    system("clear")
    print ("* " * 24)
    print ("* " * 5 + " Bienvenido al rerecetario " + " *" * 5 )
    print ("* " * 24)
    print ("\n")
    print (f"Las recetas se encentras en {mi_ruta}")
    print (f"El total de Recetas: {contar_recetas(mi_ruta)}")

    eleccion_menu = "x"
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print ("Elige una opcion: ")
        print ('''
        [1]. Leer Receta
        [2]. Crear Receta Nueva
        [3]. Crear Categoria Nueva
        [4]. Eliminar Receta
        [5]. Eliminar Categoria
        [6]. Salis del Programa
        ''')
        eleccion_menu = input ()
        return int(eleccion_menu)


def mostrar_categorias (ruta):
    print ("Categorias:")
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print (f"[{contador}]. {carpeta_str}")
        lista_categorias.append(carpeta)
        contador +=1

    return lista_categorias

def elegir_categoria (lista):
    eleccion_correcta = 'x'

    while not eleccion_correcta.isnumeric() or int (eleccion_correcta) not in range(1, len(lista) +1 ):
        eleccion_correcta = input("\n Elige una categoria: ")
    
    return lista[int(eleccion_correcta)-1]

def mostrar_receta (ruta):
    print ("Estas son las recetas: ")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob('*.txt'):
        receta_str =  str(receta.name)
        print (f"[{contador}]. {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 'x'

    while not eleccion_receta.isnumeric() or int (eleccion_receta) not in range(1, len(lista)+1):
        eleccion_receta = input ('\n Elige una receta: ')
    return lista[int(eleccion_receta)-1]    

def leer_receta (receta):
    print (Path.read_text(receta))

def crear_receta (ruta):
    existe = False

    while not existe:
        print ('Escribe el nombre de tu receta: ')
        nombre_receta = input() + '.txt'
        print ("Escribe tu nueva receta: ")
        contenido_receta = input ()
        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists (ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print (f"Tu recera {nombre_receta}, ha sido creada")
            existe = True
        else:
            print ("Lo siento, esa receta ya existe")


def crear_categoria (ruta):
    existe = False

    while not existe:
        print ('Escribe el nombre de la nueva Categoria: ')
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists (ruta_nueva):
            Path.mkdir(ruta_nueva)
            print (f"Tu categoria {nombre_categoria}, ha sido creada")
            existe = True
        else:
            print ("Lo siento, esa categoria ya existe")


def eliminar_receta (receta):
    Path(receta).unlink()
    print(f'la receta {receta.name}, ha sido eliminada')


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print (f'La Categoria {categoria.name}, ha sido eliminada')


def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input ("\n Presione V para volver al menu")



finalizar_programa = False

while not finalizar_programa:

    menu = inicio()

    if menu == 1:
        miscategorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(miscategorias)
        mis_recetas = mostrar_receta(mi_categoria)
        mi_receta =  elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
        
    elif menu == 2:
        miscategorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(miscategorias)
        crear_receta(mi_categoria)
        volver_inicio()
        
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
        
    elif menu == 4:
        miscategorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(miscategorias)
        mis_recetas = mostrar_receta(mi_categoria)
        mi_receta =  elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
        
    elif menu == 5:
        miscategorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(miscategorias)
        eliminar_categoria (mi_categoria)
        volver_inicio()
        
    elif menu == 6 :
        finalizar_programa = True