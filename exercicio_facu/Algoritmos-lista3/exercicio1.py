# 1.	Escrever um algoritmo que lê 10 valores e conte
# quantos destes valores são negativos, escrevendo
# esta informação.

negativos = 0

for i in range(10):
    valor = int(input("Digite um valor: "))
    if valor < 0:
        negativos =+ 1
print(f"A qunatidade de números negativos são {negativos}")