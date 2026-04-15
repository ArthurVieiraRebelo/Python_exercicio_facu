numero = int(input("Digite um numero: "))
soma = 0
if numero < 1:
    print("Numero invalido")
else:
    for i in range(1, numero + 1):
        divisor = 1/i
        soma += divisor
        if i == 1:
            print("1")
        if i > 1:
            print(f"1/{i}")
    print(f"A soma dos números é igual a: {soma:.2f}")
