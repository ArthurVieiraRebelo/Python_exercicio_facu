#Escreva uma função que receba como parâmetro um
#valor n inteiro e positivo e que calcule a seguinte
#soma: S = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n . A função
#deverá retornar o valor de S.

def soma(n1):
    soma = 0
    for i in range(1, n1 + 1):
        soma += 1/i
    return soma

n1 = int(input("Digite um número: "))

print(f"{soma(n1):.2f}")