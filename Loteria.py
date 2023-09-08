#Escribir un programa que pregunte al usuario los números ganadores de la lotería, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor. 
ganador = []
for i in range(4):
    numero = int(input("Ingrese el numero ganador: "))
    ganador.append(numero)
ganador.sort()
print("Los numeros ganadores son de menor a mayor: ")
for numero in ganador:
    print(numero)

