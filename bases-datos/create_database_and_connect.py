#ya tenemos nuestro modulo instalado para conectarnos de python a mysql
import mysql.connector

#conexion
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)
# comprobar conexion
#print(database)

#nuestra connecion la podemos llamar para hacer tareas
cursor = database.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute('SHOW DATABASES')

for bd in cursor:
    print(bd)
