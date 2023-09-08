#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir. 

Asignaturas = ["Matematicas", "Fisica", "Quimica", "HIstoria", "Lengua"]
asignatura = []
for materia in Asignaturas:
    nota = float(input("Que nota tienes en " + materia + ": "))
    if nota >= 11:
        asignatura.append(materia)
for materia in asignatura:
    Asignaturas.remove(materia)
print("Tienes que repetir " + str(Asignaturas))