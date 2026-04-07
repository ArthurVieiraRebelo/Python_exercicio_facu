# 2.	Escreva um algoritmo que leia 20
# valores e encontre o maior e o menor deles.
# Mostre o resultado.

for i in range(5):
    valor = int(input("Digite um numero: "))
    if i == 0:
        maior = valor
        menor = valor
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
print(maior)
print(menor)