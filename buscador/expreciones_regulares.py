import re
'''
\d = digito numerico
\w = caracter alfanumerico ejemplo: \w\w\w-\w\w  asb-25 | sol-do
\s = espacio en blanco ejemplo: numero\s\d\d  numero 25
\D = NO numerico 
\W = NO alfanumerico ejemplo: \W\W\W #+=
\S = NO es un espacio en blanco ejemplo: \S\S\S\S 1234

CUANTIFICADORES
+  | 1 o mas veces ejemplo: codigo_\d-\d+ codigo_5-5
{n} | se repite n veces ejemplo: \d-\d{4} 1-2678
{n,m} | se repite de n a m veces ejemplo: \w{3,5} hola
{n,} | se repite de n hacia arriba ejemplo: -\d{4,}-  -5235-
* | 0 o mas veces ejemplo: \w\s*\w a    b
? 1 o ninguna ejemplo: casas? casa
'''
#PUEDES BUSCAR TEXTO 
texto = "Si necesutas ayuda llama al (658)-598-9977 las 24 horaqs al servicio de ayuda online" 
patron = 'ayuda'
busqueda = re.findall(patron, texto)
print (busqueda)
for hallazgo in re.finditer(patron, texto):
    print (hallazgo.span())

#PUEDES IDENTIFICAR NUMEROS
texto = 'llama al 564-525-6588 ya mismo'
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado =  re.search(patron, texto)
print (resultado.group(1))

#PODRIAS VALIDAR UNA CLAVE
clave = input ("Clave: ")
patron = r'\D{1}\w{7}'
chequear = re.search(patron, clave)
print(chequear)

texto = 'No atendemos los lunes por la tarde'

buscar = re.search(r'lunes | martes', texto)
buscar = re.search(r'....demos', texto)
print (buscar)