vezes_lidas = int(input("Quantos vezes deseja ser perguntado um número? "))

for i in range (vezes_lidas):
    numero = int(input("Digite um número: "))
    fatorial = 1
    for t in range(1, numero + 1):
        if t == 1:
            print(numero)
        fatorial = fatorial * t
    print(f"O fatorial do número {numero} é {fatorial}")