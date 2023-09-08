#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante. 
def funcion():

    abecedario = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
    abecedario_final = []
    for i in range(len(abecedario)):
        if i%3!=0:
            abecedario_final += abecedario[i]

    print(abecedario_final)

funcion()  