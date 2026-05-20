#Escrever uma função somarIntervalo(n1, n2) que
#retorna a soma dos números inteiros que existem
#entre n1 e n2 (inclusive ambos). A função deve
#funcionar inclusive se o valor de n2 for menor que n1.

def somar_intervalo(n1 , n2):
    intervalo = 0
    troca = 0
    if n2 < n1:
        troca = n1
        n1 = n2
        n2 = troca
    for i in range(n1 , n2 + 1):
        intervalo += i
    return intervalo

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print(somar_intervalo(n1 , n2))
