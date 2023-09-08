ganador = []
for i in range(4):
    numero = int(input("Ingrese el numero ganador: "))
    ganador.append(numero)
ganador.sort()
print("Los numeros ganadores son de menor a mayor: ")
for numero in ganador:
    print(numero)

