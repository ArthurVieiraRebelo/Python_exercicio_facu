#Implemente uma função que retorne o menor elemento de um vetor de
#inteiros.

def menor_valor(valores):
    valor_menor = valores[2]
    for i in range(len(valores)):
        if valores[i] < 0 :
            print("Não pode número negativo")
        else:
            if valores[i] < valor_menor:
                valor_menor = valores[i]
    return valor_menor


valores = [1 , 7 , 10 , 2 , 8 , 3]

print(menor_valor(valores))