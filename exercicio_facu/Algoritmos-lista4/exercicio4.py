#Escrever uma função contarImpar(n1, n2) que retorna
#o número de inteiros ímpares que existem entre n1 e
#n2 (inclusive ambos, se for o caso). A função deve
#funcionar inclusive se o valor de n2 for menor que n1.

def contar_impar(n1 , n2):
    troca = 0
    impar = 0
    if n2 < n1:
        troca = n1
        n1 = n2
        n2 = troca
    for i in range(n1 , n2 + 1):
        if not i % 2 == 0:
            impar += 1
    return impar

n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))
print(contar_impar(n1 , n2))
