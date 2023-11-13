class Persona :

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente (Persona):

    #CONTRUCTOR
    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    #METODOS
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido} \nBalance de la cuenta {self.numero_cuenta}: ${self.balance}."
    
    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print ("Deposito aceptado.")


    def retirar (self, monto_retirar):
        if self.balance >= monto_retirar:
            self.balance -= monto_retirar
            print("Retiro realizado.")
        else:
            print("No cuenta con fondos suficientes.")


def crear_cliente():
    nombre_cliente = input ("Ingrese su  nombre: ")
    apellido_cliente = input("Ingrese su apellido: ")
    numero_cuenta = input ("Ingrese su numero de cuenta: ")
    
    #creamos el objeto Cliente 
    cliente= Cliente(nombre_cliente, apellido_cliente, numero_cuenta)
    return cliente



def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)

    opcion = 0

    while  opcion != 's':
        print ('Elije: Depositar (D), Retirar (R), o Salir (S).')
        opcion = input()
        opcion.lower
        if opcion == "d": 
            monto_deposito = int (input("Monto a depositar: "))
            mi_cliente.depositar(monto_deposito)
        elif opcion == 'r':
            monto_retirar = int (input("Monto a retirar: "))
            mi_cliente.retirar(monto_retirar)
        print(mi_cliente)

    print ("Estimado usuario muchas gracias por preferir Banco 'x'")


inicio()