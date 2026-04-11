numero1 = int(input("Digite o primeiro valor: "))
numero2 = int(input("Digite o segundo valor: "))

intervalo1 = numero1
intervalo2 = numero2

if numero1 < numero2:
    print(numero1)
    for i in range(numero1, numero2):
        intervalo1 += 1
        print(intervalo1)
else:
    print(numero2)
    for i in range(numero2, numero1):
        intervalo2 += 1
        print(intervalo2)
        