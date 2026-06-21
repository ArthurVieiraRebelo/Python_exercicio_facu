# 8.	Implemente uma função que, dado um valor,
# retorne se esse valor pertence ou não a um vetor de
# inteiros.

def verificar_valor(vetor, valor):
    achou = False
    posicao = 0
    while not achou and posicao <= len(vetor) - 1:
        if vetor[posicao] == valor:
            achou = True
        posicao += 1
    return achou

print(verificar_valor([1, 2, 3], 5))