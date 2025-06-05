


registro_central =[]

while True:
    print ( f'****** Bienvenido *******')
    print (f'Tienes las siguientes opciones.')
    print ("1. Registra un Estudiante.")
    print ("2. Muestra un registro.")
    print ('3. Salir.')

    opcion = input ("Selecciona una opcion: \n")

    if opcion == '1':
        # Variables de registro.
        nombre = input("Ingresa el nombre del estudiante: ")
        edad = int (input("Ingresa la edad del estudiante: "))
        curso = input ("Ingresa el curso del estudiante: ")

        # Asignacion de valores en diccionario y se manda a lista.
        estudiante = {'Nombre': nombre, "Edad": edad, "Curso": curso }
        registro_central.append(estudiante)
        print("Se registro el estudiante de manera correcta.\n")
    
    elif opcion == '2':
        if registro_central:
            print ("\nRegistro de Estudiantes: \n")
            for estudiante in registro_central:
                print (f'Nombre: {estudiante["Nombre"]}, Edad: {estudiante["Edad"]}, Curso:Ju {estudiante["Curso"]}\n')
        else:
            print ("El registro esta vacio.")
    elif opcion == '3':
        print('Saliendo del programa.')
        break
    else:
        print('Opcion incorrecta, intente de nuevo.')