#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios. 
lista = [50, 75, 46, 22, 80, 65, 8]
lista.sort()
print("El precio menor es: " + str(lista[0]))
print("El precio mayor es: " + str(lista[-1]))

