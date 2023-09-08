#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario. 
Asignatura = ("Matematicas", "Fisica", "Quimica", "Historia", "lenguaje")
notas = []
for asignatura in Asignatura:
    nota = input("Que nota sacaste para " + asignatura + ": ")
    notas.append(nota)
for i in range(len(Asignatura)):
    print("En " + Asignatura[i] + " has sacado " + notas[i])