from random import randint

numero_aleatorio = randint(1,16)
total = 0
positivo = 0
negativo =0

for i in range(numero_aleatorio):
    numero = int(input("Digite um número: "))
    total += numero
    if numero > 0:
        positivo += 1
    else:
        negativo += 1
media = total / numero_aleatorio
porcentual_positivo = positivo / numero_aleatorio * 100
porcentual_negativo = negativo / numero_aleatorio * 100

print(f"A média aritmética dos números é: {media}")
print(f"O total de números positivo é de {positivo} e o dos negativos é {negativo}")
print(f"O percentual de números positivos é de {porcentual_positivo}% e os do negativos {porcentual_negativo}%")

