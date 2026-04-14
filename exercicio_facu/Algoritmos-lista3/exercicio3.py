numero = int(input("digite um numero: "))

fatorial = 1

if numero <= 0:
    print("Número inválido")
else:
    for i in range(1, numero + 1):
        fatorial = fatorial * i
    print(fatorial)


