valores = 0
numero = int(input("Digite um numero: "))
total = 0
while numero >= 0:
    total += numero
    valores +=1
    numero = int(input("Digite um numero: "))

media = total / valores

print(f"A média aritmética dos valores possitivos que você digitou é {media}")