intervalo1 = 0
intervalo2 = 0
intervalo3 = 0
intervalo4 = 0

numero = int(input("Digite um numero: "))
while numero > 0:
    if numero < 0 or numero > 100:
        print("Numero invalido")
    else:
        if numero == 0 or numero < 26:
            intervalo1 += 1
        else:
            if numero < 51:
                intervalo2 += 1
            else:
                if numero < 76:
                    intervalo3 += 1
                else:
                    intervalo4 += 1
    numero = int(input("Digite um numero: "))
if intervalo1 > 0:
    print(f"A quantidade de números dentre o íntervalo [0,25] é de {intervalo1}")
if intervalo2 > 0:
    print(f"A quantidade de números dentre o intervalo [26,50] é de {intervalo2}")
if intervalo3 > 0:
    print(f"A quantidade de números dentre o intervalo [51,75] é de {intervalo3} ")
if intervalo4 > 0:
    print(f"A quantidade de números dentre o intervalo [76, 100] é de {intervalo4} ")


