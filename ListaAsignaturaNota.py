Asignatura = ("Matematicas", "Fisica", "Quimica", "Historia", "lenguaje")
notas = []
for asignatura in Asignatura:
    nota = input("Que nota sacaste para " + asignatura + ": ")
    notas.append(nota)
for i in range(len(Asignatura)):
    print("En " + Asignatura[i] + " has sacado " + notas[i])