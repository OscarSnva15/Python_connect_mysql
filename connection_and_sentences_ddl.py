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
cursor = database.cursor()

#crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    id int(10) auto_increment not null,
    marca varchar(20) NOT NULL,
    modelo varchar(20) NOT NULL,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY (id)
)
""")
database.commit()

#comprobar
cursor.execute('SHOW TABLES')

for table in cursor:
    print(table)

#insertar datos
cursor.execute("""
INSERT INTO vehiculos VALUES(
     null,
    'Renault',
    'Dinamique',
    185000
)
""")
database.commit()

#insertar datos de manera masiva
coches = [
    ('seat', 'Ibiza', 12500),
    ('Citroen', 'Saxo', 15000),
    ('Renault', 'Clio', 22000),
    ('Mercedes', 'Clase c', 35000)
]

#insertar el lotes
cursor.executemany('INSERT INTO vehiculos values (null, %s, %s, %s)', coches)
database.commit()

#cerrar conexion
cursor.close()
