#ya tenemos nuestro modulo instalado para conectarnos de python a mysql
import mysql.connector

#conexion
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'master_python'
)

# definir objeto de la conexión para hacer tareas
cursor = database.cursor(buffered=True)

#Consultar todos los registros dentro de la tabla
cursor.execute("select * from vehiculos where vehiculos.precio <= 22000")
result = cursor.fetchall()

#consultar solo el primero vehiculo
cursor.execute("select * from vehiculos where precio <= 150000.00")
result = cursor.fetchone()
print('primer result',result)

#eliminar registros de una tabla
cursor.execute("delete from vehiculos where marca = 'seat' ")
database.commit()
print(cursor.rowcount,'vehiculos deleted')

#actualizar registros de una tabla
cursor.execute("update vehiculos set precio = 100000 where marca = 'Renault'")
database.commit()