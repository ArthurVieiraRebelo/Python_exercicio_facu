#Faça um algoritmo para verificar e imprimir entre 4 números lidos qual é o menor.

numero_1 = float(input("Digite o primeiro numero: "))
numero_2 = float(input("Digite o segundo numero: "))
numero_3 = float(input("Digite o terceiro numero: "))
numero_4 = float(input("Digite o quarto numero: "))

if numero_1 < numero_2 and numero_1 < numero_3 and numero_1 < numero_4:
    numero = numero_1
else:
    if numero_2 < numero_3 and numero_2 < numero_4:
        numero = numero_2
    else:
        if numero_3 < numero_4:
            numero = numero_3
        else:
            numero = numero_4
print(numero)
