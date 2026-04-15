numeros = int(input("Digite um numero: "))

total_num = 0
numeros_pares = 0
numeros_impares = 0
total_par = 0
total = 0

while numeros != 0:
    total += numeros
    par = (numeros % 2) == 0
    total_num += 1
    if numeros < 0:
        print("Digite um número positivo")
    else:
        if par == True:
            numeros_pares += 1
            total_par += numeros
        else:
            numeros_impares += 1
    numeros = int(input("Digite um numero: "))

media_geral = total / total_num
media_par = total_par / total_num

print(f"A quantidade de números pares é de {numeros_pares} e a qunatidade de ímpares é de {numeros_impares}")
print(f"A média de números pares é: {media_par}")
print(f"A média geral é: {media_geral}")