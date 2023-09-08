import math 

def funcion():
    lista = []
    suma = 0
    suma_cuadrados = 0
    contador = 0
    while True:
        numero = input("Introduce un numero: ")
        if numero == "":
            break
        else:
            lista.append(float(numero))
            suma += float(numero)
            suma_cuadrados += float(numero)**2
            contador += 1
    media = suma/contador
    desviacion = math.sqrt((suma_cuadrados/contador)-(media**2))
    print("La media de los numeros introducidos es: " + str(media))
    print("La desviacion tipica de los numeros introducidos es: " + str(desviacion))
funcion()