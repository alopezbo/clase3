#Ejemplo 4-3
#Cree un software con dos bases de datos, la primera con el nombre "empleados" y la segunda "transacciones"
#En la base de datos empleados, cree dos tablas con los nombres:
#1)Empleados y 2)Horarios. En la tabla Empleados cree 3 casillas:
#1)Nombre,2)cedula y 3)puesto
#En la base de datos transacciones, cree 3 tablas: 1)Inventario,2)efectivo y 3)activos con las casillas en
#Inventario: 1)entrada,2)salida y 3)saldo.
#Solicitele al usuario ingresar los datos de un nuevo empleado o ver los empleados que ya hay
import sqlite3
#Crear base de datos empleados.db
cnxnempleados=sqlite3.connect("empleados.db")
#Crear tabla empleados
try:
cnxnempleados.execute("""create table empleados (
nombre text,
cedula int,
puesto text
)""")
print("se creo la tabla empleados")
except sqlite3.OperationalError:
print("ya existe la tabla empleados")
#Crear tabla horarios
try:
cnxnempleados.execute("""create table horarios (
horario real
)""")
print("se creo la tabla horarios")
except sqlite3.OperationalError:
print("ya existe la tabla horarios")
#Crear base de datos transacciones.db
cnxntransacciones=sqlite3.connect("transacciones.db")
#Crear tabla inventario
try:
cnxntransacciones.execute("""create table inventario (
entrada real,
salida real,
saldo real
)""")
print("se creo la tabla inventario")
except sqlite3.OperationalError:
print("ya existe tabla inventario")
#Crear tabla efectivo
try:
cnxntransacciones.execute("""create table efectivo (
efectivo real
)""")
print("se creo la tabla efectivo")
except sqlite3.OperationalError:
print("ya existe tabla efectivo")
#Crear tabla activos
try:
cnxntransacciones.execute("""create table activos (
activos real
)""")
print("se creo la tabla activos")
except sqlite3.OperationalError:
print("ya existe tabla activos")
opcion=int(input("Desea agregar nuevo empleado? \n 1-Si \n 2-Desplegar la tabla EMPLEADO"))
if opcion==1:
nombre=input("Ingrese nombre de EMPLEADO")
cedula=int(input("Ingrese numero de cedula del EMPLEADO"))
puesto=input("Ingrese nombre del puesto del EMPLEADO")
cnxnempleados.execute("insert into empleados(nombre,cedula,puesto)values(?,?,?)",(nombre,cedula,puesto))
cnxnempleados.commit()
elif opcion==2:
mostrarempleados=cnxnempleados.execute("select nombre,cedula,puesto from empleados")
for fila in mostrarempleados:
print(fila)
cnxntransacciones.close()
cnxnempleados.close()