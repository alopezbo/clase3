#Ejemplo 1.3 
#Crear base de datos con 3 columnas (Codigo, descripcion y precio). Para la columna codigo se genera un valor automaticamente. 

import sqlite3 #base de datos nativa 
conexion=sqlite3.connect("bc.db") #conexion a la base de datos 
try: 
#Ejecute lo que esta en la tabla articulos, lleva 3 comillas para indicar que se va a poner el codigo en varias lineas
    conexion.execute("""create table articulos(
                                codigo integer primary key AUTOINCREMENT, 
                                description text, 
                                precio real 
                                )""") 
    print("se creo la tabla") 
except sqlite3.OperationalError:
    print("ya existe") 

#Insertar dos valores (?,?) que en este caso corresponden a "naranja" y "20" 
conexion.execute("insert into articulos(description,precio)values(?,?)",("naranja",20)) 

#Consolidar valor agregado 
conexion.commit() 

#Mostrar contenido de la tabla Articulos 
curso=conexion.execute("select codigo,description,precio from articulos") 
for fila in curso: 
    print(fila) 

#Cerrar la conexion con la base de datos 
conexion.close()  
