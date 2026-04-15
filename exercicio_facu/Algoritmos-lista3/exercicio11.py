total = 0
positivo = 0
negativo =0
pergunta = "sim"
vezes = 0
while pergunta == "s" or "S":
    vezes += 1
    numero = int(input("Digite um número: "))
    total += numero
    if numero > 0:
        positivo += 1
    else:
        negativo += 1
    pergunta = str(input("Quer continuar? [S/N] "))
media = total / vezes
porcentual_positivo = (positivo / vezes) * 100
porcentual_negativo = (negativo / vezes) * 100

print(f"A média aritmética dos números é: {media}")
print(f"O total de números positivo é de {positivo} e o dos negativos é {negativo}")
print(f"O percentual de números positivos é de {porcentual_positivo}% e os do negativos {porcentual_negativo}%")

