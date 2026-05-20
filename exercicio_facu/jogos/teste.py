n1 = int(input("Digite um numero inteiro: "))
n2 = int(input("Digite outro numero inteiro: "))

impar = 0
for i in range(n1, n2 + 1):
    if not i % 2 == 0:
        impar += 1

print(impar)

