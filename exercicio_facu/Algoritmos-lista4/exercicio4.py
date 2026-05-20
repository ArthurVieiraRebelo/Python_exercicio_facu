# 4.	Escrever uma função contarImpar(n1, n2)
# que retorna o número de inteiros ímpares que
# existem entre n1 e n2 (inclusive ambos, se for
# o caso). A função deve funcionar inclusive
# se o valor de n2 for menor que n1.
from pip._internal.utils import retry

def ordenar_numeros(n1, n2):
    if n1 < n2:
        return n1, n2
    else:
        return n2, n1

def contar_impar(n1, n2):
    n1, n2 = ordenar_numeros(n1, n2)
    quantidade = 0
    for i in range(n1, n2 + 1):
        if i % 2 != 0:
            quantidade += 1
    return quantidade

print(contar_impar(20,10))