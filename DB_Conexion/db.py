import mysql.connector

midb = mysql .connector.connect(
    host='localhost',
    user='root',
    password='',
    database='prueba'
)

# Un cursos es un objeto que permite interactuar con la DB
# mediante un SQL. 
cursor =midb.cursor()

# LISTAR 
#cursor.execute('SELECT * FROM usuario')
#resultado = cursor.fetchall()
#print (resultado)
#unresultado = cursor.fetchone()
#print (unresultado)

# INSERTAR
#sql = 'INSERT INTO usuario (email, username, edad) values (%s, %s,%s)'
#values = ('ngonzalez@algo.com', 'ngonzalez', 39)
#cursor.execute(sql,values)
# Es necesario hacer commit para que la transaccion se refleje en la DB
#midb.commit()
# Validacion si fue correcto da 1
#print (cursor.rowcount)

# UPDATE 
#sql = 'update usuario set edad = %s where id= %s'
#values = (35,4)
#cursor.execute(sql,values)
#midb.commit()
#print(cursor.rowcount)

# DELETE

sql = 'delete from usuario where id =%s'
values = (4, )
cursor.execute(sql,values)
midb.commit()
