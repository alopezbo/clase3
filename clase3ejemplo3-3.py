# Ejemplo3-3
# Cree un software que le solicite al usuario el nombre del estudiante y lo guarde 
# en una base de datos no relacional. Al final debe mostrarle al usuario la lista 
# de todos los estudiantes 
 
#nombre=input("Ingrese nombre de la persona") 
#archivo=nombre+".txt" 
#datos=open(archivo,"w") 
#datos.write(nombre) 
#datos.close() 
 
#|||||||||||||||||||||||||||||||||||||||||| 
increment=0 
while True: 
    opcion=int(input("Ingrese numero")) 
if opcion==1: 
    estudiante=input("") 
    increment +=1 
    archivo=str(increment)+".txt" 
    f=open(archivo,"w") 
    f.write(estudiante) 
    f.close() 
elif opcion==2: 
    for lista in increment: 
        f=open(lista+'.txt',"r") 
        f.read(estudiante) 
        f.close() 
        break 
