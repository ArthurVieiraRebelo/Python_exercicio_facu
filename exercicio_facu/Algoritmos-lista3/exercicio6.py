total = 0

valores = int(input("Digite quantos valores você quer para fazer a media: "))

for i in range(1, valores + 1):
    numero = int(input("digite um numero: "))
    if numero > 0:
        total += numero
    else:
        print("digite um numero positivo")
        valores -= 1
media = total / valores

print(f"A média aritmética dos valores possitivos que você digitou é {media}")