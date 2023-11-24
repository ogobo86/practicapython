import unittest
import cambia_texto


class ProbarCambiaTexto(unittest.TestCase):


    def test_mayuculas(self):

        # Palabra es un ejemplo de prueba para el test
        palabra = 'buen dia'

        # Usamos la funcion del modulo cambia_texto para comprobar la funcionalidad
        resultado = cambia_texto.todo_mayusculas(palabra)

        # Comprobacion del funcionamiento y verificacion
        self.assertEqual(resultado, 'Buen Dia')



if __name__ == '__main__':
    unittest.main()
