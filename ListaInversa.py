#programa que almacene una lista del 1 al 10 y la muestre en orden inverso separados por comas.
lista = [1,2,3,4,5,6,7,8,9,10]
lista.reverse()
for numero in lista:
    print(numero, end=", ")