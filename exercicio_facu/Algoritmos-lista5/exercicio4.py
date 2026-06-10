# 4. Implemente uma função que ordene um vetor de inteiros de tamanho 10


def menor_valor(valores):
    valor_menor = -1
    for i in range(len(valores)):
        if valores[i] < 0:
            print("Não pode número negativo")
        else:
            if valores[i] < valor_menor:
                valor_menor = valores[i]
    return valor_menor

def ordenador(valor_menor):
    while vetor != []:
        menor_valor(vetor)
        ordenado.append(valor_menor)
        vetor.remove(valor_menor)

vetor = [ 4, 5, 3, 9, 1, 7, 18, 11, 10, 8 ]
ordenado = [ ]
print(menor_valor(vetor))
print(ordenador())