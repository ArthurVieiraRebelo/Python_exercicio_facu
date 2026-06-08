#Implemente uma função que retorne o maior elemento de um vetor de
#inteiros.


def maior_valor(valores):
    valor_maior = 0
    for i in range(len(valores)):
        if valores[i] < 0 :
            print("Não pode número negativo")
        else:
            if valores[i] > valor_maior:
                valor_maior = valores[i]
    return valor_maior


valores = [1 , 7 , 10 , 2 , 8 , 3]

print(maior_valor(valores))