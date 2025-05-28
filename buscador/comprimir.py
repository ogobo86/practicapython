import zipfile
#IMPORTANTE debes de colocarte en el directorio correspondiente
#COMPRIMIR
mi_zip = zipfile.ZipFile('Archivo_comprimido.zip', 'w')
mi_zip.write('Documento_A.txt')
mi_zip.write('Documento_B.txt')
mi_zip.close()
#DESCOMPRIMIR
zip_abierto = zipfile.ZipFile('Archivo_comprimido.zip', 'r')
zip_abierto.extractall()

#CON SHUTIL
'''
import shutil

#COMPRIMIR
carpeta_origen = 'RUTA_A_COMPRIMIR'
archivo_destino = 'Todo_Comprimido'
shutil.make_archive(archivo_destino, 'zip'. carpeta_origen)

#DESCOMPRIMIR
shutil.unpack_archive('Todo_Comprimido.zip', 'Extraccion Terminada', 'zip' )
'''