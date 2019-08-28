#Ejemplo 2.3: Pedirle al usuario que ingrese el la descripcion y el valor del articulo
 
import sqlite3 #base de datos nativa 
conexion=sqlite3.connect("bc.db") #conexion a la base de datos 
try: 
#Ejecute lo que esta en la tabla "articulos", lleva 3 comillas para indicar que se va a poner el codigo en varias lineas 
    conexion.execute(""" create table articulos (  
    codigo integer primary key AUTOINCREMENT, 
    description text, 
    precio real 
    )""") 
    print("se creo la tabla") 
except sqlite3.OperationalError: 
    print("ya existe") 
#Insertar dos valores (?,?) que en este caso corresponden a "naranja" y "20" 
#conexion.execute("insert into articulos(description,precio)values(?,?)",("naranja",20)) 
#Consolidar valor agregado naranja y 20 
#conexion.commit() 

#Mostrar contenido de la tabla Articulos 
curso=conexion.execute("select codigo,description,precio from articulos") 
#se pudo haber usado "row" en lugar de "fila" 
for fila in curso: 
	print(fila) 

#Pedirle al usuario que ingrese la descripcion y el precio 
description=input("Ingrese la descripcion del articulo") 
precio=float(input("Ingrese el precio del articulo")) 
conexion.execute("insert into articulos(description,precio)values(?,?)",(description,precio)) 
conexion.commit() 

#Cerrar la conexion con la base de datos, va al final de la tabla 
conexion.close()  
