numero = int(input("Digite um número: "))
fatorial = 1
soma = 0
for i in range(1, numero + 1):
    fatorial *= i
    divisor = 1 / fatorial
    soma += divisor
print(f"A soma é {soma:.2f}")